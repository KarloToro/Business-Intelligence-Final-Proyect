
## B.1 Resumen del proceso de generación de datos sintéticos

La generación de los datos de AndesMarket no se realizó mediante un único prompt ni mediante una asignación completamente aleatoria. Se trabajó de forma iterativa, construyendo primero tablas maestras y reglas de negocio, para después implementar scripts reproducibles que generaran clientes, calendario y ventas coherentes entre sí.

### 1. Construcción de los catálogos base

Las dimensiones de Producto, Tienda y Promoción fueron tratadas como catálogos maestros curados.

- **Producto:** El catálogo se construyó iterativamente por categorías, generando lotes de productos con nombre, subcategoría, marca, precio de lista y costo unitario promedio. Posteriormente se añadió la clasificación `producto_estrella` para distinguir los productos de alta rotación y se incorporaron campos de asociación entre subcategorías para permitir la generación de canastas de compra relacionadas.
    
- **Tienda:** Esta dimensión definió establecimientos físicos y canales online distribuidos en las regiones donde opera la empresa ficticia. Cada tienda recibió una probabilidad de selección, empleada posteriormente dentro de su propia región.
    
- **Promoción:** Incluyó campañas comerciales de 2024 y 2025, con fechas de inicio y fin, tipo de promoción y porcentaje de descuento. Esto permitió que el generador aplicara solamente promociones vigentes en la fecha y canal correspondiente. El notebook carga estos catálogos como entradas curadas antes de generar las transacciones.
    

### 2. Estimación de la distribución geográfica de clientes

Para evitar distribuir los clientes uniformemente entre todos los distritos, se elaboró la tabla maestra `distribucion_clientes_por_distrito.csv`. La estimación combinó dos criterios en el campo `peso_final`:

- **Peso regional:** Aproximación de la presencia comercial de AndesMarket a partir de la cantidad de tiendas ficticias ubicadas en cada región.
    
- **Peso distrital:** Participación de cada distrito dentro de su región utilizando población distrital del INEI correspondiente a 2022.
    

Se seleccionaron principalmente distritos urbanos y comercialmente representativos: 14 distritos de Lima y 7 distritos por cada una de las demás regiones consideradas. El volumen total se fijó en 5,000 clientes sintéticos. Para cada cliente, el script realiza un muestreo ponderado mediante el `peso_final`, de manera que los distritos más poblados y las regiones con mayor presencia comercial tengan una representación mayor, sin copiar ni utilizar registros de personas reales.

### 3. Generación de clientes

El script `generar_clientes.py` crea los 5,000 registros de la dimensión cliente utilizando una semilla fija para asegurar la reproducibilidad. Los nombres se construyen a partir de tablas maestras separadas (nombres femeninos, nombres masculinos y apellidos) y los siguientes atributos se asignan de forma ponderada:

- Sexo.
    
- Rango de edad y fecha de nacimiento.
    
- Región y distrito.
    
- Segmento del programa de fidelización.
    

La distribución del programa se definió en cuatro niveles (No afiliado, Bronce, Plata y Oro) y cada segmento recibió una probabilidad diferente de recompra, haciendo que los clientes de niveles superiores tengan mayor presencia en las compras repetidas. La columna `fecha_alta` se deja temporalmente vacía y luego se completa con la fecha de la primera compra real generada, evitando inconsistencias entre la dimensión y la tabla de hechos.

### 4. Generación de la dimensión Tiempo

El script `generar_dim_tiempo.py` construye el calendario completo entre el 1 de enero de 2024 y el 31 de diciembre de 2025. Para cada fecha se derivan atributos como día, mes, trimestre, año y día de la semana, e identifica los feriados peruanos, permitiendo analizar temporalmente las ventas respecto a campañas, feriados y periodos estacionales.

### 5. Generación de ventas

El script `generar_ventas.py` produce los tickets y las líneas de venta para los dos años de operación.

Se definieron 45 tickets diarios durante los meses regulares y 60 tickets diarios durante julio y diciembre (representando el aumento por Fiestas Patrias y fin de año), lo que produce aproximadamente 34,755 tickets base. Los primeros 5,000 tickets garantizan que cada cliente realice al menos una compra (conectándolos a la tabla de hechos y completando su `fecha_alta`).

Para las recompras posteriores, los clientes se eligen mediante muestreo ponderado según su nivel:

|**Segmento de Fidelización**|**Probabilidad de Recompra**|
|---|---|
|**No afiliado**|0.12|
|**Bronce**|0.28|
|**Plata**|0.47|
|**Oro**|0.72|

_Nota: La tienda se elige después del cliente y solamente entre las de su región, evitando compras físicas ilógicas en otras zonas geográficas._

Para cada ticket se selecciona un producto base (80% de probabilidad para productos estrella, 20% para los no estrella) y se aplica la posibilidad de incorporar productos asociados para generar canastas coherentes. Finalmente, el script aplica las promociones vigentes y calcula la cantidad, precio de lista, descuento, precio final, importe de venta, costo total y margen.

### 6. Validación de la versión limpia

Antes de inyectar problemas de calidad, el conjunto es validado en memoria. Las comprobaciones estructurales incluyen:

- Todos los clientes tienen al menos una venta.
    
- `fecha_alta` coincide con la primera compra.
    
- No existen claves foráneas huérfanas.
    
- No existen duplicados en el grano `id_venta` + `numero_linea`.
    
- Cada día contiene la cantidad de tickets definida.
    
- Todas las fechas se encuentran dentro del calendario.
    
- Las referencias a producto, tienda y promoción son válidas.
    

Esto asegura que los errores hallados posteriormente sean fruto del ruido intencional.

### 7. Introducción controlada de ruido

Tras validar la versión limpia, se crea una copia para la capa `data/raw` a la que se le introducen problemas de calidad:

- Fechas de enero a junio de 2024 en formato DD/MM/YYYY, mientras que el resto permanece en formato ISO YYYY-MM-DD.
    
- ~0.8% de valores faltantes en `descuento_pct`.
    
- ~1.5% de valores faltantes en la marca de los productos.
    
- Duplicación de ~0.6% de las líneas de venta.
    
- Inconsistencia en la capitalización de los nombres de clientes, alternando aleatoriamente entre mayúsculas y minúsculas sin respetar las reglas ortográficas de la RAE para nombres propios.
    

Estas tablas alteradas se exportan a `data/raw/` y son consumidas posteriormente por el notebook `01_datamart_etl.ipynb` para generar la versión limpia en `data/processed/`.

### Resumen de Componentes y Scripts

|**Archivo / Componente**|**Responsabilidad Principal**|
|---|---|
|**`config.py`**|Centraliza la semilla, volúmenes, fechas, probabilidades de edad, segmentos y recompra.|
|**`generar_clientes.py`**|Genera los 5,000 clientes a partir de tablas maestras y distribuciones ponderadas.|
|**`generar_dim_tiempo.py`**|Construye el calendario 2024–2025 con atributos temporales y feriados peruanos.|
|**`generar_ventas.py`**|Genera tickets y líneas, garantiza la primera compra, simula recompras, selecciona tienda, productos y promociones y calcula las métricas.|
|**`inyectar_ruido.py`** _(o equivalentes)_|Introduce formatos mixtos, nulos, duplicados y variantes textuales para la capa _raw_.|
|**`validar_dataset.py`**|Comprueba volúmenes, fechas, grano, cobertura de clientes e integridad referencial.|
|**`00_generacion_datos.ipynb`**|Orquesta el flujo completo: carga catálogos, ejecuta generación, valida, introduce ruido y exporta los CSV.|