from Cliente import Cliente
from Productos import Productos
from Pedido import Pedido


print("=" * 30)
print("====SISTEMA DE PEDIDOS====")
print("=" * 30)

cliente1 = Cliente("Camilo Vargas", "jcvr081990@gmail.com", 3003316289)
cliente2 = Cliente("Olga Valentina", "laolgavale@gmail.com", 3027896645)

producto1 = Productos("SmartTV", "E0021", 1800000)
producto2 = Productos("Samsung S24", "A098", 3300000)

pedido1 = Pedido(cliente1, producto2, "17/11/2025")
pedido2 = Pedido(cliente2, producto1, "17/11/2025")

pedido1.mostrarPedido()
pedido2.mostrarPedido()