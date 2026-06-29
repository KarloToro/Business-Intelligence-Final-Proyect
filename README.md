# 📊 Proyecto BI — Empresa Ficticia con Datos Sintéticos

Solución integral de **Business Intelligence** desarrollada para una empresa ficticia, usando **Python**, **Power BI** y técnicas de minería de datos. El proyecto cubre desde la generación reproducible de datos sintéticos hasta la construcción de un datamart, tableros ejecutivos y modelos analíticos para apoyar la toma de decisiones gerenciales.

## 🚀 Objetivo del proyecto

Diseñar una solución de BI capaz de transformar datos transaccionales sintéticos en información accionable para la gerencia, respondiendo preguntas sobre ventas, clientes, productos, promociones, abandono, segmentación, canasta de mercado y pronóstico de demanda.

## 🧩 Componentes principales

| Parte | Enfoque             | Resultado esperado                                                  |
| ----- | ------------------- | ------------------------------------------------------------------- |
| 0     | Generación de datos | Datos sintéticos reproducibles con problemas de calidad controlados |
| 1     | Datamart analítico  | Modelo dimensional tipo estrella y proceso ETL                      |
| 2     | Visualización       | Dashboard ejecutivo en Power BI e insights de negocio               |
| 3     | Clasificación       | Predicción de abandono o propensión de clientes                     |
| 4     | Segmentación        | Clustering de clientes mediante RFM + K-Means                       |
| 5     | Asociación          | Reglas de canasta de mercado para promociones cruzadas              |
| 6     | Regresión           | Pronóstico de ventas o demanda                                      |

## 🛠️ Stack tecnológico

* **Python 3.10+**
* **Jupyter Notebooks**
* **pandas / numpy**
* **matplotlib / seaborn / plotly**
* **scikit-learn**
* **mlxtend**
* **faker**
* **Power BI Desktop**
* **Git / GitHub**

## 📁 Estructura del repositorio

```text
proyecto-bi/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 00_generacion_datos.ipynb
│   ├── 01_datamart_etl.ipynb
│   ├── 02_visualizacion.ipynb
│   ├── 03_clasificacion.ipynb
│   ├── 04_segmentacion.ipynb
│   ├── 05_asociacion.ipynb
│   └── 06_regresion.ipynb
├── powerbi/
├── prompts/
├── informe/
└── docs/
```

## 🔁 Reproducibilidad

El proyecto puede reproducirse ejecutando los notebooks en orden:

```bash
pip install -r requirements.txt
```

Luego abrir Jupyter y ejecutar:

```text
00_generacion_datos.ipynb
01_datamart_etl.ipynb
02_visualizacion.ipynb
03_clasificacion.ipynb
04_segmentacion.ipynb
05_asociacion.ipynb
06_regresion.ipynb
```

Los datos son completamente sintéticos y se generan con una semilla fija para asegurar resultados consistentes.

## 📈 Resultados esperados

* Datamart analítico con esquema estrella.
* Tablero ejecutivo en Power BI.
* Métricas DAX para ventas, margen, ticket promedio y crecimiento.
* Modelo de clasificación para riesgo de abandono.
* Segmentos de clientes con estrategias diferenciadas.
* Reglas de asociación para promociones cruzadas.
* Pronóstico de ventas o demanda.
* Informe consolidado con hallazgos, recomendaciones y reflexión ética.

## 🔐 Nota sobre los datos

Este repositorio no contiene datos reales de personas ni empresas. Todos los datos utilizados son sintéticos y fueron generados exclusivamente con fines académicos.
