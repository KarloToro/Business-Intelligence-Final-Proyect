# Universidad Nacional Mayor de San Marcos

**Facultad de Ingeniería de Sistemas e Informática**  
**Escuela Profesional de Ingeniería de Software**

---

# Informe del Proyecto Grupal

## Solución integral de Inteligencia de Negocios para una empresa retail ficticia

**Asignatura:** Inteligencia de Negocios  
**Docente:** Mg. Juan Gamarra Moreno  
**Semestre:** 2026-1  
**Equipo:** [PENDIENTE: nombre del equipo, si aplica]

| Integrante | Rol principal |
| --- | --- |
| Karlo Toro | Generación de datos |
| Hector Huapaya | Científico de datos |
| Leslie Diaz | Arquitecto de BI |
| Alex Palomino | Analista de negocio y editor del documento |

**Lima, Perú**  
**Fecha:** [PENDIENTE: completar fecha de entrega]

---

# Índice

1. Resumen ejecutivo  
2. Empresa ficticia, problemática y preguntas de negocio  
3. Generación de datos sintéticos  
4. Parte 1: Datamart analítico y ETL  
5. Parte 2: Visualización de datos  
6. Parte 3: Clasificación  
7. Parte 4: Segmentación  
8. Parte 5: Asociación  
9. Parte 6: Regresión  
10. Insights, recomendaciones y conclusiones  
11. Reflexión ética e integridad académica  
12. Registro de prompts  
13. Tabla de contribución del equipo  
14. Autoevaluación y lista de verificación  

---

# 1. Resumen ejecutivo

Este proyecto desarrolla una solución de Inteligencia de Negocios para una empresa retail ficticia, utilizando datos sintéticos generados con fines académicos. La solución busca convertir datos transaccionales en información accionable para apoyar decisiones sobre ventas, margen, productos, clientes, promociones, segmentación, asociación, abandono y pronóstico.

El repositorio contiene una base procesada con 5,000 clientes, 506 productos, 15 tiendas o canales, 29 promociones, 34,755 tickets y 55,858 líneas de venta para el periodo 2024-2025. La validación ejecutada mediante `scripts/validar_dataset.py` confirma consistencia en dimensiones, claves, fechas, promociones vigentes y canastas generadas.

Como primera lectura empresarial, los datos permiten reportar ingresos totales por S/ 1,428,828.48 y ganancia total por S/ 392,905.08. Además, los productos estrella muestran una contribución relevante, con S/ 762,080.07 en ingresos y S/ 216,172.97 en ganancia.

Después de la actualización del repositorio, existen resultados de clasificación, segmentación, asociación y regresión. La clasificación identifica 810 clientes en riesgo alto y 505 en riesgo medio; la segmentación agrupa a los 5,000 clientes en cuatro segmentos; la asociación genera 26 reglas de canasta de mercado; y el pronóstico de ventas con Gradient Boosting alcanza un MAE de S/ 261.19 y un MAPE de 13.45% en el periodo de prueba.

Estos resultados permiten avanzar hacia recomendaciones comerciales más concretas. Sin embargo, el informe mantiene espacios pendientes para integrar la evidencia de datamart, visualización y Power BI, así como para revisar algunos aspectos técnicos detectados en clasificación y segmentación.

---

# 2. Empresa ficticia, problemática y preguntas de negocio

## 2.1 Descripción de la empresa ficticia

El proyecto representa una empresa retail ficticia de tipo omnicanal, con tiendas físicas y canales online en distintas regiones del Perú. La empresa comercializa productos de consumo masivo y categorías complementarias como abarrotes, bebidas, lácteos, frutas y verduras, carnes y aves, limpieza, cuidado personal, hogar, bebés, mascotas, congelados, snacks y dulces.

Para efectos del informe final, se puede adoptar el nombre de referencia propuesto por las instrucciones del proyecto: **AndesMarket S.A.C.**.  

`[PENDIENTE: confirmar si el equipo usará formalmente el nombre AndesMarket S.A.C. o si mantendrá solo "empresa retail ficticia".]`

La operación simulada cuenta con:

| Elemento | Cantidad |
| --- | ---: |
| Clientes sintéticos | 5,000 |
| Productos | 506 |
| Tiendas o canales de venta | 15 |
| Promociones | 29 |
| Tickets de venta | 34,755 |
| Líneas de venta | 55,858 |
| Periodo de análisis | 2024-01-01 a 2025-12-31 |

## 2.2 Problemática del negocio

La empresa necesita transformar datos transaccionales en información útil para la toma de decisiones gerenciales. Sin una solución BI consolidada, la gerencia tendría dificultades para:

- monitorear ventas, margen y rentabilidad;
- identificar productos, segmentos y canales con mayor contribución;
- evaluar el comportamiento de clientes y promociones;
- detectar oportunidades de fidelización, segmentación y venta cruzada;
- anticipar riesgos de abandono;
- proyectar ventas futuras;
- sustentar decisiones comerciales con indicadores consistentes.

La problemática central no es la falta de datos, sino la necesidad de organizarlos, validarlos, modelarlos e interpretarlos para generar conocimiento accionable.

## 2.3 Objetivo general

Diseñar una solución de Inteligencia de Negocios para una empresa retail ficticia, capaz de transformar datos transaccionales sintéticos en información accionable que apoye decisiones comerciales, de fidelización, promoción, segmentación, venta cruzada y planificación de demanda.

## 2.4 Objetivos específicos

- Generar y documentar datos sintéticos consistentes para representar la operación de una empresa retail.
- Organizar los datos en un modelo dimensional tipo estrella, con una tabla de hechos de ventas y dimensiones de cliente, producto, tienda, promoción y tiempo.
- Definir KPI que permitan evaluar ventas, margen, ticket promedio, productos, clientes, promociones y canales.
- Construir visualizaciones ejecutivas para comunicar el desempeño del negocio.
- Aplicar modelos analíticos de clasificación, segmentación, asociación y regresión.
- Interpretar los resultados desde una perspectiva empresarial, evitando conclusiones no sustentadas.
- Elaborar recomendaciones accionables basadas en evidencia disponible.
- Incluir una reflexión ética sobre datos sintéticos, privacidad, sesgos, uso de IA y limitaciones de los modelos.

## 2.5 Preguntas de negocio

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

---

# 3. Generación de datos sintéticos

## 3.1 Alcance de los datos

Los datos del proyecto son completamente sintéticos y fueron generados con fines académicos. No corresponden a personas, empresas ni transacciones reales. Los archivos ubicados en `data/processed/` se consideran la fuente oficial para las etapas analíticas y de BI.

La generación de datos está documentada principalmente en `Resumen Datos Sinteticos.md`, en los scripts de la carpeta `scripts/` y en el notebook `notebooks/00_generacion_datos.ipynb`.

## 3.2 Tablas principales

| Tabla | Descripción | Campos principales |
| --- | --- | --- |
| `dim_cliente.csv` | Clientes sintéticos | `id_cliente`, `nombre`, `sexo`, `fecha_nacimiento`, `distrito`, `region`, `fecha_alta`, `segmento_programa` |
| `dim_producto.csv` | Catálogo de productos | `id_producto`, `nombre`, `categoria`, `subcategoria`, `marca`, `precio_lista`, `costo_unitario_promedio`, `producto_estrella` |
| `dim_tienda.csv` | Tiendas y canales | `id_tienda`, `nombre`, `canal`, `region`, `ciudad`, `prob_seleccion` |
| `dim_promocion.csv` | Promociones vigentes | `id_promocion`, `nombre`, `tipo`, `descuento_pct`, `fecha_inicio`, `fecha_fin` |
| `dim_tiempo.csv` | Calendario diario | `fecha`, `dia`, `mes`, `trimestre`, `anio`, `dia_semana`, `es_feriado` |
| `fact_ventas.csv` | Hechos de venta por línea | `id_venta`, `numero_linea`, `fecha`, `id_cliente`, `id_producto`, `id_tienda`, `id_promocion`, `cantidad`, `importe_venta`, `costo_total`, `margen` |

## 3.3 Reglas de negocio aplicadas

Entre las principales reglas de generación se encuentran:

- Todos los clientes realizan al menos una compra.
- Los clientes de segmentos superiores tienen mayor probabilidad de recompra.
- Las tiendas se asignan únicamente dentro de la región del cliente.
- Aproximadamente el 20% del catálogo se marca como producto estrella.
- Las asociaciones de productos permiten simular compras complementarias.
- Las promociones solo se aplican dentro de su periodo de vigencia.
- Cada ticket puede contener múltiples líneas de venta.

## 3.4 Validación del dataset

El script `scripts/validar_dataset.py` reporta que el dataset está limpio y consistente:

| Validación | Resultado |
| --- | --- |
| Dimensiones con claves únicas | Correcto |
| `fact_ventas` con claves foráneas válidas | Correcto |
| Fechas válidas y promociones dentro de vigencia | Correcto |
| Canastas sin duplicados ni exceso de líneas | Correcto |
| Clientes con venta | 5,000 |
| Productos vendidos | 506 |

`[PENDIENTE: si el equipo cuenta con datos en data/raw con problemas de calidad introducidos a propósito, agregar una subsección con el antes/después del proceso de limpieza, como solicita la rúbrica.]`

---

# 4. Parte 1: Datamart analítico y ETL

## 4.1 Modelo dimensional esperado

El modelo esperado corresponde a un esquema estrella, con `fact_ventas` como tabla de hechos y las dimensiones `dim_cliente`, `dim_producto`, `dim_tienda`, `dim_promocion` y `dim_tiempo`.

Relaciones esperadas:

| Relación | Tipo esperado |
| --- | --- |
| `fact_ventas.id_cliente` -> `dim_cliente.id_cliente` | Muchos a uno |
| `fact_ventas.id_producto` -> `dim_producto.id_producto` | Muchos a uno |
| `fact_ventas.id_tienda` -> `dim_tienda.id_tienda` | Muchos a uno |
| `fact_ventas.id_promocion` -> `dim_promocion.id_promocion` | Muchos a uno |
| `fact_ventas.fecha` -> `dim_tiempo.fecha` | Muchos a uno |

## 4.2 Grano de la tabla de hechos

El grano de `fact_ventas` es la línea individual de venta dentro de un ticket. Por ello, un mismo `id_venta` puede tener varias líneas, diferenciadas por `numero_linea`.

## 4.3 Evidencia disponible

Actualmente existe evidencia de consistencia del datamart mediante:

- `Resumen Datos Sinteticos.md`
- `scripts/validar_dataset.py`
- Archivos de `data/processed/`

`[PENDIENTE: incorporar desarrollo del notebook 01_datamart_etl.ipynb si Leslie o el equipo lo agregan.]`

`[PENDIENTE: incorporar diagrama del modelo estrella o captura del modelo en Power BI.]`

`[PENDIENTE: incorporar diccionario de datos final si el equipo lo desarrolla como sección o anexo.]`

---

# 5. Parte 2: Visualización de datos

## 5.1 Objetivo de la visualización

La visualización debe comunicar el desempeño del negocio de forma ejecutiva, permitiendo analizar ventas, margen, productos, clientes, promociones, canales, riesgo de abandono, segmentos, reglas de asociación y pronóstico.

## 5.2 KPI principales para el dashboard

| KPI | Descripción |
| --- | --- |
| Ventas totales | Ingreso total generado por ventas |
| Margen total | Ganancia bruta generada |
| Margen porcentual | Relación entre margen y ventas |
| Ticket promedio | Ventas totales divididas entre tickets |
| Clientes activos | Clientes con al menos una compra |
| Productos vendidos | Productos presentes en ventas |
| Ventas por segmento | Contribución por segmento de cliente |
| Ventas por categoría | Contribución por categoría de producto |
| Riesgo de abandono | Distribución de clientes por nivel de riesgo |
| Pronóstico de ventas | Comparación entre ventas reales y ventas estimadas |

## 5.3 Evidencia pendiente

`[PENDIENTE: incorporar archivo Power BI o capturas del dashboard.]`

`[PENDIENTE: documentar medidas DAX utilizadas: ventas, margen, ticket promedio, crecimiento, variación temporal u otras.]`

`[PENDIENTE: agregar 5 a 8 insights visuales sustentados en el tablero.]`

---

# 6. Parte 3: Clasificación

## 6.1 Objetivo del modelo

El objetivo de la clasificación es identificar clientes con riesgo de abandono o inactividad, a partir de variables derivadas del comportamiento transaccional. El notebook disponible es `notebooks/03_clasificacion_ipynb.ipynb`.

La variable objetivo se define a partir de una regla de negocio: clientes con 180 días o más sin compras son considerados en abandono.

## 6.2 Modelos comparados

El notebook compara tres modelos:

- Regresión Logística.
- Árbol de Decisión.
- Random Forest.

Se utiliza división estratificada y manejo de desbalance mediante `class_weight='balanced'`.

## 6.3 Métricas principales

| Modelo | Accuracy | Recall abandono | ROC-AUC |
| --- | ---: | ---: | ---: |
| Regresión Logística | 0.75 | 0.77 | 0.828 |
| Árbol de Decisión | 0.74 | 0.72 | 0.815 |
| Random Forest | 0.79 | 0.41 | 0.806 |

## 6.4 Resultado exportado

El archivo `data/processed/predicciones_abandono.csv` contiene 5,000 predicciones.

| Nivel de riesgo | Clientes |
| --- | ---: |
| Alto | 810 |
| Medio | 505 |
| Bajo | 3,000 |
| Sin etiqueta | 685 |

## 6.5 Interpretación empresarial

El modelo permite identificar una base prioritaria para campañas de retención. Los clientes en riesgo alto pueden recibir acciones comerciales más intensivas, como beneficios personalizados, recordatorios, cupones o campañas de recuperación. Los clientes en riesgo medio pueden ser monitoreados mediante campañas preventivas.

## 6.6 Observaciones técnicas

Aunque el notebook exporta predicciones usando Random Forest, la Regresión Logística muestra mejor ROC-AUC y mayor recall para la clase abandono. Si el objetivo principal es detectar clientes en abandono, conviene justificar la elección del modelo final o reconsiderar el modelo exportado.

Además, existen 685 clientes con probabilidad 0.0 que quedaron sin etiqueta de riesgo. Antes de usar el archivo en Power BI o en conclusiones finales, se recomienda corregir esa categorización.

---

# 7. Parte 4: Segmentación

## 7.1 Objetivo del modelo

La segmentación busca agrupar clientes con comportamientos similares mediante variables RFM:

- Recencia: días desde la última compra.
- Frecuencia: cantidad de compras o tickets.
- Monto: gasto total del cliente.

El notebook disponible es `notebooks/04_segmentacion.ipynb`.

## 7.2 Método utilizado

Se aplica K-Means con variables RFM estandarizadas. El notebook incluye evaluación del número de clusters mediante método del codo y coeficiente de silueta. Se utiliza `k = 4`.

## 7.3 Segmentos exportados

El archivo `data/processed/segmentos_clientes.csv` contiene 5,000 clientes segmentados.

| Segmento | Clientes |
| --- | ---: |
| Leales / Frecuentes | 2,206 |
| Campeones / VIP | 1,537 |
| Nuevos / Esporádicos | 690 |
| En Riesgo / Inactivos | 567 |

## 7.4 Interpretación empresarial

La segmentación permite plantear estrategias diferenciadas:

- Clientes de alto valor: beneficios exclusivos, programas de fidelización y preventa.
- Clientes frecuentes: promociones recurrentes y campañas de acumulación.
- Clientes esporádicos: incentivos de segunda compra y recordatorios.
- Clientes en riesgo: campañas de recuperación y ofertas personalizadas.

## 7.5 Observación técnica

El notebook muestra perfiles RFM por cluster. Antes de cerrar conclusiones, se recomienda validar que los nombres comerciales asignados correspondan correctamente a los promedios de recencia, frecuencia y monto de cada grupo.

---

# 8. Parte 5: Asociación

## 8.1 Objetivo del análisis

El análisis de asociación busca descubrir categorías que suelen comprarse juntas en una misma boleta, con el fin de proponer estrategias de venta cruzada y promociones combinadas.

El notebook disponible es `notebooks/05_asociacion.ipynb`.

## 8.2 Preparación de transacciones

Las ventas se agrupan por `id_venta` para construir canastas de compra. El análisis se realiza a nivel de categoría, lo cual permite obtener reglas más estratégicas y menos dispersas que un análisis por producto individual.

La matriz transaccional contiene:

| Elemento | Valor |
| --- | ---: |
| Canastas analizadas | 34,755 |
| Categorías evaluadas | 12 |

## 8.3 Reglas generadas

El archivo `data/processed/reglas_asociacion.csv` contiene 26 reglas de asociación con soporte, confianza y lift.

Regla destacada:

| Antecedente | Consecuente | Soporte | Confianza | Lift |
| --- | --- | ---: | ---: | ---: |
| Bebidas + Lácteos | Snacks y Dulces | 0.012 | 0.454 | 4.252 |

## 8.4 Interpretación empresarial

La regla anterior sugiere que, cuando una compra incluye bebidas y lácteos, aumenta la probabilidad relativa de que también incluya snacks y dulces. Esto puede usarse para diseñar combos, promociones cruzadas, recomendaciones en tienda o distribución conjunta en canales digitales.

## 8.5 Recomendaciones

- Priorizar reglas con lift alto y confianza comercialmente útil.
- Evitar usar reglas solo por soporte si no tienen interpretación de negocio.
- Validar las reglas principales en Power BI mediante filtros por categoría, tienda, canal y periodo.

---

# 9. Parte 6: Regresión

## 9.1 Objetivo del modelo

La regresión busca pronosticar ventas diarias para apoyar decisiones de inventario, campañas y planificación operativa. El notebook disponible es `notebooks/06_regresion.ipynb`.

## 9.2 Preparación de datos

Las ventas se agregan a nivel diario y se cruzan con la dimensión tiempo. Se incorporan variables temporales y rezagos, respetando el orden cronológico de los datos.

El conjunto se divide de forma secuencial:

| Conjunto | Días |
| --- | ---: |
| Entrenamiento | 579 |
| Prueba | 145 |

## 9.3 Modelos comparados

Se comparan tres modelos:

- Regresión Lineal.
- Random Forest Regressor.
- Gradient Boosting Regressor.

## 9.4 Métricas principales

| Modelo | MAE | RMSE | MAPE | R2 |
| --- | ---: | ---: | ---: | ---: |
| Regresión Lineal | S/ 297.19 | S/ 373.02 | 15.86% | 0.168 |
| Random Forest | S/ 281.19 | S/ 354.96 | 14.45% | 0.247 |
| Gradient Boosting | S/ 261.19 | S/ 335.67 | 13.45% | 0.327 |

## 9.5 Resultado exportado

El archivo `data/processed/pronostico_ventas.csv` contiene 145 días de comparación entre ventas reales y pronosticadas, desde 2025-08-09 hasta 2025-12-31.

## 9.6 Interpretación empresarial

El modelo Gradient Boosting presenta el mejor desempeño entre los modelos comparados. El MAPE de 13.45% indica un error porcentual moderado, útil como primera referencia para planificación. Sin embargo, el R2 de 0.327 muestra que todavía existe variabilidad no explicada por el modelo, por lo que el pronóstico debe usarse con prudencia en decisiones críticas.

---

# 10. Insights, recomendaciones y conclusiones

## 10.1 Insights principales

| Hallazgo | Evidencia | Interpretación | Recomendación |
| --- | --- | --- | --- |
| La operación sintética cubre una base completa de clientes compradores. | 5,000 clientes y 5,000 clientes con venta. | Permite analizar comportamiento de compra sobre toda la base generada. | Usar esta base para segmentación y clasificación, aclarando que es sintética. |
| El periodo de análisis cubre dos años completos. | Ventas desde 2024-01-01 hasta 2025-12-31. | Permite analizar tendencias y estacionalidad. | Usar cortes por mes, trimestre y año en Power BI. |
| Existen KPI generales consolidados. | Ingresos por S/ 1,428,828.48 y ganancia por S/ 392,905.08. | Existe línea base para resumen ejecutivo. | Colocar ventas, margen y ticket promedio en primera página del dashboard. |
| Productos estrella generan mayor ingreso. | S/ 762,080.07 frente a S/ 666,748.41 en productos no estrella. | La empresa depende de productos clave. | Priorizar disponibilidad y seguimiento de margen. |
| Hay clientes con riesgo alto y medio de abandono. | 810 riesgo alto y 505 riesgo medio. | Existe una base prioritaria para retención. | Diseñar campañas diferenciadas. |
| Existen reglas de venta cruzada. | 26 reglas exportadas; lift máximo 4.252. | Hay categorías con asociación comercial útil. | Usar reglas para combos y recomendaciones. |
| El pronóstico ofrece referencia para planificación. | Gradient Boosting: MAE S/ 261.19 y MAPE 13.45%. | Permite estimar ventas diarias con error moderado. | Usarlo como apoyo, no como decisión automática. |

## 10.2 Conclusiones generales

- El proyecto cuenta con una base sintética consistente y suficiente para desarrollar una solución BI académica.
- El modelo esperado corresponde a un esquema estrella con `fact_ventas` como tabla de hechos y dimensiones de cliente, producto, tienda, promoción y tiempo.
- La validación del dataset confirma que los archivos procesados pueden usarse como fuente oficial para las etapas posteriores.
- Los KPI generales de ventas, margen, tickets, líneas de venta, segmentos y productos ya pueden calcularse.
- La clasificación aporta una primera lectura del riesgo de abandono, pero debe revisarse la selección del modelo final si el objetivo principal es detectar clientes en abandono.
- La segmentación RFM permite agrupar clientes, pero los nombres comerciales deben validarse frente a los promedios de recencia, frecuencia y monto.
- Las reglas de asociación aportan evidencia para venta cruzada entre categorías.
- El pronóstico de ventas ofrece una referencia útil para planificación, aunque todavía hay margen de mejora.

## 10.3 Recomendaciones finales

- Consolidar el dashboard ejecutivo con KPI generales de ventas, margen, ticket promedio, productos, segmentos, riesgo de abandono, reglas de asociación y pronóstico.
- Completar o incorporar evidencia de datamart y visualización si existen fuera del repositorio actual.
- Revisar el notebook de clasificación para justificar por qué se exporta Random Forest cuando Regresión Logística muestra mejor ROC-AUC y recall para abandono.
- Corregir la categorización de riesgo en `predicciones_abandono.csv` para que las probabilidades 0.0 tengan una etiqueta válida.
- Validar los nombres comerciales de los clusters antes de usarlos en conclusiones del informe.
- Documentar en cada etapa la fuente, fórmula, gráfico o métrica que sustenta cada hallazgo.

---

# 11. Reflexión ética e integridad académica

El proyecto utiliza datos sintéticos, lo cual reduce riesgos de exposición de información personal real. Esta decisión es adecuada para un contexto académico porque permite practicar generación de datos, modelado BI y análisis sin comprometer la privacidad de clientes reales.

Sin embargo, los datos sintéticos también pueden contener sesgos derivados de las reglas usadas para generarlos. Por ejemplo, las probabilidades de recompra, selección de productos estrella, distribución de clientes por segmento o asignación regional no representan necesariamente el comportamiento real de un mercado. Por ello, las conclusiones deben interpretarse como válidas dentro del escenario simulado, no como evidencia directa sobre consumidores reales.

En términos de privacidad, aunque los nombres y perfiles sean artificiales, el informe debe aclarar que no se trabajó con datos personales reales. Si el proyecto se adaptara a una empresa real, sería necesario anonimizar datos, limitar accesos, justificar el uso de variables sensibles y cumplir normas de protección de datos.

Respecto al uso de inteligencia artificial, la IA puede apoyar la redacción, estructuración del informe, revisión de código y generación de ideas. No obstante, su uso debe registrarse de forma transparente, revisarse críticamente y no reemplazar la validación técnica del equipo.

También es importante reconocer que los modelos predictivos pueden generar errores y sesgos. En clasificación, un falso negativo podría dejar sin atención a un cliente realmente riesgoso, mientras que un falso positivo podría dirigir campañas innecesarias a clientes activos. En segmentación, nombres comerciales mal asignados pueden producir decisiones equivocadas. Por ello, toda métrica, conclusión o recomendación debe sustentarse en datos, código o visualizaciones verificables dentro del repositorio.

---

# 12. Registro de prompts

El uso de herramientas de IA fue documentado en el archivo:

```text
prompts/registro_prompts.md
```

Este archivo funciona como anexo técnico del proyecto y sigue la estructura solicitada por el profesor: número, parte, objetivo del prompt, herramienta/modelo, resultado obtenido y ajustes realizados.

`[PENDIENTE: verificar antes de la entrega final que el registro de prompts incluya la generación de datos sintéticos, la documentación, la clasificación, la segmentación, la asociación y la regresión.]`

---

# 13. Tabla de contribución del equipo

| Integrante | Rol | Actividades | Porcentaje aproximado | Evidencia |
| --- | --- | --- | ---: | --- |
| Karlo Toro | Generación de datos | Generación, documentación y validación inicial de los datos sintéticos; definición de supuestos de clientes, productos, tiendas, promociones, calendario y ventas. | [PENDIENTE] | `Resumen Datos Sinteticos.md`, `scripts/`, `data/processed/`, `notebooks/00_generacion_datos.ipynb` |
| Hector Huapaya | Científico de datos | Desarrollo de modelos analíticos de clasificación, segmentación, asociación y regresión; evaluación de métricas y explicación técnica de resultados. | [PENDIENTE] | `notebooks/03_clasificacion_ipynb.ipynb`, `notebooks/04_segmentacion.ipynb`, `notebooks/05_asociacion.ipynb`, `notebooks/06_regresion.ipynb`, `data/processed/predicciones_abandono.csv`, `data/processed/segmentos_clientes.csv`, `data/processed/reglas_asociacion.csv`, `data/processed/pronostico_ventas.csv` |
| Leslie Diaz | Arquitecto de BI | Diseño del datamart, organización del modelo dimensional, relaciones, ETL, visualización ejecutiva y soporte del dashboard de Power BI. | [PENDIENTE] | `data/processed/`, `scripts/validar_dataset.py`, [PENDIENTE: notebook ETL, archivo Power BI o capturas] |
| Alex Palomino | Analista de negocio / editor del documento final | Contexto de negocio, problemática, objetivos, preguntas de negocio, KPI, interpretación empresarial, insights, recomendaciones, resumen ejecutivo, conclusiones, reflexión ética, estructura del informe y tabla de contribución. | [PENDIENTE] | `informe/Informe_PG_AndesMarket.md`, `informe/01_contexto_negocio.md`, `informe/02_kpi_e_indicadores.md`, `informe/03_insights_y_recomendaciones.md`, `informe/04_resumen_conclusiones_etica.md`, `informe/05_estructura_informe_final.md` |

`[PENDIENTE: completar porcentajes aproximados. Deben sumar 100% y ser validados por el equipo.]`

---

# 14. Autoevaluación y lista de verificación

## 14.1 Autoevaluación por componente

| Componente | Punt. máx. | Peso en PG | Autopuntaje | Evidencia |
| --- | ---: | ---: | ---: | --- |
| Parte 1: Datamart | 20 | 20% | [PENDIENTE] | [PENDIENTE] |
| Parte 2: Visualización | 20 | 15% | [PENDIENTE] | [PENDIENTE] |
| Parte 3: Clasificación | 20 | 16% | [PENDIENTE] | `notebooks/03_clasificacion_ipynb.ipynb`, `predicciones_abandono.csv` |
| Parte 4: Segmentación | 20 | 16% | [PENDIENTE] | `notebooks/04_segmentacion.ipynb`, `segmentos_clientes.csv` |
| Parte 5: Asociación | 20 | 16% | [PENDIENTE] | `notebooks/05_asociacion.ipynb`, `reglas_asociacion.csv` |
| Parte 6: Regresión | 20 | 17% | [PENDIENTE] | `notebooks/06_regresion.ipynb`, `pronostico_ventas.csv` |
| Promedio ponderado de partes | 20 | 80% | [PENDIENTE] | [PENDIENTE] |
| Rúbrica transversal | 20 | 20% | [PENDIENTE] | Informe, prompts, repositorio y bitácora |
| PG estimado | 20 | 100% | [PENDIENTE] | [PENDIENTE] |

## 14.2 Lista de verificación final

| Criterio a verificar | Estado | Evidencia | Brecha detectada | Acción de mejora |
| --- | --- | --- | --- | --- |
| Datos sintéticos reproducibles y documentados | Parcial | `Resumen Datos Sinteticos.md`, scripts, `data/processed/` | Falta confirmar `data/raw/` si aplica | Incorporar evidencia de datos crudos o justificar enfoque |
| ETL corrige problemas de calidad y reporta antes/después | Parcial | `scripts/validar_dataset.py` | Falta notebook ETL visible | Agregar `01_datamart_etl.ipynb` o documentación equivalente |
| Esquema estrella y relaciones válidas en Power BI | Parcial | Relaciones esperadas documentadas | Falta captura o archivo Power BI | Incorporar modelo Power BI |
| Medidas DAX y tablero con páginas | Pendiente | [PENDIENTE] | No se observa archivo Power BI | Agregar dashboard o capturas |
| Storytelling con insights accionables | Parcial | Sección 10 | Falta integrar insights del dashboard | Actualizar cuando exista Power BI |
| Clasificación con comparación de modelos y métricas | Sí | `03_clasificacion_ipynb.ipynb` | Modelo exportado debe justificarse | Revisar selección final |
| Segmentación con k justificado y perfilamiento | Parcial | `04_segmentacion.ipynb` | Validar nombres de segmentos | Ajustar nombres si corresponde |
| Asociación con soporte, confianza y lift | Sí | `05_asociacion.ipynb`, `reglas_asociacion.csv` | Falta priorización final para negocio | Seleccionar reglas principales |
| Regresión con validación temporal y métricas | Sí | `06_regresion.ipynb`, `pronostico_ventas.csv` | R2 bajo/moderado | Explicar limitaciones y mejoras |
| Notebooks ejecutan de principio a fin | Pendiente | [PENDIENTE] | Falta validación final del equipo | Re-ejecutar notebooks antes de entrega |
| Repositorio Git con aportes de todos | Pendiente | Historial Git | Falta revisión de commits | Verificar aportes |
| Registro de prompts completo | Parcial | `prompts/registro_prompts.md` | Revisar cobertura final | Actualizar antes de entrega |
| Informe consolidado con estructura del Anexo C | Parcial | Este archivo | Faltan secciones de compañeros | Actualizar cuando entreguen |
| Tabla de contribución por integrante | Parcial | Sección 13 | Faltan porcentajes | Completar y validar |
| Sustentación con dominio individual | Pendiente | [PENDIENTE] | Requiere preparación oral | Ensayar preguntas por parte |
| Uso ético de IA declarado | Sí | Sección 11 y `prompts/registro_prompts.md` | Mantener trazabilidad | Revisar consistencia final |

---

# Anexos

## Anexo A. Registro de prompts

Ver archivo `prompts/registro_prompts.md`.

## Anexo B. Bitácora de trabajo

La bitácora de trabajo se gestiona en un Excel compartido del equipo.

`[PENDIENTE: al pasar a DOCX/PDF, incluir captura o tabla exportada de la bitácora si el profesor lo solicita.]`

## Anexo C. Evidencias pendientes por incorporar

- Capturas del modelo dimensional en Power BI.
- Capturas del dashboard ejecutivo.
- Medidas DAX utilizadas.
- Evidencia del notebook o documentación de ETL.
- Evidencia de ejecución completa de notebooks.
- Porcentajes finales de contribución.
- Autoevaluación final.

