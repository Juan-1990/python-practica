from Libro import Libro

Libro1 = Libro("Harry Potter", "JK Rowling", 1997, 450, True)

print(Libro1._titulo)
print(Libro1._autor)
print(Libro1._anoPublicacion)
print(Libro1._numeroPaginas)

Libro1.loan()
print(Libro1.get_estado())

Libro1.returnBook()
print(Libro1.get_estado())