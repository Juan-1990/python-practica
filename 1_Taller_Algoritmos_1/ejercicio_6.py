#Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%), 
# y el valor total de la factura, si al valor de la compra 
# se le autoriza un descuento del 10% (antes de aplicarle el IVA).
compra = float(input("Ingrese el monto de la compra: "))
descuento = compra * 0.10
iva = descuento * 0.19
subtotal = descuento + iva
subtotal = round(subtotal, 2)
total = compra + subtotal
print(f"El valor de la compra es: {compra}")
print(f"El valor del descuento es {descuento}")
print(f"El valor del iva es: {iva}")
print(f"El valor total a pagar es {total}")