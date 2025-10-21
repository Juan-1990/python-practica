# #20  Ingresar el precio de compra unitario de un producto y 
# la cantidad de compra de dicho producto y un descuento. Calcular y
# mostrar el subtotal, el monto del IVA que es el 19% del subtotal, 
# y el precio neto (precio parcial con el Monto del IVA).

import random
numero = random.randint(3000,10000)
producto = str(input("Que producto deseas comprar:\n"))
precio = float(numero)
cantidad = int(input("Que cantidad deseas llevar: "))
print(f"Vas a llevar {cantidad} {producto} que tiene un sub total de {cantidad*precio} y con iba te quedaria {(cantidad * precio) + ((cantidad * precio) * 0.19)}")