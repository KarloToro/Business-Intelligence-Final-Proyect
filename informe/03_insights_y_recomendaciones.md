# 03. Insights y recomendaciones

## Criterio de uso

Este documento incluye hallazgos cuando existe evidencia en el repositorio. Cuando una etapa requiere revisión adicional, se indica como observación o pendiente para evitar conclusiones no sustentadas.

## Insights con evidencia disponible

| Hallazgo | Evidencia | Interpretación empresarial | Recomendación |
| --- | --- | --- | --- |
| La operación sintética cubre una base completa de clientes compradores. | `scripts/validar_dataset.py` reporta 5,000 clientes y 5,000 clientes con venta. | El dataset permite analizar comportamiento de compra sobre toda la base de clientes generada. | Usar esta base como referencia para segmentación y clasificación, aclarando que los datos son sintéticos. |
| El periodo de análisis está completo para dos años. | La validación reporta ventas desde 2024-01-01 hasta 2025-12-31 y 731 días calendario. | Permite evaluar tendencias mensuales, estacionalidad y comparaciones anuales. | Construir visualizaciones por mes, trimestre y año antes de presentar conclusiones ejecutivas. |
| Los ingresos totales y margen ya pueden reportarse como KPI generales. | `scripts/explorar_dataset.py` reporta ingresos por S/ 1,428,828.48 y ganancia por S/ 392,905.08. | Existe una línea base para el resumen ejecutivo y el dashboard gerencial. | Incluir ventas, margen, ticket promedio y líneas promedio por ticket como indicadores de primera vista. |
| El segmento Bronce concentra el mayor ingreso total. | El script de exploración reporta para Bronce S/ 560,380.71 en ingresos y S/ 154,586.91 en ganancia. | Este segmento tiene alta relevancia por tamaño y contribución total, aunque no necesariamente por valor individual. | Analizar ticket promedio, frecuencia y migración potencial de Bronce hacia Plata u Oro. |
| Los productos estrella concentran mayor ingreso que los no estrella. | Productos estrella: S/ 762,080.07 en ingresos y S/ 216,172.97 en ganancia. No estrella: S/ 666,748.41 en ingresos y S/ 176,732.11 en ganancia. | La empresa depende de un grupo reducido de productos clave para una parte importante del desempeño comercial. | Priorizar disponibilidad, exhibición y seguimiento de margen en productos estrella, sin descuidar oportunidades de cola larga. |
| La clasificación identifica una base prioritaria de retención. | `predicciones_abandono.csv` contiene 810 clientes en riesgo alto y 505 en riesgo medio. | La empresa puede focalizar campañas de retención en grupos con mayor probabilidad estimada de abandono. | Diseñar acciones diferenciadas para riesgo alto y medio, y corregir las 685 filas sin etiqueta de riesgo antes de usar el CSV en Power BI. |
| Regresión Logística detecta mejor abandono que Random Forest según recall y ROC-AUC. | En `03_clasificacion_ipynb.ipynb`, Regresión Logística alcanza ROC-AUC 0.828 y recall 0.77 para abandono; Random Forest alcanza ROC-AUC 0.806 y recall 0.41. | Si el objetivo principal es detectar abandono, no basta mirar accuracy general. | Revisar la elección del modelo final exportado, porque el notebook exporta Random Forest pese a que Regresión Logística muestra mejor desempeño para identificar abandono. |
| La segmentación exporta cuatro grupos de clientes. | `segmentos_clientes.csv` contiene 2,206 Leales/Frecuentes, 1,537 Campeones/VIP, 690 Nuevos/Esporádicos y 567 En Riesgo/Inactivos. | La empresa puede plantear estrategias diferenciadas de fidelización, crecimiento y recuperación. | Validar la correspondencia entre nombres comerciales y perfiles RFM antes de presentar conclusiones, porque algunos nombres no parecen coincidir con los promedios del notebook. |
| Existen reglas de asociación útiles para venta cruzada. | `reglas_asociacion.csv` contiene 26 reglas; la mayor tiene lift 4.252 para Bebidas + Lácteos -> Snacks y Dulces. | Algunas categorías aparecen juntas con una frecuencia relativa superior a la esperada por azar. | Usar estas reglas para combos, recomendaciones en tienda y promociones cruzadas, priorizando reglas con lift alto y confianza comercialmente útil. |
| El modelo de regresión permite pronosticar ventas diarias con error moderado. | `06_regresion.ipynb` reporta Gradient Boosting con MAE S/ 261.19, RMSE S/ 335.67, MAPE 13.45% y R2 0.327. | El pronóstico puede apoyar planificación operativa, aunque su capacidad explicativa todavía es limitada. | Usarlo como primera referencia para planificación, y mejorar variables antes de tomar decisiones críticas de inventario o presupuesto. |

## Pendientes para cierre del informe

| Tema | Pendiente | Motivo |
| --- | --- | --- |
| Datamart y ETL | Incorporar evidencia de `01_datamart_etl.ipynb` o documentación equivalente. | No se observa ese notebook en el repositorio actual. |
| Visualización | Agregar capturas, medidas DAX o archivo Power BI. | No se observa `02_visualizacion.ipynb` ni carpeta `powerbi/`. |
| Clasificación | Corregir o justificar la elección del modelo exportado y la categoría vacía de riesgo. | Hay 685 clientes con probabilidad 0.0 sin etiqueta de riesgo. |
| Segmentación | Validar nombres comerciales de clusters. | Los nombres exportados podrían no coincidir con el perfil RFM mostrado. |
| Informe final | Integrar resultados técnicos con lenguaje ejecutivo. | Requiere revisión conjunta del equipo. |
