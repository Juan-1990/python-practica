#Dadas las 3 notas de un aprendiz, calcule la definitiva de la asignatura 
# si la primera nota tiene un valor del 20%, la segunda del 30% y la última del 50%.
nota_1 = float(input("Ingresa la primera nota del aprendiz (20%): "))
nota_2 = float(input("Ingresa la segunda nota del aprendiz (30%): "))
nota_3 = float(input("Ingresa la tercera nota del aprendiz (50%): "))
definitiva = (nota_1 * 0.20) + (nota_2 * 0.30) + (nota_3 * 0.50)
definitiva = round(definitiva, 2)
print(f"La nota definitiva del aprendiz es: {definitiva}")