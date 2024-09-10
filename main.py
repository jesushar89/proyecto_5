import unittest


# Definición de las clases Producto e Inventario
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto_nombre):
        self.productos = [p for p in self.productos if p.nombre != producto_nombre]

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío")
        for producto in self.productos:
            producto.mostrar_detalles()


# Pruebas Unitarias para Inventario
class TestInventario(unittest.TestCase):

    def setUp(self):
        self.inventario = Inventario()
        self.producto1 = Producto("Manzana", 0.5, 100)
        self.producto2 = Producto("Banana", 0.3, 150)

    def test_agregar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.assertIn(self.producto1, self.inventario.productos)

    def test_eliminar_producto(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.eliminar_producto("Manzana")
        self.assertNotIn(self.producto1, self.inventario.productos)

    def test_mostrar_inventario(self):
        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto2)
        self.assertEqual(len(self.inventario.productos), 2)


# Este bloque se asegura de que las pruebas se ejecuten si el archivo es ejecutado directamente
if __name__ == '__main__':
    unittest.main()
