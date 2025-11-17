from abc import ABC, abstractmethod

class Forma(ABC):

    def __init__(self, color):
        self._color = color
        self._area = 0.0
    
    # Getter y Setter para color
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
    
    # Getter para área
    def get_area(self):
        return self._area
    
    # Método abstracto que debe ser implementado por las clases hijas
    @abstractmethod
    def calcularArea(self):
        """
        Método abstracto para calcular el área.
        Debe ser implementado por cada forma específica.
        """
        pass
    
    # Método para mostrar información básica
    def mostrar_info(self):
        """
        Muestra información básica de la forma.
        Puede ser sobrescrito por las clases hijas.
        """
        print(f"Forma de color: {self._color}")
        print(f"Area: {self._area:.2f} unidades²")