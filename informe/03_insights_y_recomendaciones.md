# 03. Insights y recomendaciones

## Criterio de uso

Este documento solo incluye hallazgos cuando existe evidencia en el repositorio. Para etapas sin resultados implementados se dejan marcadores pendientes, a fin de evitar métricas o conclusiones inventadas.

## Insights con evidencia disponible

| Hallazgo | Evidencia | Interpretación empresarial | Recomendación |
| --- | --- | --- | --- |
| La operación sintética cubre una base completa de clientes compradores. | `scripts/validar_dataset.py` reporta 5,000 clientes y 5,000 clientes con venta. | El dataset permite analizar comportamiento de compra sin clientes inactivos dentro del periodo generado. | Usar esta base como referencia para segmentación inicial, dejando claro que no representa abandono real sin una definición adicional de inactividad. |
| El periodo de análisis está completo para dos años. | La validación reporta ventas desde 2024-01-01 hasta 2025-12-31 y 731 días calendario. | Permite evaluar tendencias mensuales, estacionalidad y comparaciones anuales. | Construir visualizaciones por mes, trimestre y año antes de avanzar al pronóstico. |
| Los ingresos totales y margen ya pueden reportarse como KPI generales. | `scripts/explorar_dataset.py` reporta ingresos por S/ 1,428,828.48 y ganancia por S/ 392,905.08. | Existe una línea base para el resumen ejecutivo y el dashboard gerencial. | Incluir ventas, margen, ticket promedio y líneas promedio por ticket como indicadores de primera vista. |
| El segmento Bronce concentra el mayor ingreso total. | El script de exploración reporta para Bronce S/ 560,380.71 en ingresos y S/ 154,586.91 en ganancia. | Este segmento tiene alta relevancia por tamaño y contribución total, aunque no necesariamente por valor individual. | Analizar ticket promedio, frecuencia y migración potencial de Bronce hacia Plata u Oro. |
| Los productos estrella concentran mayor ingreso que los no estrella. | Productos estrella: S/ 762,080.07 en ingresos y S/ 216,172.97 en ganancia. No estrella: S/ 666,748.41 en ingresos y S/ 176,732.11 en ganancia. | La empresa depende de un grupo reducido de productos clave para una parte importante del desempeño comercial. | Priorizar disponibilidad, exhibición y seguimiento de margen en productos estrella, sin descuidar oportunidades de cola larga. |
| La canasta promedio tiene más de una línea por ticket. | `scripts/explorar_dataset.py` reporta 1.61 líneas promedio por venta. | Hay evidencia inicial de compras con múltiples productos, útil para análisis de asociación. | Completar el notebook de asociación para convertir esta señal en reglas de venta cruzada sustentadas. |

## Estructura para completar con resultados posteriores

### Visualización

| Hallazgo | Evidencia | Interpretación | Recomendación |
| --- | --- | --- | --- |
| [PENDIENTE: completar con resultado del dashboard de Power BI o notebook 02_visualizacion.ipynb] | [PENDIENTE: indicar gráfico, medida DAX o tabla usada] | [PENDIENTE: interpretación empresarial] | [PENDIENTE: recomendación accionable] |

### Clasificación

| Hallazgo | Evidencia | Interpretación | Recomendación |
| --- | --- | --- | --- |
| [PENDIENTE: completar con resultado del notebook 03_clasificacion.ipynb] | [PENDIENTE: incluir métrica del modelo y variables relevantes] | [PENDIENTE: explicar riesgo, abandono o propensión desde el negocio] | [PENDIENTE: proponer acción comercial o de fidelización] |

### Segmentación

| Hallazgo | Evidencia | Interpretación | Recomendación |
| --- | --- | --- | --- |
| [PENDIENTE: completar con resultado del notebook 04_segmentacion.ipynb] | [PENDIENTE: incluir clusters, variables RFM o perfil de segmentos] | [PENDIENTE: explicar diferencias entre segmentos] | [PENDIENTE: proponer estrategia diferenciada] |

### Asociación

| Hallazgo | Evidencia | Interpretación | Recomendación |
| --- | --- | --- | --- |
| [PENDIENTE: completar con resultado del notebook 05_asociacion.ipynb] | [PENDIENTE: incluir soporte, confianza y lift] | [PENDIENTE: interpretar relación entre productos] | [PENDIENTE: proponer venta cruzada o promoción combinada] |

### Regresión

| Hallazgo | Evidencia | Interpretación | Recomendación |
| --- | --- | --- | --- |
| [PENDIENTE: completar con resultado del notebook 06_regresion.ipynb] | [PENDIENTE: incluir variable objetivo, métrica de error y periodo evaluado] | [PENDIENTE: explicar utilidad del pronóstico] | [PENDIENTE: proponer uso en inventario, compras o planificación] |
