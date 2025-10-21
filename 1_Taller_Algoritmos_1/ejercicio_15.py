#15. Suponga que tiene Ud. 
# una tienda y desea registrar las ventas en una computadora. 
# Diseñe un algoritmo en pseudocódigo que lea por 
# cada cliente: 
#●	El monto de la venta, calcule e imprima el IVA.
#●	calcule e imprima el total a pagar 
#●	lea la cantidad con la que paga el cliente (solo efectivo), calcule e imprima el cambio. 2
#Registramos ventas
ventas = []
i = 0
cantidad = int(input("Cuantas compras vas a registrar?"))
while True:
    i += 1
    venta = float(input(f"Ingrese la venta numero {i}: "))
    venta_iva = venta + (venta * 0.19)
    ventas.append(venta)
    if i == cantidad:
        break
print(ventas)