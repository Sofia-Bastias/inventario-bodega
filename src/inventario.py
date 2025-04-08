import logging
import sentry_sdk
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


# Configuración de Sentry
sentry_sdk.init(
    dsn="https://[TU-DSN].ingest.sentry.io/[PROJECT-ID]", # Reemplaza con tu DSN de Sentry
    traces_sample_rate=1.0,
    environment="production"
)

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

