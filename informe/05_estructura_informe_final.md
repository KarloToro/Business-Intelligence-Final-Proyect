# 05. Estructura del informe final

## Orden propuesto del informe

| Sección | Contenido esperado | Responsable sugerido | Estado |
| --- | --- | --- | --- |
| Carátula | Universidad, curso, título, integrantes, docente y fecha | Alex Palomino | Pendiente de datos formales |
| Índice | Tabla de contenidos del informe | Alex Palomino | Pendiente |
| Resumen ejecutivo | Síntesis de objetivo, datos, resultados principales y recomendaciones | Alex Palomino | Actualizado en `informe/04_resumen_conclusiones_etica.md` |
| Empresa y problemática | Descripción de empresa ficticia, problemática, objetivos y preguntas de negocio | Alex Palomino | Actualizado en `informe/01_contexto_negocio.md` |
| Generación de datos | Supuestos, fuentes sintéticas, reglas y archivos generados | Karlo Toro | Cubierto por `Resumen Datos Sinteticos.md`, scripts y `notebooks/00_generacion_datos.ipynb` |
| Datamart y ETL | Modelo estrella, relaciones, validaciones, limpieza y carga | Leslie Diaz | Cubierto parcialmente por datos procesados y `scripts/validar_dataset.py`; falta notebook visible de ETL |
| Visualización | Dashboard, medidas, gráficos e interpretación | Leslie Diaz | Pendiente de dashboard, capturas o archivo Power BI visible |
| Clasificación | Objetivo del modelo, variables, entrenamiento, métricas e interpretación | Hector Huapaya | Cubierto parcialmente por `notebooks/03_clasificacion_ipynb.ipynb` y `predicciones_abandono.csv` |
| Segmentación | RFM, clusters, perfil de segmentos y estrategia | Hector Huapaya | Cubierto parcialmente por `notebooks/04_segmentacion.ipynb` y `segmentos_clientes.csv` |
| Asociación | Canasta de mercado, reglas, soporte, confianza, lift y recomendaciones | Hector Huapaya | Cubierto parcialmente por `notebooks/05_asociacion.ipynb` y `reglas_asociacion.csv` |
| Regresión | Pronóstico, variable objetivo, métricas de error e interpretación | Hector Huapaya | Cubierto parcialmente por `notebooks/06_regresion.ipynb` y `pronostico_ventas.csv` |
| Reflexión ética | Datos sintéticos, privacidad, sesgos, modelos predictivos y uso de IA | Alex Palomino | Actualizado en `informe/04_resumen_conclusiones_etica.md` |
| Conclusiones | Cierre general basado en evidencia | Alex Palomino | Borrador actualizado |
| Recomendaciones | Acciones propuestas por hallazgo | Alex Palomino | Borrador actualizado |
| Tabla de contribución | Rol, actividades, porcentaje y evidencia | Alex Palomino | Actualizada en `informe/tabla_contribuciones.md` |

## Consolidación recomendada

1. Usar `README.md` para presentar el alcance general del proyecto.
2. Usar `Resumen Datos Sinteticos.md` como base de la sección de generación de datos.
3. Usar `scripts/validar_dataset.py` como evidencia de consistencia del datamart.
4. Usar `scripts/explorar_dataset.py` como evidencia inicial de KPI e insights comerciales.
5. Incorporar los resultados de `predicciones_abandono.csv`, `segmentos_clientes.csv`, `reglas_asociacion.csv` y `pronostico_ventas.csv`.
6. Integrar resultados de Power BI y datamart ETL cuando existan archivos o capturas verificables.
7. Mantener los marcadores `[PENDIENTE: ...]` solo donde falte evidencia real.

## Partes ya cubiertas y partes faltantes

| Parte | Cubierta | Falta o revisar |
| --- | --- | --- |
| Contexto general | Sí, en README y este informe | Nombre formal de la empresa ficticia si el equipo desea asignarlo |
| Datos sintéticos | Sí | Capturas o explicación final de ejecución si el profesor lo solicita |
| Datamart | Parcialmente | Notebook `01_datamart_etl.ipynb` o documentación final del modelo |
| Visualización | No visible en repositorio | Archivo Power BI, capturas, medidas DAX e interpretación |
| Clasificación | Sí, parcialmente | Justificar modelo final y corregir etiquetas vacías de riesgo |
| Segmentación | Sí, parcialmente | Validar nombres comerciales de clusters frente al perfil RFM |
| Asociación | Sí, parcialmente | Interpretar reglas más relevantes y priorizar acciones comerciales |
| Regresión | Sí, parcialmente | Explicar limitaciones del R2 y posibles mejoras de variables |
| Informe final | Parcialmente | Integración final con resultados técnicos revisados |
