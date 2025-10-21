#Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura.
nota_1 = float(input("Ingrese la nota del aprendiz: "))
nota_2 = float(input("Ingrese la nota del aprendiz: "))
nota_3 = float(input("Ingrese la nota del aprendiz: "))
definitiva = (nota_1 + nota_2 + nota_3) / 3
definitiva = round(definitiva, 2)
print(f"La nota definitiva del aprendiz es: {definitiva}")