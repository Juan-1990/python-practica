Curso = __import__("Cursos").Curso
Estudiante = __import__("Estudiante").Estudiante

estudiante1 = Estudiante("Juan Camilo", "E001", "Ingenieria de Software")
estudiante2 = Estudiante("Maria Garcia", "E002", "Administracion de Empresas")

curso1 = Curso("Ingenieria de Software", "C001", 3)
curso2 = Curso("Administracion de Empresas", "C002", 4)

curso1.agregarEstudiante(estudiante1)
curso1.agregarEstudiante(estudiante2)
curso2.agregarEstudiante(estudiante1)

#Impresion

print("===ESTUDIANTES===")
print(f"{estudiante1.nombre} - {estudiante1.codigoEstudiantil}")
print(f"Cursos matriculados: {len(estudiante1.cursosMatriculados)}")

print(f"\n{estudiante2.nombre} - {estudiante2.codigoEstudiantil}")
print(f"Cursos matriculados: {len(estudiante2.cursosMatriculados)}")

print("\n=== CURSOS ===")
print(f"{curso1.get_nombre()} ({curso1.get_codigo()}) - Créditos: {curso1.get_numCreditos()}")
print(f"{curso2.get_nombre()} ({curso2.get_codigo()}) - Créditos: {curso2.get_numCreditos()}")