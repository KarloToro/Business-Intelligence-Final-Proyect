from __future__ import annotations

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

FECHA_INICIO = "2024-01-01"
FECHA_FIN = "2025-12-31"

FERIADOS_PERU = {
    # 2024
    "2024-01-01": "Año Nuevo",
    "2024-03-28": "Jueves Santo",
    "2024-03-29": "Viernes Santo",
    "2024-05-01": "Día del Trabajo",
    "2024-06-07": "Batalla de Arica y Día de la Bandera",
    "2024-06-29": "San Pedro y San Pablo",
    "2024-07-23": "Día de la Fuerza Aérea del Perú",
    "2024-07-28": "Fiestas Patrias - Independencia del Perú",
    "2024-07-29": "Fiestas Patrias",
    "2024-08-06": "Batalla de Junín",
    "2024-08-30": "Santa Rosa de Lima",
    "2024-10-08": "Combate de Angamos",
    "2024-11-01": "Día de Todos los Santos",
    "2024-12-08": "Inmaculada Concepción",
    "2024-12-09": "Batalla de Ayacucho",
    "2024-12-25": "Navidad",

    # 2025
    "2025-01-01": "Año Nuevo",
    "2025-04-17": "Jueves Santo",
    "2025-04-18": "Viernes Santo",
    "2025-05-01": "Día del Trabajo",
    "2025-06-07": "Batalla de Arica y Día de la Bandera",
    "2025-06-29": "San Pedro y San Pablo",
    "2025-07-23": "Día de la Fuerza Aérea del Perú",
    "2025-07-28": "Fiestas Patrias - Independencia del Perú",
    "2025-07-29": "Fiestas Patrias",
    "2025-08-06": "Batalla de Junín",
    "2025-08-30": "Santa Rosa de Lima",
    "2025-10-08": "Combate de Angamos",
    "2025-11-01": "Día de Todos los Santos",
    "2025-12-08": "Inmaculada Concepción",
    "2025-12-09": "Batalla de Ayacucho",
    "2025-12-25": "Navidad",
}


def generar_dim_tiempo() -> pd.DataFrame:
    fechas = pd.date_range(start=FECHA_INICIO, end=FECHA_FIN, freq="D")

    df = pd.DataFrame({"fecha": fechas})
    df["id_tiempo"] = df["fecha"].dt.strftime("%Y%m%d").astype(int)
    df["dia"] = df["fecha"].dt.day
    df["mes"] = df["fecha"].dt.month
    df["trimestre"] = df["fecha"].dt.quarter
    df["anio"] = df["fecha"].dt.year
    df["dia_semana"] = df["fecha"].dt.weekday + 1  # lunes=1, domingo=7
    df["es_fin_semana"] = df["dia_semana"].isin([6, 7])
    df["fecha_str"] = df["fecha"].dt.strftime("%Y-%m-%d") # clave auxiliar para cruzar con FERIADOS_PERU
    df["nombre_feriado"] = df["fecha_str"].map(FERIADOS_PERU).fillna("")
    df["es_feriado"] = df["nombre_feriado"].ne("")

    df["fecha"] = df["fecha"].dt.strftime("%Y-%m-%d")

    columnas = [
        "id_tiempo",
        "fecha",
        "dia",
        "mes",
        "trimestre",
        "anio",
        "dia_semana",
        "es_fin_semana",
        "es_feriado",
        "nombre_feriado",
    ]

    return df[columnas]


def guardar_dim_tiempo(df: pd.DataFrame) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ruta = DATA_DIR / "dim_tiempo.csv"
    df.to_csv(ruta, sep=";", index=False, encoding="utf-8")
    return ruta


if __name__ == "__main__":
    dim_tiempo = generar_dim_tiempo()
    ruta_salida = guardar_dim_tiempo(dim_tiempo)

    print("Dimensión tiempo generada.")
    print(f"Filas: {len(dim_tiempo):,}")
    print(f"Fecha mínima: {dim_tiempo['fecha'].min()}")
    print(f"Fecha máxima: {dim_tiempo['fecha'].max()}")
    print(f"Feriados: {dim_tiempo['es_feriado'].sum():,}")
    print(f"Archivo creado: {ruta_salida}")