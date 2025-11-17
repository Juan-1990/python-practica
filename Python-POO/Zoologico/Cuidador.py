class Cuidador:
    def __init__(self, nombre_cuidador, years_exp):
        self.nombre_cuidador = nombre_cuidador
        self.years_exp = years_exp
    
    def set_nombre_cuidador(self, nombre_cuidador):
        self.nombre_cuidador = nombre_cuidador

    def set_years_exp(self, years_exp):
        self.years_exp = years_exp
    
    def get_nombre_cuidador(self):
        return self.nombre_cuidador
    
    def get_years_exp(self):
        return self.years_exp
    
    def cuidar_animal(self):
     print(f"{self.nombre_cuidador} está cuidando a los animales")