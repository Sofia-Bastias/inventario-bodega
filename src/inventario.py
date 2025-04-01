# inventario.py - Gestión de Inventario (CRUD + Filtros + Reportes)
productos = []  # Lista para almacenar los productos

# Función para agregar un producto
def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    nombre = input("Nombre del producto: ").strip()
    descripcion = input("Descripción: ").strip()
    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio unitario: $"))
    categoria = input("Categoría (Ej: Electrónica, Ropa): ").strip()

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio": precio,
        "categoria": categoria
    }
    productos.append(producto)
    print(f"✅ Producto '{nombre}' agregado al inventario.")

# Función para mostrar todos los productos
def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    if not productos:
        print("No hay productos registrados.")
    else:
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. {producto['nombre']} - {producto['cantidad']} unidades (${producto['precio']}) - Categoría: {producto['categoria']}")

# Función para actualizar un producto
def actualizar_producto():
    mostrar_productos()
    if not productos:
        return

    try:
        num = int(input("\nNúmero del producto a actualizar: ")) - 1
        producto = productos[num]
        print(f"\nEditando: {producto['nombre']}")
        producto['nombre'] = input(f"Nuevo nombre ({producto['nombre']}): ") or producto['nombre']
        producto['descripcion'] = input(f"Nueva descripción ({producto['descripcion']}): ") or producto['descripcion']
        producto['cantidad'] = int(input(f"Nueva cantidad ({producto['cantidad']}): ") or producto['cantidad'])
        producto['precio'] = float(input(f"Nuevo precio (${producto['precio']}): $") or producto['precio'])
        producto['categoria'] = input(f"Nueva categoría ({producto['categoria']}): ") or producto['categoria']
        print("✅ Producto actualizado.")
    except (ValueError, IndexError):
        print("❌ Error: Número de producto inválido.")

# Función para eliminar un producto
def eliminar_producto():
    mostrar_productos()
    if not productos:
        return

    try:
        num = int(input("\nNúmero del producto a eliminar: ")) - 1
        producto = productos.pop(num)
        print(f"✅ Producto '{producto['nombre']}' eliminado.")
    except (ValueError, IndexError):
        print("❌ Error: Número de producto inválido.")

# Función para buscar/filtrar productos
def buscar_productos():
    print("\n--- BUSCAR PRODUCTOS ---")
    termino = input("Buscar por nombre o categoría: ").lower()
    resultados = [
        p for p in productos
        if termino in p['nombre'].lower() or termino in p['categoria'].lower()
    ]
    
    if not resultados:
        print("No se encontraron productos.")
    else:
        for p in resultados:
            print(f"{p['nombre']} - {p['categoria']} - Stock: {p['cantidad']}")

# Función para generar reportes
def generar_reporte():
    print("\n--- REPORTE DE INVENTARIO ---")
    total_productos = len(productos)
    valor_total = sum(p['precio'] * p['cantidad'] for p in productos)
    productos_agotados = [p for p in productos if p['cantidad'] == 0]

    print(f"Total de productos: {total_productos}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print("\nProductos agotados:")
    for p in productos_agotados:
        print(f"- {p['nombre']}")

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
            print("❌ Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
