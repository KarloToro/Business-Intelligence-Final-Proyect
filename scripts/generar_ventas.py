from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
import random
import unicodedata
from typing import Any

import pandas as pd

try:
    from scripts.config import (
        DATA_DIR,
        OUTPUT_DIR,
        SEED,
        TOTAL_CLIENTES,
        FECHA_INICIO_OPERACION,
        probabilidad_recompra,
    )
    from scripts.generar_clientes import generar_clientes
except ModuleNotFoundError:
    from config import (
        DATA_DIR,
        OUTPUT_DIR,
        SEED,
        TOTAL_CLIENTES,
        FECHA_INICIO_OPERACION,
        probabilidad_recompra,
    )
    from generar_clientes import generar_clientes


# -----------------------------------------------------------------------------
# Parámetros del algoritmo de ventas
# -----------------------------------------------------------------------------
FECHA_FIN_EXCLUSIVA_OPERACION = "2026-01-01"
VENTAS_DIARIAS_BASE = 45
VENTAS_DIARIAS_PICO = 60
MESES_PICO = {7, 12}

PROB_PRODUCTO_ESTRELLA = 0.80
PROB_ASOCIACION = 0.15
MAX_PROFUNDIDAD_ASOCIACION = 2
MAX_LINEAS_POR_VENTA = 8
COLUMNAS_ASOCIACION = ("asociacion_1", "asociacion_2", "asociacion_3")


# -----------------------------------------------------------------------------
# Utilidades generales
# -----------------------------------------------------------------------------
def _parse_date(valor: Any) -> datetime.date:
    if hasattr(valor, "date") and not isinstance(valor, str):
        return valor.date()
    return datetime.strptime(str(valor), "%Y-%m-%d").date()


def _leer_csv_semicolon(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo requerido: {path}")
    return pd.read_csv(path, sep=";")


def _normalizar_texto(valor: Any) -> str:
    if valor is None or pd.isna(valor):
        return ""
    texto = str(valor).strip()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(ch for ch in texto if not unicodedata.combining(ch))
    return texto.lower().strip()


def _limpiar_asociacion(valor: Any) -> str | None:
    if valor is None or pd.isna(valor):
        return None
    texto = str(valor).strip()
    if not texto:
        return None
    if texto.lower() in {"nan", "none", "null", "na", "n/a", "sin asociacion", "sin_asociacion"}:
        return None
    return texto


def _normalizar_pesos(valores: pd.Series | list[float]) -> list[float]:
    pesos = pd.to_numeric(pd.Series(valores), errors="coerce").fillna(0).clip(lower=0)
    total = float(pesos.sum())
    if total <= 0:
        raise ValueError("La suma de pesos debe ser mayor que cero.")
    return (pesos / total).tolist()


# -----------------------------------------------------------------------------
# Calendario de tickets
# -----------------------------------------------------------------------------
def construir_calendario_tickets(
    fecha_inicio: str = FECHA_INICIO_OPERACION,
    fecha_fin_exclusiva: str = FECHA_FIN_EXCLUSIVA_OPERACION,
    ventas_diarias_base: int = VENTAS_DIARIAS_BASE,
    ventas_diarias_pico: int = VENTAS_DIARIAS_PICO,
    meses_pico: set[int] = MESES_PICO,
) -> list[datetime.date]:
    """Devuelve una lista de fechas, una por ticket esperado.

    El rango es [fecha_inicio, fecha_fin_exclusiva). Para 2024-01-01 a
    2026-01-01 se obtienen 34,755 tickets:
    - 45 tickets diarios en meses normales.
    - 60 tickets diarios en julio y diciembre.
    """
    inicio = _parse_date(fecha_inicio)
    fin_exclusiva = _parse_date(fecha_fin_exclusiva)
    if fin_exclusiva <= inicio:
        raise ValueError("fecha_fin_exclusiva debe ser posterior a fecha_inicio.")

    fechas_tickets: list[datetime.date] = []
    fecha = inicio
    while fecha < fin_exclusiva:
        cantidad = ventas_diarias_pico if fecha.month in meses_pico else ventas_diarias_base
        fechas_tickets.extend([fecha] * cantidad)
        fecha += timedelta(days=1)
    return fechas_tickets


# -----------------------------------------------------------------------------
# Preparación de dimensiones
# -----------------------------------------------------------------------------
def _preparar_tiendas_por_region(df_tienda: pd.DataFrame) -> dict[str, tuple[list[dict], list[float]]]:
    columnas_requeridas = {"id_tienda", "nombre", "canal", "region", "prob_seleccion"}
    faltantes = columnas_requeridas - set(df_tienda.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en dim_tienda: {sorted(faltantes)}")

    tiendas_por_region: dict[str, tuple[list[dict], list[float]]] = {}
    for region, grupo in df_tienda.groupby("region"):
        grupo = grupo.copy()
        grupo["prob_seleccion"] = pd.to_numeric(grupo["prob_seleccion"], errors="coerce").fillna(0)
        grupo = grupo[grupo["prob_seleccion"] > 0]
        if grupo.empty:
            raise ValueError(f"La región {region!r} no tiene tiendas con prob_seleccion positiva.")
        tiendas_por_region[str(region)] = (
            grupo.to_dict("records"),
            _normalizar_pesos(grupo["prob_seleccion"]),
        )
    return tiendas_por_region


def _preparar_productos(df_producto: pd.DataFrame) -> dict[str, Any]:
    columnas_requeridas = {
        "id_producto",
        "nombre",
        "categoria",
        "subcategoria",
        "precio_lista",
        "costo_unitario_promedio",
        "producto_estrella",
    }
    faltantes = columnas_requeridas - set(df_producto.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en dim_producto: {sorted(faltantes)}")

    df = df_producto.copy()
    for col in COLUMNAS_ASOCIACION:
        if col not in df.columns:
            df[col] = pd.NA

    df["precio_lista"] = pd.to_numeric(df["precio_lista"], errors="coerce")
    df["costo_unitario_promedio"] = pd.to_numeric(df["costo_unitario_promedio"], errors="coerce")
    df = df.dropna(subset=["id_producto", "subcategoria", "precio_lista", "costo_unitario_promedio"])
    if df.empty:
        raise ValueError("dim_producto no tiene productos válidos.")

    producto_estrella_normalizado = df["producto_estrella"].astype(str).str.strip().str.lower()
    df["producto_estrella"] = producto_estrella_normalizado.isin({"true", "1", "si", "sí", "yes", "y"})

    productos = df.to_dict("records")
    productos_estrella = [p for p in productos if bool(p["producto_estrella"])]
    productos_no_estrella = [p for p in productos if not bool(p["producto_estrella"])]

    if not productos_estrella:
        raise ValueError("No existen productos marcados como producto_estrella=True.")
    if not productos_no_estrella:
        raise ValueError("No existen productos marcados como producto_estrella=False.")

    productos_por_subcategoria: dict[str, list[dict]] = defaultdict(list)
    for producto in productos:
        productos_por_subcategoria[_normalizar_texto(producto["subcategoria"])].append(producto)

    return {
        "productos_estrella": productos_estrella,
        "productos_no_estrella": productos_no_estrella,
        "productos_por_subcategoria": dict(productos_por_subcategoria),
    }


def _preparar_promociones(df_promocion: pd.DataFrame) -> pd.DataFrame:
    columnas_requeridas = {"id_promocion", "tipo", "descuento_pct", "fecha_inicio", "fecha_fin"}
    faltantes = columnas_requeridas - set(df_promocion.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en dim_promocion: {sorted(faltantes)}")

    df = df_promocion.copy()
    df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"], dayfirst=True, errors="coerce").dt.date
    df["fecha_fin"] = pd.to_datetime(df["fecha_fin"], dayfirst=True, errors="coerce").dt.date
    df["descuento_pct"] = pd.to_numeric(df["descuento_pct"], errors="coerce").fillna(0.0)
    df = df.dropna(subset=["id_promocion", "tipo", "fecha_inicio", "fecha_fin"])

    if df.empty:
        raise ValueError("dim_promocion no tiene promociones válidas.")
    return df


def _preparar_promos_por_fecha(
    promociones: pd.DataFrame,
    fechas_tickets: list[datetime.date],
) -> dict[datetime.date, list[dict]]:
    fechas_unicas = sorted(set(fechas_tickets))
    promos_por_fecha: dict[datetime.date, list[dict]] = {}

    sin_promocion = promociones[promociones["tipo"].astype(str).str.lower().eq("sin_promocion")]
    if sin_promocion.empty:
        fallback_sin_promo = {"id_promocion": 1, "tipo": "sin_promocion", "descuento_pct": 0.0}
    else:
        fallback_sin_promo = sin_promocion.iloc[0].to_dict()

    for fecha in fechas_unicas:
        candidatas = promociones[
            (promociones["fecha_inicio"].le(fecha))
            & (promociones["fecha_fin"].ge(fecha))
        ].copy()
        if candidatas.empty:
            candidatas = pd.DataFrame([fallback_sin_promo])

        candidatas["peso_aplicacion"] = candidatas["tipo"].map(
            {
                "sin_promocion": 0.82,
                "descuento_directo": 0.12,
                "combo": 0.10,
                "ciber_online": 0.15,
                "fidelizacion": 0.10,
            }
        ).fillna(0.05)

        promos_por_fecha[fecha] = candidatas.to_dict("records")
    return promos_por_fecha


# -----------------------------------------------------------------------------
# Selecciones del ticket
# -----------------------------------------------------------------------------
def _seleccionar_cliente(
    clientes_records: list[dict],
    indice_ticket: int,
    pesos_recompra: list[float],
    rng: random.Random,
) -> tuple[int, dict]:
    """Primera etapa: cliente secuencial. Luego: selección ponderada por recompra."""
    if indice_ticket < len(clientes_records):
        return indice_ticket, clientes_records[indice_ticket]

    indices = list(range(len(clientes_records)))
    idx = rng.choices(indices, weights=pesos_recompra, k=1)[0]
    return idx, clientes_records[idx]


def _seleccionar_tienda(
    region_cliente: str,
    tiendas_por_region: dict[str, tuple[list[dict], list[float]]],
    rng: random.Random,
) -> dict:
    if region_cliente not in tiendas_por_region:
        raise ValueError(f"No hay tiendas disponibles para la región del cliente: {region_cliente!r}")
    tiendas, pesos = tiendas_por_region[region_cliente]
    return rng.choices(tiendas, weights=pesos, k=1)[0]


def _seleccionar_producto_base(productos_info: dict[str, Any], rng: random.Random) -> dict:
    if rng.random() < PROB_PRODUCTO_ESTRELLA:
        return rng.choice(productos_info["productos_estrella"])
    return rng.choice(productos_info["productos_no_estrella"])


def _seleccionar_producto_por_subcategoria(
    subcategoria: str,
    productos_info: dict[str, Any],
    rng: random.Random,
    ids_ya_elegidos: set[int],
) -> dict | None:
    clave = _normalizar_texto(subcategoria)
    candidatos = productos_info["productos_por_subcategoria"].get(clave, [])
    if not candidatos:
        return None

    candidatos_no_repetidos = [p for p in candidatos if int(p["id_producto"]) not in ids_ya_elegidos]
    candidatos_finales = candidatos_no_repetidos or candidatos
    elegido = rng.choice(candidatos_finales)

    if int(elegido["id_producto"]) in ids_ya_elegidos:
        return None
    return elegido


def _agregar_asociaciones_recursivas(
    producto_origen: dict,
    productos_ticket: list[dict],
    ids_ya_elegidos: set[int],
    productos_info: dict[str, Any],
    rng: random.Random,
    profundidad_actual: int,
) -> None:
    if profundidad_actual >= MAX_PROFUNDIDAD_ASOCIACION:
        return
    if len(productos_ticket) >= MAX_LINEAS_POR_VENTA:
        return

    for columna in COLUMNAS_ASOCIACION:
        if len(productos_ticket) >= MAX_LINEAS_POR_VENTA:
            break

        subcategoria_asociada = _limpiar_asociacion(producto_origen.get(columna))
        if not subcategoria_asociada:
            continue

        if rng.random() >= PROB_ASOCIACION:
            continue

        producto_asociado = _seleccionar_producto_por_subcategoria(
            subcategoria=subcategoria_asociada,
            productos_info=productos_info,
            rng=rng,
            ids_ya_elegidos=ids_ya_elegidos,
        )
        if producto_asociado is None:
            continue

        productos_ticket.append(producto_asociado)
        ids_ya_elegidos.add(int(producto_asociado["id_producto"]))

        # Recursividad limitada: permite canastas más naturales sin tickets exagerados.
        _agregar_asociaciones_recursivas(
            producto_origen=producto_asociado,
            productos_ticket=productos_ticket,
            ids_ya_elegidos=ids_ya_elegidos,
            productos_info=productos_info,
            rng=rng,
            profundidad_actual=profundidad_actual + 1,
        )


def _generar_productos_ticket(productos_info: dict[str, Any], rng: random.Random) -> list[dict]:
    producto_base = _seleccionar_producto_base(productos_info, rng)
    productos_ticket = [producto_base]
    ids_ya_elegidos = {int(producto_base["id_producto"])}

    _agregar_asociaciones_recursivas(
        producto_origen=producto_base,
        productos_ticket=productos_ticket,
        ids_ya_elegidos=ids_ya_elegidos,
        productos_info=productos_info,
        rng=rng,
        profundidad_actual=0,
    )
    return productos_ticket


def _elegir_promocion(
    fecha_venta: datetime.date,
    segmento_cliente: str,
    tienda: dict,
    promos_por_fecha: dict[datetime.date, list[dict]],
    rng: random.Random,
) -> dict:
    candidatas = list(promos_por_fecha.get(fecha_venta, []))
    if not candidatas:
        candidatas = [{"id_promocion": 1, "tipo": "sin_promocion", "descuento_pct": 0.0, "peso_aplicacion": 1.0}]

    canal = _normalizar_texto(tienda.get("canal", ""))
    candidatas_filtradas: list[dict] = []
    for promo in candidatas:
        tipo = str(promo.get("tipo", "")).strip()
        if tipo == "fidelizacion" and segmento_cliente == "No afiliado":
            continue
        if tipo == "ciber_online" and canal != "online":
            continue
        candidatas_filtradas.append(promo)

    if not candidatas_filtradas:
        candidatas_filtradas = [{"id_promocion": 1, "tipo": "sin_promocion", "descuento_pct": 0.0, "peso_aplicacion": 1.0}]

    pesos = [float(p.get("peso_aplicacion", 0.05)) for p in candidatas_filtradas]
    elegida = rng.choices(candidatas_filtradas, weights=pesos, k=1)[0]
    return {
        "id_promocion": int(elegida["id_promocion"]),
        "descuento_pct": float(elegida.get("descuento_pct", 0.0)),
    }


def _cantidad_aleatoria(rng: random.Random) -> int:
    return rng.choices([1, 2, 3, 4, 5], weights=[0.58, 0.25, 0.10, 0.05, 0.02], k=1)[0]


def _crear_linea_venta(
    id_venta: int,
    fecha: datetime.date,
    cliente: dict,
    tienda: dict,
    producto: dict,
    promocion: dict,
    numero_linea: int,
    rng: random.Random,
) -> dict:
    cantidad = _cantidad_aleatoria(rng)
    precio_lista = float(producto["precio_lista"])
    costo_unitario = float(producto["costo_unitario_promedio"])
    descuento_pct = float(promocion["descuento_pct"])

    precio_unitario_final = round(precio_lista * (1 - descuento_pct), 2)
    importe_venta = round(precio_unitario_final * cantidad, 2)
    costo_total = round(costo_unitario * cantidad, 2)
    margen = round(importe_venta - costo_total, 2)

    return {
        "id_venta": int(id_venta),
        "numero_linea": int(numero_linea),
        "fecha": fecha.isoformat(),
        "id_cliente": int(cliente["id_cliente"]),
        "id_tienda": int(tienda["id_tienda"]),
        "id_producto": int(producto["id_producto"]),
        "id_promocion": int(promocion["id_promocion"]),
        "cantidad": int(cantidad),
        "precio_unitario_lista": round(precio_lista, 2),
        "descuento_pct": round(descuento_pct, 4),
        "precio_unitario_final": precio_unitario_final,
        "importe_venta": importe_venta,
        "costo_total": costo_total,
        "margen": margen,
    }


# -----------------------------------------------------------------------------
# Generador principal
# -----------------------------------------------------------------------------
def generar_ventas_y_actualizar_clientes(
    total_clientes: int = TOTAL_CLIENTES,
    seed: int = SEED,
    fecha_inicio: str = FECHA_INICIO_OPERACION,
    fecha_fin_exclusiva: str = FECHA_FIN_EXCLUSIVA_OPERACION,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Genera dim_cliente actualizado y fact_ventas con el algoritmo definitivo.

    Reglas implementadas:
    1. El calendario produce 45 tickets diarios, excepto julio y diciembre con 60.
    2. Los primeros tickets garantizan una primera compra para cada cliente.
    3. Las recompras seleccionan clientes ponderando por probabilidad_recompra.
    4. La tienda se elige después del cliente y solo dentro de su región.
    5. Cada ticket parte de un producto base: 80% estrella y 20% no estrella.
    6. Las asociaciones de productos se agregan con probabilidad de 15%, con límite
       de profundidad y de líneas por venta.
    7. Las promociones solo aplican si están vigentes en la fecha del ticket.
    8. fecha_alta se toma de la primera venta real del cliente y no se modifica.
    """
    rng = random.Random(seed)

    fechas_tickets = construir_calendario_tickets(
        fecha_inicio=fecha_inicio,
        fecha_fin_exclusiva=fecha_fin_exclusiva,
    )
    if len(fechas_tickets) < total_clientes:
        raise ValueError(
            "El calendario genera menos tickets que clientes. No se puede garantizar "
            "una primera compra para cada cliente."
        )

    clientes = generar_clientes(total_clientes=total_clientes, seed=seed).copy()
    clientes = clientes.sort_values("id_cliente").reset_index(drop=True)
    clientes_records = clientes.to_dict("records")

    productos_info = _preparar_productos(_leer_csv_semicolon(DATA_DIR / "dim_producto.csv"))
    tiendas_por_region = _preparar_tiendas_por_region(_leer_csv_semicolon(DATA_DIR / "dim_tienda.csv"))
    promociones = _preparar_promociones(_leer_csv_semicolon(DATA_DIR / "dim_promocion.csv"))
    promos_por_fecha = _preparar_promos_por_fecha(promociones, fechas_tickets)

    pesos_recompra = [float(probabilidad_recompra[c["segmento_programa"]]) for c in clientes_records]

    registros_ventas: list[dict] = []

    for indice_ticket, fecha in enumerate(fechas_tickets):
        id_venta = indice_ticket + 1
        idx_cliente, cliente = _seleccionar_cliente(
            clientes_records=clientes_records,
            indice_ticket=indice_ticket,
            pesos_recompra=pesos_recompra,
            rng=rng,
        )

        if pd.isna(clientes.at[idx_cliente, "fecha_alta"]):
            clientes.at[idx_cliente, "fecha_alta"] = fecha.isoformat()
            cliente["fecha_alta"] = fecha.isoformat()

        tienda = _seleccionar_tienda(
            region_cliente=str(cliente["region"]),
            tiendas_por_region=tiendas_por_region,
            rng=rng,
        )
        productos_ticket = _generar_productos_ticket(productos_info, rng)
        promocion_ticket = _elegir_promocion(
            fecha_venta=fecha,
            segmento_cliente=str(cliente["segmento_programa"]),
            tienda=tienda,
            promos_por_fecha=promos_por_fecha,
            rng=rng,
        )

        for numero_linea, producto in enumerate(productos_ticket, start=1):
            registros_ventas.append(
                _crear_linea_venta(
                    id_venta=id_venta,
                    fecha=fecha,
                    cliente=cliente,
                    tienda=tienda,
                    producto=producto,
                    promocion=promocion_ticket,
                    numero_linea=numero_linea,
                    rng=rng,
                )
            )

    fact_ventas = pd.DataFrame(registros_ventas)
    clientes["fecha_alta"] = pd.to_datetime(clientes["fecha_alta"], errors="coerce").dt.date.astype(str)
    return clientes, fact_ventas


def validar_resultados(clientes: pd.DataFrame, fact_ventas: pd.DataFrame) -> dict[str, Any]:
    """Validaciones básicas para confirmar consistencia del dataset generado."""
    clientes_tmp = clientes.copy()
    ventas_tmp = fact_ventas.copy()
    clientes_tmp["fecha_alta"] = pd.to_datetime(clientes_tmp["fecha_alta"], errors="coerce")
    ventas_tmp["fecha"] = pd.to_datetime(ventas_tmp["fecha"], errors="coerce")

    primera_venta = ventas_tmp.groupby("id_cliente")["fecha"].min()
    clientes_indexados = clientes_tmp.set_index("id_cliente")
    comparacion = clientes_indexados["fecha_alta"].eq(primera_venta)

    tickets_por_fecha = ventas_tmp.drop_duplicates("id_venta").groupby(ventas_tmp["fecha"].dt.date)["id_venta"].count()
    dias_invalidos = []
    for fecha, cantidad in tickets_por_fecha.items():
        esperado = VENTAS_DIARIAS_PICO if fecha.month in MESES_PICO else VENTAS_DIARIAS_BASE
        if int(cantidad) != esperado:
            dias_invalidos.append((fecha.isoformat(), int(cantidad), esperado))

    return {
        "clientes": int(len(clientes_tmp)),
        "tickets": int(ventas_tmp["id_venta"].nunique()),
        "lineas_venta": int(len(ventas_tmp)),
        "fecha_min": str(ventas_tmp["fecha"].min().date()),
        "fecha_max": str(ventas_tmp["fecha"].max().date()),
        "clientes_sin_fecha_alta": int(clientes_tmp["fecha_alta"].isna().sum()),
        "clientes_sin_venta": int(len(set(clientes_tmp["id_cliente"]) - set(ventas_tmp["id_cliente"]))),
        "fecha_alta_no_coincide_con_primera_venta": int((~comparacion).sum()),
        "dias_con_cantidad_tickets_incorrecta": dias_invalidos[:10],
        "total_dias_invalidos": int(len(dias_invalidos)),
    }


def guardar_salidas(clientes: pd.DataFrame, fact_ventas: pd.DataFrame) -> tuple[Path, Path]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ruta_clientes = OUTPUT_DIR / "dim_cliente.csv"
    ruta_ventas = OUTPUT_DIR / "fact_ventas.csv"
    clientes.to_csv(ruta_clientes, sep=";", index=False, encoding="utf-8")
    fact_ventas.to_csv(ruta_ventas, sep=";", index=False, encoding="utf-8")
    return ruta_clientes, ruta_ventas


if __name__ == "__main__":
    clientes_generados, ventas_generadas = generar_ventas_y_actualizar_clientes()
    ruta_clientes, ruta_ventas = guardar_salidas(clientes_generados, ventas_generadas)
    validacion = validar_resultados(clientes_generados, ventas_generadas)

    print("Generación terminada.")
    print(f"Clientes: {validacion['clientes']:,}")
    print(f"Tickets de venta: {validacion['tickets']:,}")
    print(f"Líneas de venta: {validacion['lineas_venta']:,}")
    print(f"Rango ventas: {validacion['fecha_min']} a {validacion['fecha_max']}")
    print(f"Clientes sin fecha_alta: {validacion['clientes_sin_fecha_alta']:,}")
    print(f"Clientes sin venta: {validacion['clientes_sin_venta']:,}")
    print(
        "fecha_alta distinta a primera venta: "
        f"{validacion['fecha_alta_no_coincide_con_primera_venta']:,}"
    )
    print(f"Días con cantidad de tickets incorrecta: {validacion['total_dias_invalidos']:,}")
    print(f"Archivo clientes: {ruta_clientes}")
    print(f"Archivo ventas: {ruta_ventas}")
