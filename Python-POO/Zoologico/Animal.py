class Animal:
    def __init__(self,nombre,edad,especie):
        self.nombre=nombre
        self.edad=edad
        self.especie=especie

    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_edad(self,edad):
        self.edad=edad
    
    def set_especie(self,especie):
        self.especie=especie

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_especie(self):
        return self.especie

    def hacer_sonido(self):
     print(f"{self.nombre} hace un sonido")

    def comer(self):
     print(f"{self.nombre} está comiendo")