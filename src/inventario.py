import logging
import sentry_sdk
import os
from dotenv import load_dotenv
from database import inicializar_db
from funciones import (
    agregar_producto,
    mostrar_productos,
    actualizar_producto,
    eliminar_producto,
    buscar_productos,
    generar_reporte
)

# Configuración de logging
logging.basicConfig(
    filename='inventario.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Cargar variables del archivo .env
load_dotenv()

# Configuración de Sentry
sentry_sdk.init(
    dsn="https://e08040f90b546ee2a41ca67c6a0fc500@o4509113964101632.ingest.us.sentry.io/4509113970720768",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    traces_sample_rate=1.0,
    environment="production"
)

# Función para agregar un producto
'''
def agregar_producto():
    try:
        print("\n--- AGREGAR PRODUCTO ---")
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío, intente nuevamente.")
        
        descripcion = input("Descripción: ").strip()
        
        # Validar cantidad y precio
        cantidad = int(input("Cantidad disponible: "))
        precio = float(input("Precio unitario: $"))
        if cantidad < 0 or precio <= 0:
            raise ValueError("Error: La cantidad debe ser mayor o igual a 0 y el precio mayor a 0.")

        categoria = input("Categoría: ").strip()
        
        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio": precio,
            "categoria": categoria
        }
        productos.append(producto)
        print(f" Producto '{nombre}' agregado exitosamente.")

    except ValueError as e:
        print(f"\n {str(e)}")
        logging.error(f"Error en agregar_producto: {str(e)}")
    except Exception as e:
        print("\n Error inesperado. Contacta al administrador.")
        logging.critical(f"Error crítico en agregar_producto: {str(e)}")
        sentry_sdk.capture_exception(e)  # Para Sentry
        '''

# Función para mostrar todos los productos    
'''
def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    if not productos:
        print("No hay productos registrados.")
    else:
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. {producto['nombre']} - {producto['cantidad']} unidades (${producto['precio']}) - Categoría: {producto['categoria']}")
'''

# Función para actualizar un producto
'''
def actualizar_producto():
    try:
        if not productos:
            print("No hay productos para actualizar.")
            return

        mostrar_productos()
        num = int(input("\nNúmero del producto a actualizar: ")) - 1
        
        if num < 0 or num >= len(productos):
            raise IndexError("Número de producto inválido.")

        producto = productos[num]
        print(f"\nEditando: {producto['nombre']}")
        
        # Actualizar solo campos no vacíos
        nuevo_nombre = input(f"Nuevo nombre ({producto['nombre']}): ").strip()
        producto['nombre'] = nuevo_nombre if nuevo_nombre else producto['nombre']
        
        nueva_cant = input(f"Nueva cantidad ({producto['cantidad']}): ").strip()
        producto['cantidad'] = int(nueva_cant) if nueva_cant else producto['cantidad']

        print("Producto actualizado")

    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
    except IndexError:
        print("Error: Número de producto no existe.")
    except Exception as e:
        print("Error inesperado")
        logging.error(f"Error en actualizar_producto: {str(e)}")
'''

# Función para eliminar un producto
'''
def eliminar_producto():
    try:
        if not productos:
            print("No hay productos para eliminar.")
            return

        mostrar_productos()
        num = int(input("\nNúmero del producto a eliminar: ")) - 1
        
        if num < 0 or num >= len(productos):
            raise IndexError("Número de producto inválido")

        producto = productos.pop(num)
        print(f"Producto '{producto['nombre']}' eliminado exitosamente.")

    except ValueError:
        print("Error: Debes ingresar un número")
    except IndexError:
        print("Error: Número de producto no existe")
    except Exception as e:
        print("Error inesperado")
        logging.error(f"Error en eliminar_producto: {str(e)}")
        if 'sentry_sdk' in globals():  # Para Sentry
            sentry_sdk.capture_exception(e)
'''
# Función para buscar/filtrar productos
'''
def buscar_productos():
    try:
        if not productos:
            print("No hay productos para buscar/filtrar.")
            return

        termino = input("Buscar por nombre o categoría: ").strip().lower()
        if not termino:
            raise ValueError("Término de búsqueda vacío.")

        resultados = [
            p for p in productos
            if termino in p['nombre'].lower() or termino in p['categoria'].lower()
        ]
        
        if not resultados:
            print("No se encontraron productos.")
        else:
            for p in resultados:
                print(f"{p['nombre']} - {p['categoria']} - Stock: {p['cantidad']}")

    except ValueError as e:
        print(f" {str(e)}")
        logging.warning(f"Búsqueda fallida: {str(e)}")
'''

# Función para generar reportes
'''
def generar_reporte():
    try:
        if not productos:
            print("No hay productos para generar reporte.")
            return

        total_productos = len(productos)
        valor_total = sum(p['precio'] * p['cantidad'] for p in productos)
        productos_agotados = [p for p in productos if p['cantidad'] == 0]

        print("\n=== REPORTE ===")
        print(f"Total de productos: {total_productos}")
        print(f"Valor total del inventario: ${valor_total:.2f}")
        print("\nProductos agotados:")
        for p in productos_agotados:
            print(f"- {p['nombre']}")

    except Exception as e:
        print("Error al generar reporte")
        logging.error(f"Error en generar_reporte: {str(e)}")
'''

# Menú principal
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar producto")
        print("2. Ver todos los productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar productos")
        print("6. Generar reporte")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_productos()
        elif opcion == "6":
            generar_reporte()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    inicializar_db()  # Esto crea la base de datos si no existe
    menu()            # Luego muestra el menú

