from __future__ import annotations

from typing import Any
import numpy as np
import pandas as pd


def aplicar_formatos_fecha_mixtos(fact_ventas: pd.DataFrame) -> pd.DataFrame:
    """Enero-junio 2024 queda en DD/MM/YYYY; el resto queda ISO YYYY-MM-DD."""
    fact = fact_ventas.copy()
    fecha_dt = pd.to_datetime(fact["fecha"], errors="coerce")

    mascara_antigua = (
        (fecha_dt >= pd.Timestamp("2024-01-01"))
        & (fecha_dt <= pd.Timestamp("2024-06-30"))
    )

    fact.loc[mascara_antigua, "fecha"] = fecha_dt.loc[mascara_antigua].dt.strftime("%d/%m/%Y")
    fact.loc[~mascara_antigua, "fecha"] = fecha_dt.loc[~mascara_antigua].dt.strftime("%Y-%m-%d")

    return fact


def inyectar_valores_faltantes(
    tablas: dict[str, pd.DataFrame],
    rng: np.random.Generator,
) -> dict[str, pd.DataFrame]:
    """Introduce nulos controlados que el ETL puede imputar sin romper el modelo."""
    tablas = {nombre: df.copy() for nombre, df in tablas.items()}

    fact = tablas["fact_ventas"]
    n_descuento = max(1, int(len(fact) * 0.008))
    idx_descuento = rng.choice(fact.index.to_numpy(), size=n_descuento, replace=False)
    fact.loc[idx_descuento, "descuento_pct"] = np.nan
    tablas["fact_ventas"] = fact

    producto = tablas["dim_producto"]
    if "marca" in producto.columns and len(producto) > 20:
        n_marca = max(1, int(len(producto) * 0.015))
        idx_marca = rng.choice(producto.index.to_numpy(), size=n_marca, replace=False)
        producto.loc[idx_marca, "marca"] = np.nan
    tablas["dim_producto"] = producto

    return tablas


def inyectar_duplicados(
    tablas: dict[str, pd.DataFrame],
    seed: int,
) -> dict[str, pd.DataFrame]:
    """Duplica algunas líneas de fact_ventas para que el ETL deduplique por grano."""
    tablas = {nombre: df.copy() for nombre, df in tablas.items()}

    fact = tablas["fact_ventas"]
    n_dup = max(1, int(len(fact) * 0.006))
    duplicados = fact.sample(n=n_dup, random_state=seed).copy()

    tablas["fact_ventas"] = pd.concat([fact, duplicados], ignore_index=True)

    return tablas


def inyectar_ruido_nombres_clientes(
    tablas: dict[str, pd.DataFrame],
    rng: np.random.Generator,
) -> dict[str, pd.DataFrame]:
    """Introduce ruido textual controlado en nombres de clientes.

    No afecta claves, relaciones, segmentos, regiones ni lógica de negocio.
    """
    tablas = {nombre: df.copy() for nombre, df in tablas.items()}

    clientes = tablas["dim_cliente"].copy()

    if "nombre" not in clientes.columns:
        tablas["dim_cliente"] = clientes
        return tablas

    indices = clientes.index.to_numpy()

    n_mayus = max(1, int(len(clientes) * 0.15))
    n_minus = max(1, int(len(clientes) * 0.15))

    idx_mayus = rng.choice(indices, size=n_mayus, replace=False)
    restantes = np.setdiff1d(indices, idx_mayus)
    idx_minus = rng.choice(restantes, size=n_minus, replace=False)

    clientes.loc[idx_mayus, "nombre"] = (
        clientes.loc[idx_mayus, "nombre"]
        .astype(str)
        .str.upper()
    )

    clientes.loc[idx_minus, "nombre"] = (
        clientes.loc[idx_minus, "nombre"]
        .astype(str)
        .str.lower()
    )

    tablas["dim_cliente"] = clientes
    return tablas


def inyectar_ruido(
    tablas_limpias: dict[str, pd.DataFrame],
    seed: int = 20260701,
) -> dict[str, pd.DataFrame]:
    """Genera la capa raw con ruido controlado a partir de tablas limpias."""
    rng = np.random.default_rng(seed)

    tablas = {nombre: df.copy() for nombre, df in tablas_limpias.items()}

    tablas["fact_ventas"] = aplicar_formatos_fecha_mixtos(tablas["fact_ventas"])
    tablas = inyectar_valores_faltantes(tablas, rng)
    tablas = inyectar_duplicados(tablas, seed)
    tablas = inyectar_ruido_nombres_clientes(tablas, rng)

    return tablas


def resumen_ruido(tablas_raw: dict[str, pd.DataFrame]) -> dict[str, Any]:
    """Resumen simple para mostrar en el notebook 00."""
    fact = tablas_raw["fact_ventas"]
    producto = tablas_raw["dim_producto"]

    return {
        "lineas_fact_ventas_raw": len(fact),
        "tickets_raw": fact["id_venta"].nunique(),
        "duplicados_grano_fact": int(fact.duplicated(["id_venta", "numero_linea"]).sum()),
        "nulos_descuento_pct": int(fact["descuento_pct"].isna().sum()),
        "nulos_marca_producto": int(producto["marca"].isna().sum()) if "marca" in producto.columns else 0,
        "ejemplo_fechas_raw": fact["fecha"].head(8).tolist(),
    }