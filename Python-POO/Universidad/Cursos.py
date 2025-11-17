class Curso:
    def __init__(self, nombre, codigo, numCreditos):
        self._nombre = nombre
        self._codigo = codigo
        self._numCreditos = numCreditos
        self._estudiantes = []

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_numCreditos(self, numCreditos):
        self._numCreditos = numCreditos

    def get_nombre(self):
        return self._nombre
    
    def get_codigo(self):
        return self._codigo
    
    def get_numCreditos(self):
        return self._numCreditos
    
    def agregarEstudiante(self, estudiante):
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)
            if self not in estudiante.cursosMatriculados:
                estudiante.cursosMatriculados.append(self)

