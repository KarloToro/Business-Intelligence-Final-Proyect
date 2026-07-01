from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
import random

import pandas as pd

try:
    from scripts.config import (
        DATA_DIR,
        OUTPUT_DIR,
        RNG,
        SEED,
        TABLAS_MAESTRAS_DIR,
        TOTAL_CLIENTES,
        distribucion_segmento_programa,
        rangos_edades,
    )
except ModuleNotFoundError:
    from config import (
        DATA_DIR,
        OUTPUT_DIR,
        RNG,
        SEED,
        TABLAS_MAESTRAS_DIR,
        TOTAL_CLIENTES,
        distribucion_segmento_programa,
        rangos_edades,
    )


def _validar_probabilidades(nombre: str, distribucion: dict[str, float], tolerancia: float = 1e-9) -> None:
    total = sum(distribucion.values())
    if abs(total - 1.0) > tolerancia:
        raise ValueError(f"La distribución '{nombre}' debe sumar 1. Actualmente suma {total:.6f}.")


def _elegir_clave_ponderada(distribucion: dict[str, float], rng: random.Random) -> str:
    claves = list(distribucion.keys())
    pesos = list(distribucion.values())
    return rng.choices(claves, weights=pesos, k=1)[0]


def _fecha_aleatoria(fecha_inicio: str, fecha_fin: str, rng: random.Random) -> str:
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    if fin < inicio:
        raise ValueError(f"Rango de fechas inválido: {fecha_inicio} > {fecha_fin}")
    dias = (fin - inicio).days
    return (inicio + timedelta(days=rng.randint(0, dias))).isoformat()


def _leer_columna_csv(path: Path, columna: str, sep: str = ",") -> list[str]:
    df = pd.read_csv(path, sep=sep)
    if columna not in df.columns:
        raise ValueError(f"No se encontró la columna '{columna}' en {path}. Columnas: {list(df.columns)}")
    valores = df[columna].dropna().astype(str).str.strip()
    valores = valores[valores.ne("")]
    if valores.empty:
        raise ValueError(f"La columna '{columna}' en {path} está vacía.")
    return valores.tolist()


def _cargar_distribucion_distritos(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, sep=";")
    columnas_requeridas = {"region", "distrito", "peso_final"}
    faltantes = columnas_requeridas - set(df.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en {path}: {sorted(faltantes)}")

    df = df[["region", "distrito", "peso_final"]].copy()
    df["peso_final"] = pd.to_numeric(df["peso_final"], errors="coerce")
    df = df.dropna(subset=["region", "distrito", "peso_final"])
    df = df[df["peso_final"] > 0]

    total = df["peso_final"].sum()
    if total <= 0:
        raise ValueError("La suma de peso_final debe ser mayor que cero.")

    # Normaliza por seguridad. Tu CSV ya parece venir normalizado, pero esto evita errores por redondeo.
    df["peso_final"] = df["peso_final"] / total
    return df


def generar_clientes(total_clientes: int = TOTAL_CLIENTES, seed: int = SEED) -> pd.DataFrame:
    """Genera dim_cliente sin fecha_alta final.

    fecha_alta se deja como NaT porque se debe completar desde la primera venta real
    del cliente. Esa actualización está implementada en generar_ventas.py.
    """
    rng = random.Random(seed)

    _validar_probabilidades("rangos_edades", {k: v["probabilidad"] for k, v in rangos_edades.items()})
    _validar_probabilidades("distribucion_segmento_programa", distribucion_segmento_programa)

    nombres_mujer = _leer_columna_csv(TABLAS_MAESTRAS_DIR / "nombres_mujer.csv", "nombres_mujer")
    nombres_varon = _leer_columna_csv(TABLAS_MAESTRAS_DIR / "nombres_varon.csv", "nombres_varon")
    apellidos = _leer_columna_csv(TABLAS_MAESTRAS_DIR / "apellidos.csv", "apellidos")
    distritos = _cargar_distribucion_distritos(TABLAS_MAESTRAS_DIR / "distribucion_clientes_por_distrito.csv")

    rango_probs = {rango: valores["probabilidad"] for rango, valores in rangos_edades.items()}
    distrito_opciones = list(distritos.itertuples(index=False, name=None))
    distrito_pesos = distritos["peso_final"].tolist()

    registros = []
    for id_cliente in range(1, total_clientes + 1):
        es_mujer = bool(rng.getrandbits(1))
        sexo = "F" if es_mujer else "M"
        primer_nombre = rng.choice(nombres_mujer if es_mujer else nombres_varon)
        apellido_paterno = rng.choice(apellidos)
        apellido_materno = rng.choice(apellidos)
        nombre = f"{primer_nombre} {apellido_paterno} {apellido_materno}"

        rango_elegido = _elegir_clave_ponderada(rango_probs, rng)
        rango = rangos_edades[rango_elegido]
        fecha_nacimiento = _fecha_aleatoria(rango["fecha_inicio"], rango["fecha_fin"], rng)

        region, distrito, _peso = rng.choices(distrito_opciones, weights=distrito_pesos, k=1)[0]
        segmento = _elegir_clave_ponderada(distribucion_segmento_programa, rng)

        registros.append(
            {
                "id_cliente": id_cliente,
                "nombre": nombre,
                "sexo": sexo,
                "fecha_nacimiento": fecha_nacimiento,
                "distrito": distrito,
                "region": region,
                "fecha_alta": pd.NaT,
                "segmento_programa": segmento,
            }
        )

    return pd.DataFrame(registros)


def guardar_clientes(df_clientes: pd.DataFrame, output_path: Path | None = None) -> Path:
    output_path = output_path or OUTPUT_DIR / "dim_cliente.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_clientes.to_csv(output_path, sep=";", index=False, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    clientes = generar_clientes()
    ruta = guardar_clientes(clientes)
    print(f"Clientes generados: {len(clientes):,}")
    print(f"Archivo creado: {ruta}")
    print(clientes.head())
