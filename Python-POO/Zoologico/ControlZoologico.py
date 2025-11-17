
Animal = __import__("Animal").Animal
Mamifero = __import__("Mamifero").Mamifero
Ave = __import__("Ave").Ave
Cuidador = __import__("Cuidador").Cuidador
Jaula = __import__("Jaula").Jaula


cuidador1 = Cuidador("Camilo", 7)


animal1 = Mamifero("Oso de Anteojos", 6, "Andino", "Largo y negro")
animal2 = Mamifero("Jaguar", 5, "Africano", "Manchado")
animal3 = Ave("Cóndor de los Andes", 8, "Cóndor", 3.2)

jaula1 = Jaula(1, [animal1, animal2, animal3], cuidador1)


print("=== INFORMACIÓN DEL ZOOLÓGICO ===")
print(f"Número de jaula: {jaula1.get_numero()}")
print(f"Cuidador: {jaula1.get_cuidador().get_nombre_cuidador()}")
print(f"Años de experiencia: {jaula1.get_cuidador().get_years_exp()}")

print("\n--- Oso de Anteojos ---")
print(f"Nombre: {animal1.get_nombre()}")
print(f"Edad: {animal1.get_edad()}")
print(f"Especie: {animal1.get_especie()}")
print(f"Tipo de pelaje: {animal1.get_tipo_pelaje()}")

print("\n--- Jaguar ---")
print(f"Nombre: {animal2.get_nombre()}")
print(f"Edad: {animal2.get_edad()}")
print(f"Especie: {animal2.get_especie()}")
print(f"Tipo de pelaje: {animal2.get_tipo_pelaje()}")

print("\n--- Cóndor ---")
print(f"Nombre: {animal3.get_nombre()}")
print(f"Edad: {animal3.get_edad()}")
print(f"Envergadura: {animal3.get_alas()} metros")
      
print("\n=== COMPORTAMIENTOS ===")
animal1.hacer_sonido()
animal1.comer()
animal1.amamantar()
animal3.volar()


print("\n=== OPERACIONES DE JAULA ===")
cuidador2 = Cuidador("Valentina", 5)
jaula1.asignar_cuidador(cuidador2)

animal4 = Mamifero("Mono Araña", 3, "Ateles", "Negro")
jaula1.asignar_animal(animal4)

jaula1.retirar_animal(animal2)

print(f"\nNuevo cuidador: {jaula1.get_cuidador().get_nombre_cuidador()}")