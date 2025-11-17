from Vehiculos import Vehiculos
from VehiculosTerrestres import VehiculosTerrestres
from VehiculosAcuaticos import VehiculosAcuaticos

#VEHICULOS TERRESTRES

print("=" * 50)
print("Vehiculos Terrestres")
print("=" * 50)

moto1 = VehiculosTerrestres("Honda", "NX500", "2 Personas", 2)
moto2 = VehiculosTerrestres("Yamaha", "R7", "2 Personas", 2)

carro1 = VehiculosTerrestres("Chevrolet", "Spark", "4 Personas", 4)
carro2 = VehiculosTerrestres("Renault", "Sandero", "4 Personas", 4)

camioneta1 = VehiculosTerrestres("Toyota", "Hilux", "4 Personas", 4)
camioneta2 = VehiculosTerrestres("Ford", "Ranger", "4 Personas", 4)

bus1 = VehiculosTerrestres("Chevrolet", "NPR Euro", "60 Personas", 6)
bus2 = VehiculosTerrestres("Chevrolet", "Buseton NQR Euro VI", "70 Personas", 6)

#VEHICULOS ACUATICOS

print("\n" + "= " * 50)
print("Vehiculos Acuaticos")
print("=" * 50)

lancha1 = VehiculosAcuaticos("Lancha BK1", "BK1", "19 Personas", "outboard motor")

yate1 = VehiculosAcuaticos("Azimut", "Grande 36M", "16 Personas", "POD")

barco = VehiculosAcuaticos("Crucero", "Royal Caribbean", "Miles de personas", "Sistemas diésel-eléctricos, que alimentan propulsores azimutales para una mejor eficiencia y maniobrabilidad.")

print("\n" + "= " * 50)
print("DEMOSTRACIONES")
print("=" * 50)

moto1.mostrar_info()
moto1.manejar()
moto1.frenar()
moto1.moverse()

print()
bus1.mostrar_info()
bus1.manejar()
bus1.frenar()
bus1.moverse()

print()
lancha1.mostrar_info()
lancha1.moverse()
lancha1.manejar()
lancha1.anclar()

print()
yate1.mostrar_info()
yate1.moverse()
yate1.anclar()
yate1.manejar()

print("\n" + "= " * 50)
print("TODOS LOS VEHICULOS CREADOS EXITOSAMENTE")
print("=" * 50)