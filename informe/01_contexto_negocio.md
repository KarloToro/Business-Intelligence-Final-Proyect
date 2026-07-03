# 01. Contexto de negocio

## Fuentes revisadas

Este documento se basa en `README.md`, `Resumen Datos Sinteticos.md`, los scripts de generación y validación ubicados en `scripts/`, el notebook disponible `notebooks/00_generacion_datos.ipynb` y los archivos finales de `data/processed/`.

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

Los datos no corresponden a personas ni empresas reales. Fueron generados con fines académicos para construir una solución integral de Inteligencia de Negocios.

## Problemática del negocio

La empresa necesita transformar datos transaccionales en información útil para la toma de decisiones gerenciales. Sin una solución BI consolidada, la gerencia tendría dificultades para:

- monitorear ventas, margen y rentabilidad;
- identificar productos, segmentos y canales con mayor contribución;
- evaluar el comportamiento de clientes y promociones;
- detectar oportunidades de fidelización, segmentación y venta cruzada;
- proyectar demanda o ventas futuras;
- sustentar decisiones comerciales con indicadores consistentes.

La problemática central no es la falta de datos, sino la necesidad de organizarlos, validarlos, modelarlos e interpretarlos para generar conocimiento accionable.

## Necesidad de la solución BI

La solución BI es necesaria para integrar los datos sintéticos en un modelo analítico, construir indicadores de negocio y facilitar el análisis de ventas, clientes, productos, promociones y demanda.

Según el README, el proyecto debe cubrir generación de datos, datamart, visualización, clasificación, segmentación, asociación y regresión. Actualmente, el repositorio contiene datos procesados, scripts de generación y validación, y resultados exploratorios básicos. Las etapas posteriores deben completarse con notebooks y/o reportes específicos.

## Objetivo general

Diseñar una solución de Inteligencia de Negocios para una empresa retail ficticia, capaz de transformar datos transaccionales sintéticos en información accionable que apoye decisiones comerciales, de fidelización, promoción, segmentación y planificación de demanda.

## Objetivos específicos

- Generar y documentar datos sintéticos consistentes para representar la operación de una empresa retail.
- Organizar los datos en un modelo dimensional tipo estrella, con una tabla de hechos de ventas y dimensiones de cliente, producto, tienda, promoción y tiempo.
- Definir KPI que permitan evaluar ventas, margen, ticket promedio, productos, clientes, promociones y canales.
- Construir visualizaciones ejecutivas para comunicar el desempeño del negocio.
- Aplicar modelos analíticos de clasificación, segmentación, asociación y regresión según las etapas del proyecto.
- Interpretar los resultados desde una perspectiva empresarial, evitando conclusiones no sustentadas.
- Elaborar recomendaciones accionables basadas en evidencia disponible.
- Incluir una reflexión ética sobre datos sintéticos, privacidad, sesgos y uso de inteligencia artificial.

## Preguntas de negocio

- ¿Cuál es el nivel total de ventas, margen y tickets durante el periodo 2024-2025?
- ¿Qué segmentos de clientes generan mayores ingresos y margen?
- ¿Qué productos y categorías concentran la mayor venta y rentabilidad?
- ¿Qué diferencia existe entre productos estrella y productos no estrella?
- ¿Qué canales o tiendas tienen mayor contribución comercial?
- ¿Qué promociones se aplican con mayor frecuencia y qué impacto tienen en ventas y margen?
- ¿Qué clientes presentan mayor valor comercial?
- ¿Qué patrones de compra permiten proponer ventas cruzadas?
- ¿Qué segmentos de clientes requieren estrategias diferenciadas?
- ¿Qué variables podrían ayudar a predecir abandono, propensión de compra o demanda futura?

## Estado de cobertura de esta parte

| Elemento | Estado | Evidencia |
| --- | --- | --- |
| Descripción general del proyecto | Cubierto parcialmente | `README.md` |
| Descripción de datos sintéticos | Cubierto | `Resumen Datos Sinteticos.md` |
| Empresa ficticia | Cubierto parcialmente | Inferida de los datos retail y del README; falta nombre formal de la empresa |
| Problemática de negocio | Requiere redacción | Este documento propone una versión alineada al proyecto |
| Objetivos | Requiere redacción | Este documento propone objetivo general y específicos |
| Preguntas de negocio | Requiere redacción | Este documento propone preguntas vinculadas a las etapas del proyecto |
| Resultados analíticos avanzados | Pendiente | No existen notebooks implementados para 03 a 06 |
