class Empleados:
    def __init__(self, empleado_id, nombre, salarioBase):
        self._empleado_id = empleado_id
        self._nombre = nombre
        self._salarioBase = salarioBase

    def set_empleado(self, empleado_id):
        self._empleado_id = empleado_id
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_salarioBase(self, salarioBase):
        self._salarioBase = salarioBase

    def get_empleado(self):
        return self._empleado_id
    
    def get_nombre(self):
        return self._nombre
    
    def get_salarioBase(self):
        return self._salarioBase
    
    
