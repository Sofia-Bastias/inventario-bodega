import unittest
from unittest.mock import patch
from funciones import agregar_producto, mostrar_productos, actualizar_producto, eliminar_producto
from database import inicializar_db, conectar


class TestProductos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Este método se ejecuta antes de todas las pruebas. Se encarga de iniciar la base de datos. """
        # Crear la base de datos y las tablas si no existen
        inicializar_db()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """ Este método se ejecuta antes de cada prueba. Limpiar la tabla de productos antes de cada prueba. """
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos")  # Limpiar la tabla de productos antes de cada prueba
        conn.commit()
        conn.close()

    # TEST 1: Agregar producto
    @patch('builtins.input', side_effect=[
        "TestProducto",         # nombre
        "Producto de prueba",   # descripcion
        "10",                   # cantidad
        "99.99",                # precio
        "Pruebas"               # categoria
    ])
    def test_agregar_producto(self, mock_input):
        agregar_producto()

        # Ahora verificamos que el producto fue agregado
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, descripcion, cantidad, precio, categoria FROM productos")
        producto = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(producto)
        self.assertEqual(producto, ("TestProducto", "Producto de prueba", 10, 99.99, "Pruebas"))
    
    # TEST 2: Agregar producto sin nombre
    @patch('builtins.input', side_effect=[
        "",                     # nombre
        "Producto de prueba",   # descripcion
        "10",                   # cantidad
        "99.99",                # precio
        "Pruebas"               # categoria
    ])
    def test_agregar_producto_sin_nombre(self, mock_input):
        with self.assertRaises(ValueError) as context:
            agregar_producto()
        
        # Verificamos que se lanzó la excepción con el mensaje correcto
        self.assertEqual(str(context.exception), "❌ Error al agregar producto\n.ERROR:root:Error en agregar_producto: El nombre no puede estar vacío.")


    @patch('builtins.input', side_effect=[
        "TestProducto",         # nombre
        "Producto de prueba",   # descripcion
        "10",                   # cantidad
        "99.99",                # precio
        "Pruebas",              # categoria
        "1",                    # id
        "Producto B",           # nuevo nombre
        "15"                    # nueva cantidad
    ])
    def test_actualizar_producto(self, mock_input):
        agregar_producto()        
        # Luego actualizar ese producto
        actualizar_producto()

        # Verificar que el producto ha sido actualizado
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, descripcion, cantidad, precio, categoria FROM productos")
        producto = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(producto)
        self.assertEqual(producto, ("Producto B", "Producto de prueba", 15, 99.99, "Pruebas"))
    
    @patch('builtins.input', side_effect=[
        "TestProducto",         # nombre
        "Producto de prueba",   # descripcion
        "10",                   # cantidad
        "99.99",                # precio
        "Pruebas",              # categoria
        "9999",                 # id
        "Producto B",           # nuevo nombre
        "15"                    # nueva cantidad
    ])
    def test_actualizar_producto_no_existente(self, mock_input):
        agregar_producto()
        # Luego actualizar ese producto
        actualizar_producto()

        # Verificar que el producto ha sido actualizado
        # Ahora verificamos que el producto fue agregado
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, descripcion, cantidad, precio, categoria FROM productos")
        producto = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(producto)
        self.assertEqual(producto, ("Producto B", "Producto de prueba", 15, 99.99, "Pruebas"))


    @patch('builtins.input', side_effect=[
        "TestProducto",         # nombre
        "Producto de prueba",   # descripcion
        "10",                   # cantidad
        "99.99",                # precio
        "Pruebas",              # categoria
        "4"                    # id
    ])
    def test_eliminar_producto(self, mock_input):
        # Primero agregar un producto
        agregar_producto()

        # Luego eliminar ese producto
        eliminar_producto()

        # Verificar que la lista de productos esté vacía
        productos = mostrar_productos()
        self.assertEqual(productos, None)


if __name__ == '__main__':
    unittest.main()
