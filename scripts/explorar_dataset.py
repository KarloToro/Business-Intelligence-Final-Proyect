from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "processed"


def leer(nombre: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / nombre, sep=";", encoding="utf-8")


def main():
    clientes = leer("dim_cliente.csv")
    productos = leer("dim_producto.csv")
    ventas = leer("fact_ventas.csv")

    df = (
        ventas
        .merge(clientes[["id_cliente", "nombre", "segmento_programa", "region"]], on="id_cliente", how="left")
        .merge(productos[["id_producto", "nombre", "categoria", "subcategoria", "producto_estrella"]], 
               on="id_producto", how="left", suffixes=("", "_producto"))
    )

    print("\n==============================")
    print("RESUMEN GENERAL")
    print("==============================")
    print(f"Clientes únicos: {df['id_cliente'].nunique():,}")
    print(f"Tickets de venta: {df['id_venta'].nunique():,}")
    print(f"Líneas de venta: {len(df):,}")
    print(f"Ingresos totales: S/ {df['importe_venta'].sum():,.2f}")
    print(f"Ganancia total: S/ {df['margen'].sum():,.2f}")
    print(f"Líneas promedio por venta: {len(df) / df['id_venta'].nunique():.2f}")

    print("\n==============================")
    print("TOP 15 CLIENTES QUE MÁS COMPRAN")
    print("==============================")
    top_clientes = (
        df.groupby(["id_cliente", "nombre", "segmento_programa"])
        .agg(
            tickets=("id_venta", "nunique"),
            lineas=("id_venta", "count"),
            gasto_total=("importe_venta", "sum"),
            ganancia_generada=("margen", "sum"),
        )
        .sort_values("gasto_total", ascending=False)
        .head(15)
    )
    print(top_clientes.to_string())

    print("\n==============================")
    print("TOP 15 PRODUCTOS MÁS VENDIDOS")
    print("==============================")
    top_productos = (
        df.groupby(["id_producto", "nombre_producto", "categoria", "subcategoria", "producto_estrella"])
        .agg(
            unidades_vendidas=("cantidad", "sum"),
            lineas=("id_venta", "count"),
            ingresos=("importe_venta", "sum"),
            ganancia=("margen", "sum"),
        )
        .sort_values("unidades_vendidas", ascending=False)
        .head(15)
    )
    print(top_productos.to_string())

    print("\n==============================")
    print("INGRESOS Y GANANCIA POR SEGMENTO")
    print("==============================")
    ingresos_segmento = (
        df.groupby("segmento_programa")
        .agg(
            clientes=("id_cliente", "nunique"),
            tickets=("id_venta", "nunique"),
            lineas=("id_venta", "count"),
            ingresos=("importe_venta", "sum"),
            ganancia=("margen", "sum"),
            ticket_promedio=("importe_venta", "mean"),
        )
        .sort_values("ingresos", ascending=False)
    )
    print(ingresos_segmento.to_string())

    print("\n==============================")
    print("GANANCIA DE PRODUCTOS TOP")
    print("==============================")
    ganancia_top = (
        df.groupby(["id_producto", "nombre_producto", "categoria", "subcategoria"])
        .agg(
            unidades_vendidas=("cantidad", "sum"),
            ingresos=("importe_venta", "sum"),
            costo_total=("costo_total", "sum"),
            ganancia=("margen", "sum"),
        )
        .assign(
            margen_pct=lambda x: (x["ganancia"] / x["ingresos"] * 100).round(2)
        )
        .sort_values("ganancia", ascending=False)
        .head(15)
    )
    print(ganancia_top.to_string())

    print("\n==============================")
    print("PRODUCTOS ESTRELLA VS NO ESTRELLA")
    print("==============================")
    estrellas = (
        df.groupby("producto_estrella")
        .agg(
            productos=("id_producto", "nunique"),
            unidades=("cantidad", "sum"),
            ingresos=("importe_venta", "sum"),
            ganancia=("margen", "sum"),
        )
        .sort_values("ingresos", ascending=False)
    )
    print(estrellas.to_string())


if __name__ == "__main__":
    main()