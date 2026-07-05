# 02. KPI e indicadores

## Fuentes revisadas

Los KPI se definieron a partir del objetivo del proyecto descrito en `README.md`, la estructura del datamart descrita en `Resumen Datos Sinteticos.md`, los campos disponibles en `data/processed/`, los resultados del script `scripts/explorar_dataset.py` y los notebooks analíticos disponibles.

## KPI principales de negocio

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
| Efecto de promociones | Comparación de ventas, descuento y margen por `id_promocion` o `tipo` | Evaluar impacto comercial de campañas | Visualización y recomendaciones |
| Ventas por periodo | Suma de `importe_venta` por fecha, mes, trimestre o año | Identificar tendencias y estacionalidad | Regresión y pronóstico |

## Valores generales ya calculados

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

## Indicadores de clasificación

| Indicador | Resultado | Utilidad empresarial |
| --- | ---: | --- |
| Clientes modelados | 5,000 | Base total para estimar riesgo de abandono |
| Clientes definidos como abandono en el modelado | 24.18% | Tamaño del grupo objetivo según la regla de 180 días sin compras |
| Regresión Logística ROC-AUC | 0.828 | Mejor capacidad de discriminación entre los modelos comparados |
| Regresión Logística recall clase abandono | 0.77 | Capacidad de detectar clientes en abandono |
| Random Forest accuracy | 0.79 | Mayor exactitud general reportada |
| Random Forest ROC-AUC | 0.806 | Modelo usado para exportar predicciones a Power BI |
| Predicciones exportadas | 5,000 | Archivo `predicciones_abandono.csv` |
| Riesgo alto exportado | 810 clientes | Grupo prioritario para acciones de retención |
| Riesgo medio exportado | 505 clientes | Grupo para seguimiento preventivo |
| Riesgo bajo exportado | 3,000 clientes | Grupo de menor prioridad inmediata |
| Riesgo sin etiqueta | 685 clientes | Observación técnica: probabilidades 0.0 quedaron fuera de las categorías del CSV |

## Indicadores de segmentación

| Segmento exportado | Clientes |
| --- | ---: |
| Leales / Frecuentes | 2,206 |
| Campeones / VIP | 1,537 |
| Nuevos / Esporádicos | 690 |
| En Riesgo / Inactivos | 567 |

El notebook reporta un perfil RFM por cluster con recencia, frecuencia, monto y ticket promedio. Antes de cerrar conclusiones comerciales, se recomienda revisar la correspondencia entre los nombres de segmentos y los promedios RFM, porque algunos nombres exportados no parecen alinearse con el perfil numérico mostrado en el notebook.

## Indicadores de asociación

| Indicador | Resultado |
| --- | ---: |
| Canastas analizadas | 34,755 |
| Categorías evaluadas | 12 |
| Reglas exportadas | 26 |
| Regla con mayor lift | Bebidas + Lácteos -> Snacks y Dulces |
| Lift máximo | 4.252 |
| Confianza de la regla anterior | 0.454 |
| Soporte de la regla anterior | 0.012 |

## Indicadores de regresión

| Indicador | Resultado |
| --- | ---: |
| Días de entrenamiento | 579 |
| Días de prueba | 145 |
| Modelo seleccionado | Gradient Boosting |
| MAE | S/ 261.19 |
| RMSE | S/ 335.67 |
| MAPE | 13.45% |
| R2 | 0.327 |
| Periodo exportado | 2025-08-09 a 2025-12-31 |

## Relación con cada parte del proyecto

| Parte del proyecto | KPI asociados | Estado actual |
| --- | --- | --- |
| Generación de datos | Clientes, productos, tiendas, promociones, tickets, líneas de venta | Cubierto con datos y scripts |
| Datamart y ETL | Integridad de claves, relaciones, tablas de hechos y dimensiones | Cubierto parcialmente por `Resumen Datos Sinteticos.md` y `scripts/validar_dataset.py` |
| Visualización | Ventas, margen, ticket promedio, productos, segmentos, canales | Pendiente de dashboard o archivo Power BI visible |
| Clasificación | Abandono, probabilidad, riesgo, accuracy, recall, ROC-AUC | Cubierto parcialmente |
| Segmentación | RFM, clusters, perfiles, tamaño de segmentos | Cubierto parcialmente |
| Asociación | Soporte, confianza, lift | Cubierto parcialmente |
| Regresión | MAE, RMSE, MAPE, R2 | Cubierto parcialmente |
