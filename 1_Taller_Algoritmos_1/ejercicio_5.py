#5.	Lea la distancia (en kilómetros) recorrida por un auto, 
# el tiempo (en horas) en que la recorrió y calcule 
# la velocidad a la cual se desplazaba el auto (V=D/T).
distancia = float(input("Ingresa la distancia recorrida en kilometros: "))
tiempo = float(input("Ingrese el tiempo que recorrio en horas: "))
if tiempo == 0:
    print("Error: el tiempo no puede ser cero")
else:
    velocidad = distancia / tiempo
    velocidad = round(velocidad, 2)
    print(f"La velocidad del auto es: {velocidad} km/h")