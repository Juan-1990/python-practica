class Automovil:

    def __init__(self, marca, modelo, anio, color, motor):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._color = color
        self._motor = motor

    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_anio(self, anio):
        self._anio = anio
    
    def set_color(self, color):
        self._color = color

    def get_marca(self):
        return self._marca
    
    def get_modelo(self):
        return self._modelo

    def get_anio(self):
        return self._anio
    
    def get_color(self):
        return self._color
    
    def get_motor(self):
        return self._motor
    
    def encender(self):
        print(f"Encendiendo {self._marca} {self._modelo}...")
        self._motor.prender()
    
    def apagar(self):
        print(f"Apagando {self._marca} {self._modelo}...")
        self._motor.apagar()
    
    def acelerar(self):
        print(f"Acelerando {self._marca} {self._modelo}...")
        self._motor.acelerar()
    
    def mostrar_info(self):
        print(f"\n--- Información del Automóvil ---")
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"Año: {self._anio}")
        print(f"Color: {self._color}")
        print(f"Motor: {self._motor.get_cilindraje()}cc, {self._motor.get_tipoCombustible()}, {self._motor.get_potencia()} HP")