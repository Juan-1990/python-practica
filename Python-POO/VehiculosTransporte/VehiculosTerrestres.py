from Vehiculos import Vehiculos

class VehiculosTerrestres(Vehiculos):
    def __init__(self, marca, modelo, capacidad, num_ruedas):
        super().__init__(marca, modelo, capacidad,)
        self._num_ruedas = num_ruedas

    def set_num_ruedas(self, num_ruedas):
        self._num_ruedas = num_ruedas

    def get_num_ruedas(self):
        return self._num_ruedas
    
    def manejar(self):
        print(f"Manejando el {self._marca} {self._modelo} por carretera")

    def frenar(self):
        print(f"Frenando el {self._marca} {self._modelo}")

    def moverse(self):
        print(f"El {self._marca} {self._modelo} se mueve sobre {self._num_ruedas} ruedas")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Numero de ruedas {self._num_ruedas}")