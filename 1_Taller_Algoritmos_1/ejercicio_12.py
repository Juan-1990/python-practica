# Un maestro desea saber qué porcentaje de hombres 
# y qué porcentaje de mujeres hay en un grupo de alumnos.
hombres = int(input("Cuantos hombres hay?\n"))
mujeres = int(input("Cuantas mujeres hay?\n"))
print(f"El porcentaje de hombres es: {(hombres/(hombres+mujeres))*100}%")
print(f"El porcentaje de mujeres es: {(mujeres/(hombres+mujeres))*100}%")