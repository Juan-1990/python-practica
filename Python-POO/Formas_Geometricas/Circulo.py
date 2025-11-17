import math
from Forma import Forma

class Circulo(Forma):

    def __init__(self, color, radio):
        super().__init__(color)
        self._radio = radio
        self.calcularArea()
    
    def get_radio(self):
        return self._radio
    
    def set_radio(self, radio):
        self._radio = radio
        self.calcularArea()  
    
    def calcularArea(self):
        
        #Calcula el área del círculo usando la fórmula: π * r²
        
        self._area = math.pi * (self._radio ** 2)
        return self._area
    
    def mostrar_info(self):

        print(f"\n=== CÍRCULO ===")
        print(f"Color:  {self._color}")
        print(f"Radio:  {self._radio} unidades")
        print(f"Area:   {self._area:.2f} unidades²")
        print(f"Perímetro: {2 * math.pi * self._radio:.2f} unidades")
        print("=" * 30)