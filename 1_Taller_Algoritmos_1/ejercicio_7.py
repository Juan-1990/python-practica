# Dada una cantidad de tiempo medida en horas, 
# minutos y segundos, diga a cuántos segundos equivale.
hora = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

hora = 3600
minutos = 60
total_segundos = minutos * hora
print(f"el total de segundos es: {total_segundos}")