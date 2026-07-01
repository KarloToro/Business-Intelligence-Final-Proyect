from __future__ import annotations

import random
from pathlib import Path

SEED = 20260701
RNG = random.Random(SEED)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
TABLAS_MAESTRAS_DIR = DATA_DIR / "tablas_maestras"
OUTPUT_DIR = DATA_DIR / "processed"

TOTAL_CLIENTES = 5_000

FECHA_INICIO_OPERACION = "2024-01-01"
FECHA_FIN_OPERACION = "2025-12-31"

rangos_edades = {
    "18_29": {
        "probabilidad": 0.28,
        "fecha_inicio": "1996-01-02",
        "fecha_fin": "2008-01-01",
    },
    "30_49": {
        "probabilidad": 0.40,
        "fecha_inicio": "1976-01-02",
        "fecha_fin": "1996-01-01",
    },
    "50_80": {
        "probabilidad": 0.30,
        "fecha_inicio": "1945-01-02",
        "fecha_fin": "1976-01-01",
    },
    "80_mas": {
        "probabilidad": 0.02,
        "fecha_inicio": "1925-01-02",
        "fecha_fin": "1945-01-01",
    },
}

segmento_programa = {
    "No afiliado": {"probabilidad": 0.35, "probabilidad_recompra": 0.12},
    "Bronce": {"probabilidad": 0.40, "probabilidad_recompra": 0.28},
    "Plata": {"probabilidad": 0.18, "probabilidad_recompra": 0.47},
    "Oro": {"probabilidad": 0.07, "probabilidad_recompra": 0.72},
}

# Alias derivados para mantener compatibilidad 
distribucion_segmento_programa = {
    segmento: valores["probabilidad"]
    for segmento, valores in segmento_programa.items()
}

probabilidad_recompra = {
    segmento: valores["probabilidad_recompra"]
    for segmento, valores in segmento_programa.items()
}
