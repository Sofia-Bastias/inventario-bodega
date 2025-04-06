# Gestión de Inventario  
**Integrantes**: Álvaro Sánchez y Sofía Bastías  
## Requerimientos completados  
- CRUD de productos.  
- Filtrado por categoría (asumido).  
- Reportes en consola.  

## Flujo de Trabajo (GitHub Flow)  
Elegimos **GitHub Flow** por:  
- **Simplicidad**: Solo usamos la rama `main` con protección activada.  
- **Rapidez**: No necesitamos múltiples ramas para un equipo de 2 personas.  
- **Prácticas estándar**: Es el modelo usado por GitHub en proyectos pequeños.  

### Reglas del repositorio  
1. **Protección de rama `main`**:  
   - Requiere 1 aprobación en PR antes de merge.  
   - Bloquea force pushes.  
2. **Commits descriptivos (esto se intenta)**: Ej: "Agrega CRUD de productos".  

## Configuración de GitHub  
- **Protección de ramas**: Activada para la rama `main`, requiriendo 1 aprobación en PRs antes de hacer merge.  
  ![Captura](/docs/repo-branch.png)  
## Integración con Slack  
Notificaciones configuradas en el canal `#github-alerts` mediante la app de GitHub:  
- Se suscribió al repo `Sofía-Bastias/inventario-bodega` para recibir updates de commits, pulls y issues.  
![Suscripción exitosa](/docs/slack-integration-success.png)  

## Manejo/Control de Excepciones  
El sistema controla los siguientes errores:  

| Función              | Errores manejados                           |  
|----------------------|--------------------------------------------|  
| `agregar_producto`   | Nombre vacío, cantidad/precio inválidos    |  
| `actualizar_producto`| Número de producto inválido, valores negativos |  
| `eliminar_producto`  | Índice incorrecto, entrada no numérica     |  
| `buscar_productos`   | Término de búsqueda vacío                  |  
| `generar_reporte`    | Inventario vacío                           |  

### 1. Validación de Entradas
- **Campos obligatorios vacíos**:  

  Si el nombre del producto está vacío:
  ```python
  if not nombre:
      raise ValueError("El nombre no puede estar vacío, intente nuevamente.") #Mensaje al usuario
- **Datos numéricos inválidos**:

  Si se ingresa texto en cantidad o precio:
  ```python
  cantidad = int(input("Cantidad disponible: "))  # Si se ingresa "abc"
  ```
     Mensaje al usuario (en actualizar_producto):
   ```python
   except ValueError:
        print("Error: La cantidad debe ser un número entero.")
   ```
   Si la cantidad es negativa o el precio ≤ 0:
   ```python
  if cantidad < 0 or precio <= 0:
    raise ValueError("Error: La cantidad debe ser mayor o igual a 0 y el precio mayor a 0.") #Mensaje al usuario
   ```
### 2. Operaciones Riesgosas
- **Índices inválidos**:

  Al intentar actualizar/eliminar un producto que no existe:
   ```python
   if num < 0 or num >= len(productos):
    raise IndexError("Número de producto inválido.") #Mensaje al usuario
   ```
- **Búsquedas vacías**:

  Si no se ingresa término de búsqueda:
   ```python
   if not termino:
    raise ValueError("Término de búsqueda vacío.") #Mensaje al usuario
   ```
### 3. Errores Inesperados
- **Fallos críticos** (ej: fallo de sistema):
   ```python
   except Exception as e:
    print("Error inesperado. Contacta al administrador.")
    logging.critical(f"Error crítico en agregar_producto: {str(e)}")
   ```
