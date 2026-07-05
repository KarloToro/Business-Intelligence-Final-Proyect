# 01. Contexto de negocio

## Fuentes revisadas

Este documento se basa en `README.md`, `Resumen Datos Sinteticos.md`, los scripts de generación y validación ubicados en `scripts/`, los notebooks disponibles en `notebooks/`, los archivos finales de `data/processed/` y los resultados exportados por los modelos analíticos.

## Descripción de la empresa ficticia

El proyecto representa una empresa retail ficticia que opera con tiendas físicas y canales online en distintas regiones del Perú. La empresa comercializa productos de consumo masivo y categorías complementarias como abarrotes, bebidas, lácteos, frutas y verduras, carnes y aves, limpieza, cuidado personal, hogar, bebés, mascotas, congelados, snacks y dulces.

De acuerdo con los datos procesados, la operación simulada cuenta con:

- 5,000 clientes sintéticos.
- 506 productos.
- 15 tiendas o canales de venta.
- 29 promociones.
- 34,755 tickets de venta.
- 55,858 líneas de venta.
- Periodo de análisis: 2024-01-01 a 2025-12-31.

Adicionalmente, después de la actualización del repositorio existen resultados analíticos exportados para abandono de clientes, segmentación RFM, reglas de asociación y pronóstico de ventas.

## Problemática del negocio

La empresa necesita transformar datos transaccionales en información útil para la toma de decisiones gerenciales. Sin una solución BI consolidada, la gerencia tendría dificultades para:

- monitorear ventas, margen y rentabilidad;
- identificar productos, segmentos y canales con mayor contribución;
- evaluar el comportamiento de clientes y promociones;
- detectar oportunidades de fidelización, segmentación y venta cruzada;
- anticipar riesgos de abandono;
- proyectar ventas futuras;
- sustentar decisiones comerciales con indicadores consistentes.

La problemática central no es la falta de datos, sino la necesidad de organizarlos, validarlos, modelarlos e interpretarlos para generar conocimiento accionable.

## Necesidad de la solución BI

La solución BI es necesaria para integrar los datos sintéticos en un modelo analítico, construir indicadores de negocio y facilitar el análisis de ventas, clientes, productos, promociones, canastas de compra y demanda futura.

Según el README, el proyecto cubre generación de datos, datamart, visualización, clasificación, segmentación, asociación y regresión. Actualmente ya existen notebooks para generación de datos, clasificación, segmentación, asociación y regresión. No se observan todavía notebooks de datamart (`01_datamart_etl.ipynb`) ni visualización (`02_visualizacion.ipynb`) en la estructura actual.

## Objetivo general

Diseñar una solución de Inteligencia de Negocios para una empresa retail ficticia, capaz de transformar datos transaccionales sintéticos en información accionable que apoye decisiones comerciales, de fidelización, promoción, segmentación, venta cruzada y planificación de demanda.

## Objetivos específicos

- Generar y documentar datos sintéticos consistentes para representar la operación de una empresa retail.
- Organizar los datos en un modelo dimensional tipo estrella, con una tabla de hechos de ventas y dimensiones de cliente, producto, tienda, promoción y tiempo.
- Definir KPI que permitan evaluar ventas, margen, ticket promedio, productos, clientes, promociones y canales.
- Construir visualizaciones ejecutivas para comunicar el desempeño del negocio.
- Aplicar modelos analíticos de clasificación, segmentación, asociación y regresión según las etapas del proyecto.
- Interpretar los resultados desde una perspectiva empresarial, evitando conclusiones no sustentadas.
- Elaborar recomendaciones accionables basadas en evidencia disponible.
- Incluir una reflexión ética sobre datos sintéticos, privacidad, sesgos, uso de IA y limitaciones de los modelos.

## Preguntas de negocio

- ¿Cuál es el nivel total de ventas, margen y tickets durante el periodo 2024-2025?
- ¿Qué segmentos de clientes generan mayores ingresos y margen?
- ¿Qué productos y categorías concentran la mayor venta y rentabilidad?
- ¿Qué diferencia existe entre productos estrella y productos no estrella?
- ¿Qué canales o tiendas tienen mayor contribución comercial?
- ¿Qué promociones se aplican con mayor frecuencia y qué impacto tienen en ventas y margen?
- ¿Qué clientes presentan mayor probabilidad de abandono?
- ¿Qué grupos de clientes se identifican mediante variables RFM?
- ¿Qué categorías aparecen asociadas en una misma canasta de compra?
- ¿Qué nivel de error presenta el pronóstico de ventas y cómo puede usarse para planificación?

## Estado de cobertura de esta parte

| Elemento | Estado | Evidencia |
| --- | --- | --- |
| Descripción general del proyecto | Cubierto | `README.md` |
| Descripción de datos sintéticos | Cubierto | `Resumen Datos Sinteticos.md` |
| Empresa ficticia | Cubierto parcialmente | Inferida de los datos retail y del README; falta nombre formal definitivo si el equipo desea asignarlo |
| Problemática de negocio | Cubierto | Este documento |
| Objetivos | Cubierto | Este documento |
| Preguntas de negocio | Cubierto | Este documento |
| Clasificación | Cubierto parcialmente | `notebooks/03_clasificacion_ipynb.ipynb` y `data/processed/predicciones_abandono.csv` |
| Segmentación | Cubierto parcialmente | `notebooks/04_segmentacion.ipynb` y `data/processed/segmentos_clientes.csv` |
| Asociación | Cubierto parcialmente | `notebooks/05_asociacion.ipynb` y `data/processed/reglas_asociacion.csv` |
| Regresión | Cubierto parcialmente | `notebooks/06_regresion.ipynb` y `data/processed/pronostico_ventas.csv` |
| Visualización y datamart ETL | Pendiente o no visible | No se observan `01_datamart_etl.ipynb`, `02_visualizacion.ipynb` ni carpeta `powerbi/` en el repositorio actual |
