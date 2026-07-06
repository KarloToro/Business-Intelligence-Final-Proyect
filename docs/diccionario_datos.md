# Diccionario de datos — Datamart retail

| Tabla | Campo | Tipo | Descripción | Clave/FK |
| --- | --- | --- | --- | --- |
| fact_ventas | id_venta | int | PK lógica del ticket | No |
| fact_ventas | numero_linea | int | Número de línea dentro del ticket | No |
| fact_ventas | fecha | date | Fecha de la venta (FK → dim_tiempo) | Sí |
| fact_ventas | id_cliente | int | Cliente (FK → dim_cliente) | Sí |
| fact_ventas | id_tienda | int | Tienda/canal (FK → dim_tienda) | Sí |
| fact_ventas | id_producto | int | Producto (FK → dim_producto) | Sí |
| fact_ventas | id_promocion | int | Promoción aplicada (FK → dim_promocion) | Sí |
| fact_ventas | cantidad | int | Unidades vendidas | No |
| fact_ventas | precio_unitario_lista | float | Precio de lista unitario | No |
| fact_ventas | descuento_pct | float | Descuento aplicado (0-1) | No |
| fact_ventas | precio_unitario_final | float | Precio unitario neto | No |
| fact_ventas | importe_venta | float | Métrica: ingreso de la línea | No |
| fact_ventas | costo_total | float | Costo total de la línea | No |
| fact_ventas | margen | float | Métrica: importe_venta - costo_total | No |
| dim_cliente | id_cliente | int | PK del cliente | Sí |
| dim_cliente | nombre | str | Nombre del cliente | No |
| dim_cliente | sexo | str | Sexo (M/F) | No |
| dim_cliente | fecha_nacimiento | date | Fecha de nacimiento | No |
| dim_cliente | distrito | str | Distrito de residencia | No |
| dim_cliente | region | str | Región | No |
| dim_cliente | fecha_alta | date | Primera compra / alta en programa | No |
| dim_cliente | segmento_programa | str | Segmento fidelización (Bronce, Plata, Oro...) | No |
| dim_producto | id_producto | int | PK del producto | Sí |
| dim_producto | nombre | str | Nombre del producto | No |
| dim_producto | categoria | str | Categoría comercial | No |
| dim_producto | subcategoria | str | Subcategoría | No |
| dim_producto | marca | str | Marca | No |
| dim_producto | precio_lista | float | Precio de lista | No |
| dim_producto | costo_unitario_promedio | float | Costo unitario promedio | No |
| dim_producto | producto_estrella | bool | Indicador producto estrella (Pareto) | No |
| dim_tienda | id_tienda | int | PK de tienda/canal | Sí |
| dim_tienda | nombre | str | Nombre de la tienda | No |
| dim_tienda | canal | str | Físico u Online | No |
| dim_tienda | region | str | Región de operación | No |
| dim_tienda | ciudad | str | Ciudad | No |
| dim_promocion | id_promocion | int | PK de promoción | Sí |
| dim_promocion | nombre | str | Nombre de la campaña | No |
| dim_promocion | tipo | str | Tipo de promoción | No |
| dim_promocion | descuento_pct | float | Porcentaje de descuento | No |
| dim_promocion | fecha_inicio | date | Inicio de vigencia | No |
| dim_promocion | fecha_fin | date | Fin de vigencia | No |
| dim_tiempo | fecha | date | PK del calendario | Sí |
| dim_tiempo | dia | int | Día del mes | No |
| dim_tiempo | mes | int | Mes | No |
| dim_tiempo | trimestre | int | Trimestre | No |
| dim_tiempo | anio | int | Año | No |
| dim_tiempo | dia_semana | str | Nombre del día | No |
| dim_tiempo | es_feriado | bool | Indicador de feriado | No |
