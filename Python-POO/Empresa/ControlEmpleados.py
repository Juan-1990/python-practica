
Empleados = __import__("Empleados").Empleados
EmpleadoTiempoCompleto = __import__("EmpleadoTiempoCompleto").EmpleadoTiempoCompleto
EmpleadoPorHora = __import__("EmpleadoPorHora").EmpleadoPorHora

empleado1 = EmpleadoTiempoCompleto( "E001","Carlos Martínez", 3000000)
empleado2 = EmpleadoPorHora("E002","Ana López", 0, 15000, 160)

print("=== EMPLEADOS DE LA EMPRESA ===")

print(f"\n--- Empleado 1 ---")
print(f"Nombre: {empleado1.get_nombre()}")
print(f"ID: {empleado1.get_empleado()}")
print(f"Tipo: Tiempo Completo")
print(f"Salario base: ${empleado1.get_salarioBase():,}")
print(f"Salario calculado: ${empleado1.calcular_salario():,}")

print(f"\n--- Empleado 2 ---")
print(f"Nombre: {empleado2.get_nombre()}")
print(f"ID: {empleado2.get_empleado()}")
print(f"Tipo: Por Horas")
print(f"Tarifa por hora: ${empleado2.get_tarifa_hora():,}")
print(f"Horas trabajadas: {empleado2.get_horas_trabajadas()}")
print(f"Salario calculado: ${empleado2.calcular_salario():,}")