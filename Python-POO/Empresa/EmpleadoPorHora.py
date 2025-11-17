from Empleados import Empleados

class EmpleadoPorHora(Empleados):
    def __init__(self, nombre, empleado_id, salarioBase, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, empleado_id, salarioBase)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas
    
    def set_tarifa_hora(self, tarifa_hora):
        self.tarifa_hora = tarifa_hora
    
    def set_horas_trabajadas(self, horas_trabajadas):
        self.horas_trabajadas = horas_trabajadas
    
    def get_horas_trabajadas(self):
        return self.horas_trabajadas
    
    def get_tarifa_hora(self):
        return self.tarifa_hora
    
    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas
