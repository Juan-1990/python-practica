class Motor:
    def __init__(self, cilindraje, tipoCombustible, potencia):
        self._cilindraje = cilindraje
        self._tipoCombustible = tipoCombustible
        self._potencia = potencia
        self._encendido = False

    def set_cilindraje(self, cilindraje):
        self._cilindraje = cilindraje
        
    def set_tipoCombustible(self, tipoCombustible):
        self._tipoCombustible = tipoCombustible

    def set_potencia(self, potencia):
        self._potencia = potencia

    def get_cilindraje(self):
        return self._cilindraje 
    
    def get_tipoCombustible(self):
        return self._tipoCombustible
    
    def get_potencia(self):
        return self._potencia
    
    def esta_encendido(self):
        return self._encendido
    
    def prender(self):
       if not self._encendido:
           self._encendido = True
           print(f"Motor de {self._cilindraje}cc encendido con {self._tipoCombustible}")
           return True
       else: 
           print("El motor esta encendido")
           return False
       
    def acelerar(self):
        if not self._encendido:
            print("No se puede acelerar. el motor esta apagado")
            return
        if self._potencia <= 80:
            print(f"El motor tiene una potencia baja de {self._potencia} HP")
        elif self._potencia <= 200:
            print(f"El motor tiene una potencia media de {self._potencia} HP")
        else:
            print(f"El motor tiene una potencia alta de {self._potencia} HP")
        
    def apagar(self):
        if self._encendido:
            self._encendido = False 
            print("Motor apagado")
            return True

        else:
            print("El motor ya esta apagado")
            return False