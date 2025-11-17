from Animal import Animal
class Mamifero (Animal):
    def __init__(self,nombre,edad,especie,tipo_pelaje):
          super().__init__(nombre, edad, especie)
          self.tipo_pelaje = tipo_pelaje
    
    def set_tipo_pelaje(self, tipo_pelaje):
        self.tipo_pelaje = tipo_pelaje
    def get_tipo_pelaje(self):
        return self.tipo_pelaje
    def amamantar(self):
      print(f"{self.nombre} está amamantando a sus crías")

