# Requerimientos del Sistema  

## Validación (¿Qué se necesita?)  
- **Requerimientos originales**:  
  - CRUD de productos.  
  - Gestión de stock.  
  - Filtrado por categoría.  

- **Requerimientos ampliados/validados**:  
  - El nombre del producto es obligatorio.  
  - Precio debe ser > 0.  
  - Búsqueda funciona por nombre *o* categoría.  

## Verificación (¿Cómo se cumple?)  
| Requerimiento          | Método de Verificación           | Evidencia         |  
|------------------------|----------------------------------|------------------|  
| CRUD funcional          | Pruebas manuales (agregar/editar/eliminar) | [Capturas](/docs/crud-funciones.png) |  
| Filtrado por categoría  | Test unitario en `buscar_productos()` | [Código](/inventario.py#L130) |  
| Reportes en consola     | Ejecución y validación de salida | [Ejemplo](/docs/reporte-consola.png) |  

## Supuestos  
- No se valida el formato de la descripción (puede estar vacía).  
