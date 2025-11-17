class Jugadores:
    def __init__(self,nombre,edad,posicion,NumCamisa):
        self.nombre=nombre
        self.edad=edad
        self.posicion=posicion
        self.NumCamisa=NumCamisa
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_posicion(self, posicion):
        self.posicion = posicion
    def set_edad(self, edad):
        if edad > 0:
            self.edad = edad
        else:
            print("Error: La edad debe ser positiva")
    def set_NumCamisa(self, NumCamisa):
        self.NumCamisa= NumCamisa
    def transferir(self):
        
        print(f"{self.nombre} ha sido transferido")
    
    def __str__(self):
        return f"#{self.NumCamisa} - {self.nombre} ({self.posicion}) - {self.edad} años"
    def get_nombre(self):
        return self.nombre
    def get_posicion(self):
        return self.posicion
    def get_edad(self):
        return self.edad
    def get_Numcamisa(self):
        return self.NumCamisa