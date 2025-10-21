#14. Se trata de escribir el algoritmo que permita emitir 
# la factura correspondiente a una compra de varios artículos 
# (4) determinados, del que se adquieren una o varias unidades. El IVA es del 19%.
tomate = 5000
leche = 6000
arepa = 1500
huevo = 400
total = 0
total_unidades = 0
objeto = int(input("MARCA\n1. para toamte\n2. para leche\n3. para arepa\n4. para huevo\n"))

while True:
    objeto = int(input(" "))
    if objeto == 1:
        print(f"Tomate : {tomate}")
        total += tomate
        total_unidades += 1
    elif objeto == 2:
        print(f"Leche : {leche}")
        total += leche
        total_unidades += 1
    elif objeto == 3:
        print(f"Arepa : {arepa}")
        total += arepa
        total_unidades += 1
    elif objeto == 4:
        print(f"Huevo : {huevo}")
        total += huevo
        total_unidades += 1
    else:
        print("saliendo de la facturacion")
        break
print(f"El total a pagar con iva es: {total + (total * 0.19)}\nTotal de unidades es: {total_unidades}")