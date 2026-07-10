import random

SEED = 20260701

RNG = random.Random(SEED)

rangos_edades = {
    "18_29": {
        "probabilidad": 0.28,
        "fecha_inicio": "1996-01-02",
        "fecha_fin": "2008-01-01"
    },
    "30_49": {
        "probabilidad": 0.40,
        "fecha_inicio": "1976-01-02",
        "fecha_fin": "1996-01-01"
    },
    "50_80": {
        "probabilidad": 0.30,
        "fecha_inicio": "1945-01-02",
        "fecha_fin": "1976-01-01"
    },
    "80_mas": {
        "probabilidad": 0.02,
        "fecha_inicio": "1925-01-02",
        "fecha_fin": "1945-01-01"
    }
}

distribucion_segmento_programa = {
    "No afiliado": 0.35,
    "Bronce": 0.40,
    "Plata": 0.18,
    "Oro": 0.07,
}

probabilidad_recompra = {
    "No afiliado": 0.12,
    "Bronce": 0.28,
    "Plata": 0.47,
    "Oro": 0.72,
}