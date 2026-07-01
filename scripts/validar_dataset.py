from __future__ import annotations

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

ARCHIVOS = {
    "cliente": DATA_DIR / "dim_cliente.csv",
    "producto": DATA_DIR / "dim_producto.csv",
    "promocion": DATA_DIR / "dim_promocion.csv",
    "tiempo": DATA_DIR / "dim_tiempo.csv",
    "tienda": DATA_DIR / "dim_tienda.csv",
    "ventas": DATA_DIR / "fact_ventas.csv",
}


def leer_csv(nombre: str) -> pd.DataFrame:
    path = ARCHIVOS[nombre]

    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")

    return pd.read_csv(path, sep=";", encoding="utf-8")


def assert_sin_nulos(df: pd.DataFrame, columnas: list[str], nombre_tabla: str) -> None:
    nulos = df[columnas].isna().sum()
    nulos = nulos[nulos > 0]

    if not nulos.empty:
        raise ValueError(f"{nombre_tabla} tiene nulos en columnas críticas:\n{nulos}")


def assert_pk_unica(df: pd.DataFrame, columna: str, nombre_tabla: str) -> None:
    duplicados = df[columna].duplicated().sum()

    if duplicados > 0:
        raise ValueError(f"{nombre_tabla}.{columna} tiene {duplicados} duplicados.")


def validar_archivos() -> dict[str, pd.DataFrame]:
    print("Validando existencia y lectura de archivos...")

    dataframes = {nombre: leer_csv(nombre) for nombre in ARCHIVOS}

    for nombre, df in dataframes.items():
        if df.empty:
            raise ValueError(f"{nombre} está vacío.")

        print(f"OK {nombre}: {len(df):,} filas")

    return dataframes


def validar_dimensiones(df_cliente, df_producto, df_promocion, df_tiempo, df_tienda) -> None:
    print("\nValidando dimensiones...")

    assert_pk_unica(df_cliente, "id_cliente", "dim_cliente")
    assert_pk_unica(df_producto, "id_producto", "dim_producto")
    assert_pk_unica(df_promocion, "id_promocion", "dim_promocion")
    assert_pk_unica(df_tiempo, "fecha", "dim_tiempo")
    assert_pk_unica(df_tienda, "id_tienda", "dim_tienda")

    assert_sin_nulos(
        df_cliente,
        ["id_cliente", "nombre", "sexo", "fecha_nacimiento", "distrito", "region", "segmento_programa"],
        "dim_cliente",
    )

    assert_sin_nulos(
        df_producto,
        ["id_producto", "nombre", "categoria", "subcategoria", "precio_lista", "costo_unitario_promedio"],
        "dim_producto",
    )

    assert_sin_nulos(
        df_promocion,
        ["id_promocion", "tipo", "descuento_pct", "fecha_inicio", "fecha_fin"],
        "dim_promocion",
    )

    assert_sin_nulos(
        df_tiempo,
        ["fecha", "dia", "mes", "trimestre", "anio", "dia_semana", "es_feriado"],
        "dim_tiempo",
    )

    assert_sin_nulos(
        df_tienda,
        ["id_tienda", "nombre", "canal", "region"],
        "dim_tienda",
    )

    if (pd.to_numeric(df_producto["precio_lista"], errors="coerce") <= 0).any():
        raise ValueError("Hay productos con precio_lista <= 0.")

    if (pd.to_numeric(df_producto["costo_unitario_promedio"], errors="coerce") <= 0).any():
        raise ValueError("Hay productos con costo_unitario_promedio <= 0.")

    print("OK dimensiones consistentes.")


def validar_fact_ventas(df_ventas, df_cliente, df_producto, df_promocion, df_tiempo, df_tienda) -> None:
    print("\nValidando fact_ventas...")

    columnas_obligatorias = [
        "id_venta",
        "numero_linea",
        "fecha",
        "id_cliente",
        "id_tienda",
        "id_producto",
        "id_promocion",
        "cantidad",
        "precio_unitario_lista",
        "descuento_pct",
        "precio_unitario_final",
        "importe_venta",
        "costo_total",
        "margen",
    ]

    assert_sin_nulos(df_ventas, columnas_obligatorias, "fact_ventas")

    if df_ventas.duplicated(["id_venta", "numero_linea"]).any():
        raise ValueError("Hay líneas duplicadas para la misma combinación id_venta + numero_linea.")

    validar_fk(df_ventas, "id_cliente", df_cliente, "id_cliente", "fact_ventas → dim_cliente")
    validar_fk(df_ventas, "id_producto", df_producto, "id_producto", "fact_ventas → dim_producto")
    validar_fk(df_ventas, "id_promocion", df_promocion, "id_promocion", "fact_ventas → dim_promocion")
    validar_fk(df_ventas, "id_tienda", df_tienda, "id_tienda", "fact_ventas → dim_tienda")
    validar_fk(df_ventas, "fecha", df_tiempo, "fecha", "fact_ventas → dim_tiempo")

    for col in ["cantidad", "precio_unitario_lista", "precio_unitario_final", "importe_venta", "costo_total"]:
        valores = pd.to_numeric(df_ventas[col], errors="coerce")
        if valores.isna().any():
            raise ValueError(f"fact_ventas.{col} tiene valores no numéricos.")
        if (valores < 0).any():
            raise ValueError(f"fact_ventas.{col} tiene valores negativos.")

    if (pd.to_numeric(df_ventas["cantidad"], errors="coerce") <= 0).any():
        raise ValueError("fact_ventas.cantidad tiene valores <= 0.")

    print("OK fact_ventas consistente.")


def validar_fk(df_fact, col_fact, df_dim, col_dim, nombre_relacion: str) -> None:
    valores_fact = set(df_fact[col_fact].dropna())
    valores_dim = set(df_dim[col_dim].dropna())

    faltantes = valores_fact - valores_dim

    if faltantes:
        muestra = list(faltantes)[:10]
        raise ValueError(
            f"Error FK en {nombre_relacion}. "
            f"Hay {len(faltantes)} valores sin correspondencia. Muestra: {muestra}"
        )


def validar_fechas(df_ventas, df_cliente, df_promocion, df_tiempo) -> None:
    print("\nValidando fechas...")

    ventas = df_ventas.copy()
    clientes = df_cliente.copy()
    promociones = df_promocion.copy()
    tiempo = df_tiempo.copy()

    ventas["fecha"] = pd.to_datetime(ventas["fecha"], errors="coerce")
    clientes["fecha_alta"] = pd.to_datetime(clientes["fecha_alta"], errors="coerce")
    promociones["fecha_inicio"] = pd.to_datetime(promociones["fecha_inicio"], errors="coerce", dayfirst=True)
    promociones["fecha_fin"] = pd.to_datetime(promociones["fecha_fin"], errors="coerce", dayfirst=True)
    tiempo["fecha"] = pd.to_datetime(tiempo["fecha"], errors="coerce")

    if ventas["fecha"].isna().any():
        raise ValueError("fact_ventas.fecha tiene fechas inválidas.")

    if tiempo["fecha"].isna().any():
        raise ValueError("dim_tiempo.fecha tiene fechas inválidas.")

    primera_venta = ventas.groupby("id_cliente")["fecha"].min()
    clientes_idx = clientes.set_index("id_cliente")

    comparacion = clientes_idx["fecha_alta"].eq(primera_venta)
    no_coinciden = (~comparacion).sum()

    if no_coinciden > 0:
        raise ValueError(f"Hay {no_coinciden} clientes cuya fecha_alta no coincide con su primera venta.")

    ventas_promo = ventas.merge(
        promociones[["id_promocion", "tipo", "fecha_inicio", "fecha_fin"]],
        on="id_promocion",
        how="left",
    )

    fuera_vigencia = ventas_promo[
        (ventas_promo["fecha"] < ventas_promo["fecha_inicio"])
        | (ventas_promo["fecha"] > ventas_promo["fecha_fin"])
    ]

    if not fuera_vigencia.empty:
        raise ValueError(f"Hay {len(fuera_vigencia):,} líneas con promoción fuera de vigencia.")

    print("OK fechas consistentes.")


def validar_asociaciones_productos(df_producto) -> None:
    print("\nValidando asociaciones de productos...")

    columnas_asociacion = ["asociacion_1", "asociacion_2", "asociacion_3"]
    columnas_existentes = [c for c in columnas_asociacion if c in df_producto.columns]

    if not columnas_existentes:
        print("AVISO: dim_producto no tiene columnas de asociación. Se omite validación.")
        return

    subcategorias_validas = set(
        df_producto["subcategoria"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    errores = []

    for _, row in df_producto.iterrows():
        id_producto = row["id_producto"]

        for col in columnas_existentes:
            valor = row[col]

            if pd.isna(valor) or str(valor).strip() == "":
                continue

            asociacion = str(valor).strip().lower()

            if asociacion in {"nan", "none", "null", "na", "n/a", "sin asociacion", "sin_asociacion"}:
                continue

            if asociacion not in subcategorias_validas:
                errores.append((id_producto, col, valor))

    if errores:
        muestra = errores[:20]
        raise ValueError(
            "Hay asociaciones que no corresponden a ninguna subcategoría existente. "
            f"Total errores: {len(errores)}. Muestra: {muestra}"
        )

    print("OK asociaciones apuntan a subcategorías válidas.")


def validar_canastas_generadas(df_ventas, df_producto) -> None:
    print("\nValidando canastas generadas...")

    ventas_producto = df_ventas.merge(
        df_producto[["id_producto", "subcategoria"]],
        on="id_producto",
        how="left",
    )

    productos_sin_subcategoria = ventas_producto["subcategoria"].isna().sum()
    if productos_sin_subcategoria > 0:
        raise ValueError(f"Hay {productos_sin_subcategoria} líneas de venta con producto sin subcategoría.")

    lineas_por_ticket = ventas_producto.groupby("id_venta")["numero_linea"].count()

    if (lineas_por_ticket <= 0).any():
        raise ValueError("Hay tickets sin líneas.")

    if (lineas_por_ticket > 8).any():
        raise ValueError("Hay tickets con más de 8 líneas, rompe MAX_LINEAS_POR_VENTA.")

    duplicados_producto_ticket = ventas_producto.duplicated(["id_venta", "id_producto"]).sum()

    if duplicados_producto_ticket > 0:
        raise ValueError(f"Hay {duplicados_producto_ticket} productos repetidos dentro del mismo ticket.")

    print("OK canastas sin duplicados ni exceso de líneas.")


def imprimir_resumen(df_ventas, df_cliente, df_producto, df_tiempo) -> None:
    print("\nResumen del dataset limpio:")
    print(f"Clientes: {len(df_cliente):,}")
    print(f"Productos: {len(df_producto):,}")
    print(f"Días calendario: {len(df_tiempo):,}")
    print(f"Tickets de venta: {df_ventas['id_venta'].nunique():,}")
    print(f"Líneas de venta: {len(df_ventas):,}")
    print(f"Fecha mínima venta: {df_ventas['fecha'].min()}")
    print(f"Fecha máxima venta: {df_ventas['fecha'].max()}")
    print(f"Clientes con venta: {df_ventas['id_cliente'].nunique():,}")
    print(f"Productos vendidos: {df_ventas['id_producto'].nunique():,}")


def main() -> None:
    dfs = validar_archivos()

    df_cliente = dfs["cliente"]
    df_producto = dfs["producto"]
    df_promocion = dfs["promocion"]
    df_tiempo = dfs["tiempo"]
    df_tienda = dfs["tienda"]
    df_ventas = dfs["ventas"]

    validar_dimensiones(df_cliente, df_producto, df_promocion, df_tiempo, df_tienda)
    validar_fact_ventas(df_ventas, df_cliente, df_producto, df_promocion, df_tiempo, df_tienda)
    validar_fechas(df_ventas, df_cliente, df_promocion, df_tiempo)
    validar_asociaciones_productos(df_producto)
    validar_canastas_generadas(df_ventas, df_producto)
    imprimir_resumen(df_ventas, df_cliente, df_producto, df_tiempo)

    print("\nVALIDACIÓN COMPLETADA: dataset limpio y consistente.")


if __name__ == "__main__":
    main()