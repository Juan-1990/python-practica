Jugadores = __import__("Jugadores").Jugadores
Equipo = __import__("EquipoFutbol").EquipoFutbol

jugador1 = Jugadores("Cristiano Ronaldo", "Delantero", 39, 7)
jugador2 = Jugadores("Sergio Ramos", "Defensa", 38, 4)
jugador3 = Jugadores("Vinicius Jr", "Delantero", 24, 20)
    
equipo = Equipo("Real Madrid", "Madrid", "Carlo Ancelotti")
equipo.agregar(jugador1)

equipo.agregar(jugador2)

equipo.agregar(jugador3)
    
equipo.mostrar()
    
equipo.remover(jugador2)

jugador2.transferir()
    
equipo.mostrar()