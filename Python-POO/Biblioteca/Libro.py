class Libro:
    def __init__(self, titulo, autor, anioPublicacion, numeroPaginas, estado):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacion = anioPublicacion
        self._numeroPaginas = numeroPaginas
        self._estado = estado

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_autor(self, autor):
        self._autor = autor

    def set_anioPublicacion(self, anioPublicacion):
        self._anioPublicacion = anioPublicacion
        
    def set_numeroPaginas(self, numeroPaginas):
        self._numeroPaginas = numeroPaginas

    def set_estado(self, estado):
        self._estado = estado

    def get_titulo(self):
        return self._titulo
        
    def get_autor(self):
        return self.autor
        
    def get_anioPblicacion(self):
        return self._anioPublicacion
        
    def get_numeroPaginas(self):
        return self.numeroPaginas
        
    def get_estado(self):
        return self._estado
        
    def loan(self):
        self._estado = False

    def returnBook(self):
        self._estado = True
