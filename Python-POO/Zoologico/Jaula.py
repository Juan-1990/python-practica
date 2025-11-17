class Jaula:
    def __init__(self, numero, animales, cuidador):
        self.numero = numero
        self.animales = animales
        self.cuidador = cuidador
    
    def set_numero(self, numero):
        self.numero = numero
    
    def set_animales(self, animales):
        self.animales = animales
    
    def set_cuidador(self, cuidador):
        self.cuidador = cuidador
    def get_numero(self):
        return self.numero
    
    def get_animales(self):
        return self.animales
    
    def get_cuidador(self):
        return self.cuidador
    
    def asignar_animal(self, animal):
        self.animales.append(animal)
        print(f"Animal {animal.get_nombre()} asignado a la jaula")
    
    def asignar_cuidador(self, cuidador):
        self.cuidador = cuidador
        print(f"Cuidador {cuidador.get_nombre_cuidador()} asignado a la jaula")
    
    def retirar_animal(self, animal):
        if animal in self.animales:
            self.animales.remove(animal)
            print(f"Animal {animal.get_nombre()} retirado de la jaula")