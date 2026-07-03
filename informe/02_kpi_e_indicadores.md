# 02. KPI e indicadores

## Fuentes revisadas

Los KPI se definieron a partir del objetivo del proyecto descrito en `README.md`, la estructura del datamart descrita en `Resumen Datos Sinteticos.md`, los campos disponibles en `data/processed/` y los resultados del script `scripts/explorar_dataset.py`.

## KPI principales

| KPI | Fórmula o forma de cálculo | Utilidad empresarial | Relación con el proyecto |
| --- | --- | --- | --- |
| Ventas totales | Suma de `fact_ventas.importe_venta` | Medir el ingreso generado por la operación | Visualización, resumen ejecutivo, análisis comercial |
| Margen total | Suma de `fact_ventas.margen` | Evaluar la ganancia bruta generada | Visualización, rentabilidad, recomendaciones |
| Costo total | Suma de `fact_ventas.costo_total` | Controlar el costo asociado a las ventas | Datamart, rentabilidad |
| Margen porcentual | `margen total / ventas totales` | Comparar rentabilidad entre productos, segmentos o canales | Dashboard, análisis por producto y segmento |
| Tickets de venta | Conteo distinto de `fact_ventas.id_venta` | Medir volumen de transacciones | Visualización y comportamiento de compra |
| Líneas de venta | Conteo de filas de `fact_ventas` | Medir detalle operativo y composición de tickets | Asociación y canasta de mercado |
| Unidades vendidas | Suma de `fact_ventas.cantidad` | Identificar demanda por producto o categoría | Visualización, asociación, regresión |
| Ticket promedio | `ventas totales / tickets de venta` | Evaluar valor medio por compra | Dashboard ejecutivo, campañas comerciales |
| Líneas promedio por ticket | `líneas de venta / tickets de venta` | Analizar profundidad de compra y potencial de canasta | Asociación y venta cruzada |
| Clientes activos | Conteo distinto de `fact_ventas.id_cliente` | Medir base real de clientes compradores | Segmentación, clasificación |
| Productos vendidos | Conteo distinto de `fact_ventas.id_producto` | Evaluar cobertura del catálogo vendido | Análisis de productos |
| Ventas por segmento | Suma de `importe_venta` agrupada por `dim_cliente.segmento_programa` | Identificar segmentos con mayor contribución | Segmentación y fidelización |
| Margen por segmento | Suma de `margen` agrupada por `segmento_programa` | Medir rentabilidad por tipo de cliente | Segmentación y recomendaciones |
| Ventas por producto/categoría | Suma de `importe_venta` agrupada por producto, subcategoría o categoría | Identificar productos relevantes | Visualización, asociación |
| Unidades por producto | Suma de `cantidad` agrupada por producto | Medir demanda de productos | Asociación, regresión |
| Participación de productos estrella | Ventas o unidades de productos con `producto_estrella=True` sobre total | Evaluar dependencia comercial de productos clave | Generación de datos, visualización |
| Efecto de promociones | Comparación de ventas, descuento y margen por `id_promocion` o `tipo` | Evaluar impacto comercial de campañas | Visualización y recomendaciones |
| Ventas por tienda/canal | Suma de `importe_venta` agrupada por tienda o canal | Comparar desempeño físico y online | Dashboard ejecutivo |
| Ventas por periodo | Suma de `importe_venta` por fecha, mes, trimestre o año | Identificar tendencias y estacionalidad | Regresión y pronóstico |

## Valores ya calculados en el repositorio

El script `scripts/explorar_dataset.py` reporta los siguientes resultados generales:

| Indicador | Valor |
| --- | ---: |
| Clientes únicos | 5,000 |
| Tickets de venta | 34,755 |
| Líneas de venta | 55,858 |
| Ingresos totales | S/ 1,428,828.48 |
| Ganancia total | S/ 392,905.08 |
| Líneas promedio por venta | 1.61 |

También se identificó que los productos estrella generan S/ 762,080.07 de ingresos y S/ 216,172.97 de ganancia, mientras que los productos no estrella generan S/ 666,748.41 de ingresos y S/ 176,732.11 de ganancia.

## Relación con cada parte del proyecto

| Parte del proyecto | KPI asociados | Estado actual |
| --- | --- | --- |
| Generación de datos | Clientes, productos, tiendas, promociones, tickets, líneas de venta | Cubierto con datos y scripts |
| Datamart y ETL | Integridad de claves, relaciones, tablas de hechos y dimensiones | Cubierto por `Resumen Datos Sinteticos.md` y `scripts/validar_dataset.py` |
| Visualización | Ventas, margen, ticket promedio, productos, segmentos, canales | Pendiente de dashboard o notebook específico |
| Clasificación | Churn, propensión o riesgo de abandono | Pendiente de `03_clasificacion.ipynb` |
| Segmentación | RFM, clusters, valor de cliente | Pendiente de `04_segmentacion.ipynb` |
| Asociación | Reglas de canasta, soporte, confianza, lift | Pendiente de `05_asociacion.ipynb` |
| Regresión | Pronóstico de ventas o demanda, error del modelo | Pendiente de `06_regresion.ipynb` |

## Indicadores pendientes de definir cuando existan modelos

- Accuracy, precision, recall, F1-score y matriz de confusión para clasificación.
- Variables RFM y tamaño de clusters para segmentación.
- Soporte, confianza y lift para reglas de asociación.
- MAE, RMSE, MAPE o R2 para regresión, según el modelo implementado.
