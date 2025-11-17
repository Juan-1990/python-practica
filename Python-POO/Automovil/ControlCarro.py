from Automovil import Automovil
from Motor import Motor

print("____Ejemplo de Composicion____")

motor1 = Motor(2000,"Gasolina",150)
auto1 = Automovil("Toyota", "Corolla", 2024, "Rojo", motor1)
auto1.mostrar_info()

print("\n--- Probando funcionalidad ---")
auto1.encender()
auto1.acelerar()
auto1.apagar()

print("\n" + "="*50 + "\n")

motor2 = Motor(cilindraje=3500, tipoCombustible="Gasolina Premium", potencia=300)
auto2 = Automovil("Ferrari", "F8", 2023, "Rojo Italiano", motor2)
auto2.mostrar_info()

print("\n--- Probando funcionalidad ---")
auto2.encender()
auto2.acelerar()
auto2.apagar()

print("\n" + "="*50 + "\n")

motor3 = Motor(cilindraje=1000, tipoCombustible="Gasolina", potencia=65)
auto3 = Automovil("Chevrolet", "Spark", 2024, "Azul", motor3)
auto3.mostrar_info()

print("\n--- Probando funcionalidad ---")
auto3.encender()
auto3.acelerar()

print("\n--- Probando error: acelerar sin encender ---")
auto3.apagar()
auto3.acelerar()