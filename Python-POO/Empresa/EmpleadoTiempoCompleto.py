from Empleados import Empleados

class EmpleadoTiempoCompleto(Empleados):

    def __init__(self, empleado_id, nombre, salarioBase):
        super().__init__(empleado_id, nombre, salarioBase)
    
    def calcular_salario(self):
            return self._salarioBase

    def set_salarioFijo(self, salarioFijo):
        self._salarioFijo = salarioFijo

    def get_salarioFijo(self):
        return self._salarioFijo