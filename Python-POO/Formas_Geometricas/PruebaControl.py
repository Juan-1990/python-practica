from Circulo import Circulo
from Rectangulo import Rectangulo

print("===FORMAS GEOMÉTRICAS===")

# ========== EJEMPLO 1: Crear círculos ==========
print("\n" + "=" * 50)
print("         EJEMPLO 1: CÍRCULOS")
print("=" * 50)

circulo1 = Circulo("Rojo", 5.0)
circulo1.mostrar_info()

circulo2 = Circulo("Azul", 3.5)
circulo2.mostrar_info()

# ========== EJEMPLO 2: Crear rectángulos ==========
print("\n" + "=" * 50)
print("         EJEMPLO 2: RECTÁNGULOS")
print("=" * 50)

rectangulo1 = Rectangulo("Verde", 10.0, 5.0)
rectangulo1.mostrar_info()

rectangulo2 = Rectangulo("Amarillo", 8.0, 8.0)
rectangulo2.mostrar_info()

if rectangulo2.es_cuadrado():
    print("✓ Este rectángulo es un CUADRADO")

# ========== EJEMPLO 3: POLIMORFISMO ==========
print("\n" + "=" * 50)
print("         EJEMPLO 3: POLIMORFISMO")
print("=" * 50)

# Lista con diferentes formas (Polimorfismo)
formas = [
    Circulo("Morado", 4.0),
    Rectangulo("Naranja", 6.0, 3.0),
    Circulo("Rosa", 7.5),
    Rectangulo("Cyan", 5.0, 5.0)
]

print("\nMostrando todas las formas usando POLIMORFISMO:")
print("-" * 50)

for i, forma in enumerate(formas, 1):
    print(f"\n>>> Forma #{i}")
    forma.mostrar_info()  # Llama al método correcto según el tipo

# ========== EJEMPLO 4: Modificar atributos ==========
print("\n" + "=" * 50)
print("         EJEMPLO 4: MODIFICAR ATRIBUTOS")
print("=" * 50)

print("\nEstado inicial del círculo:")
circulo_test = Circulo("Negro", 3.0)
circulo_test.mostrar_info()

print("\nCambiando el radio a 6.0...")
circulo_test.set_radio(6.0)
circulo_test.mostrar_info()

print("\nCambiando el color a 'Dorado'...")
circulo_test.set_color("Dorado")
circulo_test.mostrar_info()

# ========== EJEMPLO 5: Comparación de áreas ==========
print("\n" + "=" *50)
print("         EJEMPLO 5: COMPARACIÓN DE ÁREAS")
print("=" * 50)

circulo_comp = Circulo("Plata", 5.0)
rectangulo_comp = Rectangulo("Bronce", 7.0, 4.5)

print("\nComparando áreas:")
print("-" * 50)
circulo_comp.mostrar_info()
rectangulo_comp.mostrar_info()

if circulo_comp.get_area() > rectangulo_comp.get_area():
    print(f"\nEl CÍRCULO tiene mayor área: {circulo_comp.get_area():.2f} > {rectangulo_comp.get_area():.2f}")
elif circulo_comp.get_area() < rectangulo_comp.get_area():
    print(f"\nEl RECTÁNGULO tiene mayor área: {rectangulo_comp.get_area():.2f} > {circulo_comp.get_area():.2f}")
else:
    print("\nAmbas formas tienen la misma área")

# ========== EJEMPLO 6: Estadísticas ==========
print("\n" + "=" * 50)
print("         EJEMPLO 6: ESTADÍSTICAS")
print("=" * 50)

todas_formas = [
    Circulo("Rojo", 5.0),
    Circulo("Azul", 3.0),
    Rectangulo("Verde", 10.0, 5.0),
    Rectangulo("Amarillo", 7.0, 4.0),
    Circulo("Morado", 6.5)
]

area_total = sum(forma.get_area() for forma in todas_formas)
area_promedio = area_total / len(todas_formas)
forma_mayor = max(todas_formas, key=lambda f: f.get_area())

print(f"\nEstadísticas de {len(todas_formas)} formas:")
print(f"Area total:    {area_total:.2f} unidades²")
print(f"Area promedio: {area_promedio:.2f} unidades²")
print(f"\nForma con mayor área:")
forma_mayor.mostrar_info()

print("\n" + "=" * 50)
print("           FIN DE LAS PRUEBAS")
print("=" * 50)