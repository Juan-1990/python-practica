class EquipoFutbol:
    def __init__(self, nombre, ciudad, entrenador):
        self.nombre = nombre
        self.ciudad = ciudad
        self.entrenador = entrenador
        self.jugadores = []
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_ciudad(self, ciudad):
        self.ciudad = ciudad
    
    def set_entrenador(self, entrenador):
        self.entrenador = entrenador
    
    def set_jugadores(self, jugadores):
        self.jugadores = jugadores
    
    def get_nombre(self):
        return self.nombre
    
    def get_ciudad(self):
        return self.ciudad
    
    def get_entrenador(self):
        return self.entrenador
    
    def get_jugadores(self):
        return self.jugadores
    
    def agregar(self, jugador):
        self.jugadores.append(jugador)
    
    def remover(self, jugador):
        self.jugadores.remove(jugador)
    
    def mostrar(self):
        print(f"\nEquipo: {self.nombre}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Entrenador: {self.entrenador}")
        print("Jugadores:")
        for jugador in self.jugadores:
            print(f"  {jugador}")