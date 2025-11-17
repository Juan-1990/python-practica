from Productos import Productos
from Cliente import Cliente

class Pedido:
    def __init__(self, cliente, producto, fecha):
        self._cliente = cliente
        self._producto = producto
        self._fecha = fecha
        self._total = producto.get_precio()

    def set_cliente(self, cliente):
        self._cliente = cliente

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_total(self, total):
        self._total = total

    def set_precio_unitario(self, precio_unitario):
        self._precio_unitario = precio_unitario

    
    def get_cliente(self):
        return self._cliente

    def get_fecha(self):
        return self._fecha

    def get_total(self):
        return self._total

    """ def get_precio_unitario(self):
        return self._precio_unitario """
    
    def mostrarPedido(self):
        print("=" * 30)
        print("===Datos del Cliente===")
        print(f"Nombre Cliente: {self._cliente.get_nombre()}")
        print(f"Correo: {self._cliente.get_email()}")
        print(f"Telefono: {self._cliente.get_telefono()}")
        print()
        print("PRODUCTO ADQUIRIDO")
        print(f"Nombre Producto: {self._producto.get_nombre()}")
        print(f"Codigo: {self._producto.get_codigo()}")
        print(f"Precio: {self._producto.get_precio():,.0f}")
        print(f"Total a pagar: ${self._total:,.0f}")
    