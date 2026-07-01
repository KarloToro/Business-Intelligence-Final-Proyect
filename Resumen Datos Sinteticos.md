# Resumen de creación de datos sintéticos

## Objetivo

Este proyecto genera un conjunto de datos sintéticos para simular la operación de una empresa retail durante dos años (2024–2025). El propósito es disponer de información suficientemente realista para desarrollar las etapas posteriores del proyecto de Inteligencia de Negocios (Power BI, modelado dimensional, dashboards, KPIs y análisis), sin utilizar datos reales.

Los archivos contenidos en `data/processed` representan la versión final del dataset y son los que deben utilizarse durante el resto del proyecto.

---

# Archivos disponibles

## dim_cliente.csv

Contiene aproximadamente **5,000 clientes**.

Campos principales:

* id_cliente
* nombre
* sexo
* fecha_nacimiento
* distrito
* region
* fecha_alta
* segmento_programa

### Consideraciones

* Todos los clientes realizan al menos una compra.
* `fecha_alta` corresponde a la fecha de la primera compra realizada por el cliente.
* Los segmentos del programa de fidelización fueron generados con una distribución probabilística y posteriormente utilizados durante la generación de ventas para simular diferentes probabilidades de recompra.

---

## dim_producto.csv

Contiene aproximadamente **500 productos**.

Campos principales:

* id_producto
* nombre
* categoria
* subcategoria
* marca
* precio_lista
* costo_unitario_promedio
* producto_estrella

Adicionalmente existen columnas de asociación entre productos:

* asociacion_1
* asociacion_2
* asociacion_3

### Consideraciones

Los productos marcados como **producto_estrella** representan aproximadamente el 20% del catálogo y concentran la mayor parte de las ventas.

Las asociaciones permiten simular compras complementarias durante la generación de un mismo ticket.

---

## dim_tienda.csv

Contiene las tiendas disponibles para la empresa.

Campos principales:

* id_tienda
* nombre
* canal
* ciudad
* region
* prob_seleccion

### Consideraciones

Las ventas únicamente pueden asignarse a tiendas pertenecientes a la misma región del cliente.

---

## dim_promocion.csv

Contiene las promociones disponibles durante los años 2024 y 2025.

Campos principales:

* id_promocion
* nombre
* tipo
* descuento_pct
* fecha_inicio
* fecha_fin

### Consideraciones

Las promociones solamente pueden aplicarse dentro de su periodo de vigencia.

---

## dim_tiempo.csv

Calendario diario comprendido entre:

* 2024-01-01
* 2025-12-31

Incluye:

* fecha
* día
* mes
* trimestre
* año
* día de la semana
* indicador de fin de semana
* indicador de feriado
* nombre del feriado

Esta tabla está diseñada para relacionarse con `fact_ventas` mediante el campo **fecha**.

---

## fact_ventas.csv

Tabla de hechos que contiene el detalle de cada línea de venta.

Campos principales:

* id_venta
* numero_linea
* fecha
* id_cliente
* id_producto
* id_tienda
* id_promocion
* cantidad
* precio_unitario_lista
* descuento_pct
* precio_unitario_final
* importe_venta
* costo_total
* margen

Cada fila representa una línea individual dentro de un ticket de venta.

---

# Supuestos utilizados durante la generación

La información fue generada siguiendo reglas de negocio con el objetivo de producir un comportamiento razonablemente realista.

Entre las principales reglas se encuentran:

* Todos los clientes realizan al menos una compra.
* Los clientes pertenecientes a segmentos superiores presentan mayor probabilidad de recompra.
* Las tiendas se asignan únicamente dentro de la región del cliente.
* Aproximadamente el 20% de los productos concentra la mayor parte de las ventas (productos estrella).
* Los productos pueden generar ventas complementarias utilizando asociaciones entre subcategorías.
* Las promociones únicamente se aplican cuando se encuentran vigentes.
* Cada ticket puede contener múltiples líneas de venta.

---

# Relaciones esperadas

El modelo estrella esperado es el siguiente:

* fact_ventas.id_cliente → dim_cliente.id_cliente
* fact_ventas.id_producto → dim_producto.id_producto
* fact_ventas.id_tienda → dim_tienda.id_tienda
* fact_ventas.id_promocion → dim_promocion.id_promocion
* fact_ventas.fecha → dim_tiempo.fecha

No es necesario volver a generar estas relaciones mediante Python; deben establecerse directamente durante el modelado en Power BI.

---

# Consideraciones para el equipo

Los archivos presentes en `data/processed` deben considerarse la fuente oficial de datos para las siguientes etapas del proyecto.

Los scripts de generación se utilizaron únicamente para construir el dataset y no forman parte del flujo normal de análisis.

Si en etapas posteriores fuese necesario introducir ruido, valores atípicos o escenarios específicos para experimentación, se recomienda trabajar sobre una copia del dataset generado, preservando esta versión como referencia limpia y consistente.
