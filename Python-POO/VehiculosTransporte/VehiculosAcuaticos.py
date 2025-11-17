from Vehiculos import Vehiculos

class VehiculosAcuaticos(Vehiculos):
    def __init__(self, marca, modelo, capacidad, tipo_compulsion):
        super().__init__(marca, modelo, capacidad)
        self._tipo_compulsion = tipo_compulsion

    def set_tipo_compulsion(self, tipo_compulsion):
        self._tipo_compulsion = tipo_compulsion

    def get_tipo_compulsion(self):
        return 
    
    def manejar(self):
        print(f"Navegando el {self._marca} {self._modelo}")

    def anclar(self):
        print(f"Anclando el {self._marca} {self._modelo}")

    def moverse(self):
        print(f"El {self._marca} {self._modelo} navega usando {self._tipo_compulsion}")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de propulsion {self._tipo_compulsion}")