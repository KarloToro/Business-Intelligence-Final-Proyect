from __future__ import annotations

from pathlib import Path

import pandas as pd


# ------------------------------------------------------------------
# Definiciones de los campos del datamart
# ------------------------------------------------------------------

DESCRIPCIONES = {
    # fact_ventas
    ("fact_ventas", "id_venta"): (
        "int",
        "PK lógica del ticket",
        "No",
    ),
    ("fact_ventas", "numero_linea"): (
        "int",
        "Número de línea dentro del ticket",
        "No",
    ),
    ("fact_ventas", "fecha"): (
        "date",
        "Fecha de la venta (FK → dim_tiempo)",
        "Sí",
    ),
    ("fact_ventas", "id_cliente"): (
        "int",
        "Cliente (FK → dim_cliente)",
        "Sí",
    ),
    ("fact_ventas", "id_tienda"): (
        "int",
        "Tienda/canal (FK → dim_tienda)",
        "Sí",
    ),
    ("fact_ventas", "id_producto"): (
        "int",
        "Producto (FK → dim_producto)",
        "Sí",
    ),
    ("fact_ventas", "id_promocion"): (
        "int",
        "Promoción aplicada (FK → dim_promocion)",
        "Sí",
    ),
    ("fact_ventas", "cantidad"): (
        "int",
        "Unidades vendidas",
        "No",
    ),
    ("fact_ventas", "precio_unitario_lista"): (
        "float",
        "Precio de lista unitario",
        "No",
    ),
    ("fact_ventas", "descuento_pct"): (
        "float",
        "Descuento aplicado entre 0 y 1",
        "No",
    ),
    ("fact_ventas", "precio_unitario_final"): (
        "float",
        "Precio unitario neto",
        "No",
    ),
    ("fact_ventas", "importe_venta"): (
        "float",
        "Métrica: ingreso de la línea",
        "No",
    ),
    ("fact_ventas", "costo_total"): (
        "float",
        "Costo total de la línea",
        "No",
    ),
    ("fact_ventas", "margen"): (
        "float",
        "Métrica: importe_venta - costo_total",
        "No",
    ),

    # dim_cliente
    ("dim_cliente", "id_cliente"): (
        "int",
        "PK del cliente",
        "Sí",
    ),
    ("dim_cliente", "nombre"): (
        "str",
        "Nombre del cliente",
        "No",
    ),
    ("dim_cliente", "sexo"): (
        "str",
        "Sexo del cliente",
        "No",
    ),
    ("dim_cliente", "fecha_nacimiento"): (
        "date",
        "Fecha de nacimiento",
        "No",
    ),
    ("dim_cliente", "distrito"): (
        "str",
        "Distrito de residencia",
        "No",
    ),
    ("dim_cliente", "region"): (
        "str",
        "Región de residencia",
        "No",
    ),
    ("dim_cliente", "fecha_alta"): (
        "date",
        "Primera compra / alta del cliente",
        "No",
    ),
    ("dim_cliente", "segmento_programa"): (
        "str",
        "Segmento de fidelización",
        "No",
    ),

    # dim_producto
    ("dim_producto", "id_producto"): (
        "int",
        "PK del producto",
        "Sí",
    ),
    ("dim_producto", "nombre"): (
        "str",
        "Nombre del producto",
        "No",
    ),
    ("dim_producto", "categoria"): (
        "str",
        "Categoría comercial",
        "No",
    ),
    ("dim_producto", "subcategoria"): (
        "str",
        "Subcategoría comercial",
        "No",
    ),
    ("dim_producto", "marca"): (
        "str",
        (
            "Marca del producto; si no se identifica se clasifica "
            "como Marca no identificada"
        ),
        "No",
    ),
    ("dim_producto", "precio_lista"): (
        "float",
        "Precio de lista",
        "No",
    ),
    ("dim_producto", "costo_unitario_promedio"): (
        "float",
        "Costo unitario promedio",
        "No",
    ),
    ("dim_producto", "producto_estrella"): (
        "bool",
        "Indicador de producto estrella",
        "No",
    ),
    ("dim_producto", "asociacion_1"): (
        "str",
        "Subcategoría asociada 1",
        "No",
    ),
    ("dim_producto", "asociacion_2"): (
        "str",
        "Subcategoría asociada 2",
        "No",
    ),
    ("dim_producto", "asociacion_3"): (
        "str",
        "Subcategoría asociada 3",
        "No",
    ),

    # dim_tienda
    ("dim_tienda", "id_tienda"): (
        "int",
        "PK de tienda/canal",
        "Sí",
    ),
    ("dim_tienda", "nombre"): (
        "str",
        "Nombre de la tienda",
        "No",
    ),
    ("dim_tienda", "canal"): (
        "str",
        "Canal físico u online",
        "No",
    ),
    ("dim_tienda", "region"): (
        "str",
        "Región de operación",
        "No",
    ),
    ("dim_tienda", "ciudad"): (
        "str",
        "Ciudad",
        "No",
    ),
    ("dim_tienda", "prob_seleccion"): (
        "float",
        "Peso usado para seleccionar tienda durante la generación",
        "No",
    ),

    # dim_promocion
    ("dim_promocion", "id_promocion"): (
        "int",
        "PK de promoción",
        "Sí",
    ),
    ("dim_promocion", "nombre"): (
        "str",
        "Nombre de la campaña",
        "No",
    ),
    ("dim_promocion", "tipo"): (
        "str",
        "Tipo de promoción",
        "No",
    ),
    ("dim_promocion", "descuento_pct"): (
        "float",
        "Porcentaje de descuento",
        "No",
    ),
    ("dim_promocion", "fecha_inicio"): (
        "date",
        "Inicio de vigencia",
        "No",
    ),
    ("dim_promocion", "fecha_fin"): (
        "date",
        "Fin de vigencia",
        "No",
    ),

    # dim_tiempo
    ("dim_tiempo", "id_tiempo"): (
        "int",
        "PK técnica del calendario en formato YYYYMMDD",
        "Sí",
    ),
    ("dim_tiempo", "fecha"): (
        "date",
        "Fecha calendario",
        "Sí",
    ),
    ("dim_tiempo", "dia"): (
        "int",
        "Día del mes",
        "No",
    ),
    ("dim_tiempo", "mes"): (
        "int",
        "Mes",
        "No",
    ),
    ("dim_tiempo", "trimestre"): (
        "int",
        "Trimestre",
        "No",
    ),
    ("dim_tiempo", "anio"): (
        "int",
        "Año",
        "No",
    ),
    ("dim_tiempo", "dia_semana"): (
        "int",
        "Día de semana: lunes=1, domingo=7",
        "No",
    ),
    ("dim_tiempo", "es_fin_semana"): (
        "bool",
        "Indicador de fin de semana",
        "No",
    ),
    ("dim_tiempo", "es_feriado"): (
        "bool",
        "Indicador de feriado",
        "No",
    ),
    ("dim_tiempo", "nombre_feriado"): (
        "str",
        "Nombre del feriado si aplica",
        "No",
    ),
}


# ------------------------------------------------------------------
# Funciones auxiliares
# ------------------------------------------------------------------

def inferir_tipo_columna(serie: pd.Series) -> str:
    """Devuelve el tipo lógico de una columna."""

    if pd.api.types.is_bool_dtype(serie):
        return "bool"

    if pd.api.types.is_integer_dtype(serie):
        return "int"

    if pd.api.types.is_float_dtype(serie):
        return "float"

    if pd.api.types.is_datetime64_any_dtype(serie):
        return "date"

    return "str"


def construir_diccionario(
    tablas: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    """Construye el diccionario usando las tablas reales del ETL."""

    registros = []

    for nombre_tabla, df in tablas.items():
        for campo in df.columns:
            tipo, descripcion, es_clave_fk = DESCRIPCIONES.get(
                (nombre_tabla, campo),
                (
                    inferir_tipo_columna(df[campo]),
                    "Campo generado del datamart",
                    "No",
                ),
            )

            registros.append(
                {
                    "tabla": nombre_tabla,
                    "campo": campo,
                    "tipo": tipo,
                    "descripcion": descripcion,
                    "es_clave_fk": es_clave_fk,
                }
            )

    return pd.DataFrame(registros)


def exportar_diccionario_markdown(
    df_diccionario: pd.DataFrame,
    ruta_salida: Path,
) -> None:
    """Exporta el diccionario de datos a un archivo Markdown."""

    ruta_salida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with ruta_salida.open(
        "w",
        encoding="utf-8",
    ) as archivo:
        archivo.write(
            "# Diccionario de datos — Datamart retail\n\n"
        )

        archivo.write(
            "| Tabla | Campo | Tipo | Descripción | Clave/FK |\n"
        )

        archivo.write(
            "| --- | --- | --- | --- | --- |\n"
        )

        for fila in df_diccionario.itertuples(index=False):
            archivo.write(
                f"| {fila.tabla} "
                f"| {fila.campo} "
                f"| {fila.tipo} "
                f"| {fila.descripcion} "
                f"| {fila.es_clave_fk} |\n"
            )


# ------------------------------------------------------------------
# Función pública usada por el notebook
# ------------------------------------------------------------------

def generar_diccionario_datos(
    tablas: dict[str, pd.DataFrame],
    ruta_salida: Path,
) -> pd.DataFrame:
    """
    Construye y exporta el diccionario de datos del datamart.

    Parameters
    ----------
    tablas:
        Diccionario con las tablas procesadas del ETL.

    ruta_salida:
        Ruta del archivo Markdown que se generará.

    Returns
    -------
    pd.DataFrame
        Diccionario de datos generado.
    """

    df_diccionario = construir_diccionario(
        tablas=tablas,
    )

    exportar_diccionario_markdown(
        df_diccionario=df_diccionario,
        ruta_salida=ruta_salida,
    )

    return df_diccionario