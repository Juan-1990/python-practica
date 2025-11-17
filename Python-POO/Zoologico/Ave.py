from Animal import Animal
class Ave (Animal):
    def __init__(self, nombre, edad, especie, alas):
        super().__init__(nombre, edad, especie)
        self.alas = alas
    
    def set_alas(self, alas):
      self.alas=alas

    def get_alas(self):
        return self.alas

    def volar(self):
         print(f"{self.nombre} está volando")