from Forma import Forma

class Rectangulo(Forma):

    def __init__(self, color, largo, ancho):
        super().__init__(color)
        self._largo = largo
        self._ancho = ancho
        self.calcularArea()
    
    def get_largo(self):
        return self._largo
    
    def set_largo(self, largo):
        self._largo = largo
        self.calcularArea()
    
    def get_ancho(self):
        return self._ancho
    
    def set_ancho(self, ancho):
        self._ancho = ancho
        self.calcularArea()
    
    def calcularArea(self):
        self._area = self._largo * self._ancho
        return self._area
    
    def mostrar_info(self):

        print(f"\n=== RECTÁNGULO ===")
        print(f"Color:  {self._color}")
        print(f"Largo:  {self._largo} unidades")
        print(f"Ancho:  {self._ancho} unidades")
        print(f"Area:   {self._area:.2f} unidades²")
        print(f"Perímetro: {2 * (self._largo + self._ancho):.2f} unidades")
        print("=" * 30)
    
    def es_cuadrado(self):
        return self._largo == self._ancho