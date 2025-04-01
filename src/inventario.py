# inventario.py (CRUD + stock mínimo)
productos = []

def agregar_producto():
    nombre = input("Nombre: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio, "categoria": categoria}
    productos.append(producto)
    print("✅ Producto agregado")

def mostrar_productos():
    for p in productos:
        print(f"{p['nombre']} - {p['cantidad']} unidades (${p['precio']})")

# Ejemplo de uso (esto lo mejora tu compañero después)
while True:
    print("\n1. Agregar\n2. Ver todos\n3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        break
