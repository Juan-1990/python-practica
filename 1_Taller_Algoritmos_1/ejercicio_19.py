# Ingresar, para un estudiante, sus 5 notas de un curso, 
# nombre, programa, ficha.  Hacer un algoritmo que:
# Muestre el nombre
# Muestre el programa de formación
# Se debe calcular y mostrar su promedio final.

nombre = input("Ingrese el nombre del estudiante: ")
programa = input("Ingrese el programa de formación: ")
ficha = input("Ingrese el número de ficha: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
nota5 = float(input("Nota 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f"Nombre: {nombre}")
print(f"Programa de formación: {programa}")
print(f"Ficha: {ficha}")
print(f"Promedio final: {promedio:.2f}")