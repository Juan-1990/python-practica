class Estudiante:
    def __init__(self, nombre, codigoEstudiantil, carrera):
        self.nombre = nombre
        self.codigoEstudiantil = codigoEstudiantil
        self.carrera = carrera
        self.cursosMatriculados = []

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_codigoEstudiantil(self, codigoEstudiantil):
        self._codigoEstudiantil = codigoEstudiantil

    def set_carrera(self, carrera):
        self._carrera = carrera

    def set_cursosMatriculados(self, cursosMatriculados):
        self._cursosMatriculados = cursosMatriculados

    def get_nombre(self):
        return self._nombre
    
    def get_codigoEstudiantil(self):
        return self._codigoEstudiantil
    
    def get_carrera(self):
        return self._carrera
    
    def get_cursosMatriculados(self):
        return self._cursosMatriculados
    
