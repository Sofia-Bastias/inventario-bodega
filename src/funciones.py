# funciones.py
# Aqui estan todas las funciones que se encargan de la logica del programa
import sqlite3
from database import conectar
import logging
import sentry_sdk


# Función para agregar un producto
def agregar_producto():
    try:
        print("\n--- AGREGAR PRODUCTO ---")
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        descripcion = input("Descripción: ").strip()
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        categoria = input("Categoría: ").strip()

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))
        conn.commit()
        conn.close()

        print(f"✅ Producto '{nombre}' agregado.")

    except Exception as e:
        print("❌ Error al agregar producto.")
        logging.error(f"Error en agregar_producto: {str(e)}")
        sentry_sdk.capture_exception(e)
        
# Función para mostrar todos los productos
def mostrar_productos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, cantidad, precio, categoria FROM productos")
        filas = cursor.fetchall()
        conn.close()

        if not filas:
            print("No hay productos registrados.")
            return

        print("\n--- LISTA DE PRODUCTOS ---")
        for fila in filas:
            print(f"{fila[0]}. {fila[1]} - {fila[2]} unidades - ${fila[3]} - {fila[4]}")
    
    except Exception as e:
        print("❌ Error al mostrar productos:", str(e))
        
# Función para actualizar un producto
def actualizar_producto():
    try:
        mostrar_productos()
        producto_id = int(input("\nID del producto a actualizar: "))

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
        producto = cursor.fetchone()

        if not producto:
            print("Producto no encontrado.")
            return

        print(f"\nEditando: {producto[1]}")
        nuevo_nombre = input(f"Nuevo nombre ({producto[1]}): ").strip()
        nueva_cantidad = input(f"Nueva cantidad ({producto[3]}): ").strip()

        cursor.execute("""
            UPDATE productos SET nombre = ?, cantidad = ? WHERE id = ?
        """, (
            nuevo_nombre if nuevo_nombre else producto[1],
            int(nueva_cantidad) if nueva_cantidad else producto[3],
            producto_id
        ))
        conn.commit()
        conn.close()

        print("✅ Producto actualizado.")
    except ValueError:
        print("❌ Error: La cantidad debe ser un número entero.")
    except IndexError:
        print("❌ Error: Número de producto no existe.")
    except Exception as e:
        print("❌ Error al actualizar producto:", str(e))
        logging.error(f"Error en actualizar_producto: {str(e)}")
        
# Función para eliminar un producto
def eliminar_producto():
    try:
        mostrar_productos()
        producto_id = int(input("\nID del producto a eliminar: "))

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conn.commit()
        conn.close()

        print("✅ Producto eliminado exitosamente.")
    except ValueError:
        print("❌ Error: Debes ingresar un número.")
    except IndexError:
        print("❌ Error: Número de producto no existe.")
    except Exception as e:
        print("❌ Error inesperado")
        logging.error(f"Error en eliminar_producto: {str(e)}")
        if 'sentry_sdk' in globals():  # Para Sentry
            sentry_sdk.capture_exception(e)        
        
# Función para buscar/filtrar productos
def buscar_productos():
    try:
        termino = input("Buscar por nombre o categoría: ").strip().lower()

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, nombre, cantidad, categoria FROM productos
            WHERE LOWER(nombre) LIKE ? OR LOWER(categoria) LIKE ?
        """, (f"%{termino}%", f"%{termino}%"))
        resultados = cursor.fetchall()
        conn.close()

        if resultados:
            for p in resultados:
                print(f"{p[0]}. {p[1]} - {p[3]} - Stock: {p[2]}")
        else:
            print("No se encontraron productos.")

    except ValueError as e:
        print(f" {str(e)}")
        logging.warning(f"❌ Error: Búsqueda fallida: {str(e)}")    
    
    
# Función para generar reportes
def generar_reporte():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*), SUM(precio * cantidad) FROM productos")
        total, valor_total = cursor.fetchone()

        cursor.execute("SELECT nombre FROM productos WHERE cantidad = 0")
        agotados = cursor.fetchall()

        conn.close()

        print("\n=== REPORTE ===")
        print(f"Total de productos: {total}")
        print(f"Valor total del inventario: ${valor_total:.2f}")
        print("Productos agotados:")
        for nombre in agotados:
            print(f"- {nombre[0]}")

    except Exception as e:
        print("Error al generar reporte")
        logging.error(f"❌ Error en generar_reporte: {str(e)}")

