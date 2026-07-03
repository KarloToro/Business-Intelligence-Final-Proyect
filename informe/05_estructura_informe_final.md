# 05. Estructura del informe final

## Orden propuesto del informe

| Sección | Contenido esperado | Responsable sugerido | Estado |
| --- | --- | --- | --- |
| Carátula | Universidad, curso, título, integrantes, docente y fecha | Alex Palomino | Pendiente de datos formales |
| Índice | Tabla de contenidos del informe | Alex Palomino | Pendiente |
| Resumen ejecutivo | Síntesis de objetivo, datos, resultados principales y recomendaciones | Alex Palomino | Borrador en `informe/04_resumen_conclusiones_etica.md` |
| Empresa y problemática | Descripción de empresa ficticia, problemática, objetivos y preguntas de negocio | Alex Palomino | Borrador en `informe/01_contexto_negocio.md` |
| Generación de datos | Supuestos, fuentes sintéticas, reglas y archivos generados | Karlo Toro | Cubierto parcialmente en `Resumen Datos Sinteticos.md` y scripts |
| Datamart y ETL | Modelo estrella, relaciones, validaciones, limpieza y carga | Leslie Diaz | Cubierto parcialmente por datos procesados y `scripts/validar_dataset.py` |
| Visualización | Dashboard, medidas, gráficos e interpretación | Leslie Diaz | Pendiente de dashboard o evidencia |
| Clasificación | Objetivo del modelo, variables, entrenamiento, métricas e interpretación | Hector Huapaya | Pendiente de `03_clasificacion.ipynb` |
| Segmentación | RFM, clusters, perfil de segmentos y estrategia | Hector Huapaya | Pendiente de `04_segmentacion.ipynb` |
| Asociación | Canasta de mercado, reglas, soporte, confianza, lift y recomendaciones | Hector Huapaya | Pendiente de `05_asociacion.ipynb` |
| Regresión | Pronóstico, variable objetivo, métricas de error e interpretación | Hector Huapaya | Pendiente de `06_regresion.ipynb` |
| Reflexión ética | Datos sintéticos, privacidad, sesgos y uso de IA | Alex Palomino | Borrador en `informe/04_resumen_conclusiones_etica.md` |
| Conclusiones | Cierre general basado en evidencia | Alex Palomino | Borrador parcial |
| Recomendaciones | Acciones propuestas por hallazgo | Alex Palomino | Borrador parcial |
| Tabla de contribución | Rol, actividades, porcentaje y evidencia | Alex Palomino | Plantilla en `informe/tabla_contribuciones.md` |

## Consolidación recomendada

1. Usar `README.md` para presentar el alcance general del proyecto.
2. Usar `Resumen Datos Sinteticos.md` como base de la sección de generación de datos.
3. Usar `scripts/validar_dataset.py` como evidencia de consistencia del datamart.
4. Usar `scripts/explorar_dataset.py` como evidencia inicial de KPI e insights.
5. Integrar resultados de Power BI y notebooks faltantes solo cuando existan archivos o capturas verificables.
6. Mantener los marcadores `[PENDIENTE: ...]` hasta que cada integrante entregue su parte.

## Partes ya cubiertas y partes faltantes

| Parte | Cubierta | Falta |
| --- | --- | --- |
| Contexto general | Sí, en README y este informe | Nombre formal de la empresa ficticia si el equipo desea asignarlo |
| Datos sintéticos | Sí | Capturas o explicación final de ejecución en notebook |
| Datamart | Parcialmente | Notebook `01_datamart_etl.ipynb` o documentación final del modelo |
| Visualización | No visible en repositorio | Archivo Power BI, capturas, medidas DAX e interpretación |
| Clasificación | No visible en repositorio | Notebook, métricas e interpretación |
| Segmentación | No visible en repositorio | Notebook, clusters y perfiles |
| Asociación | No visible en repositorio | Reglas, soporte, confianza y lift |
| Regresión | No visible en repositorio | Modelo, métricas de error y pronóstico |
| Informe final | Parcialmente | Integración con resultados técnicos faltantes |
