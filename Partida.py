from Jugador import Jugador

class Partida:

    def __init__(self):
        self.jugadores = []

    def info_jugadores(self):
        colores = ["rojo", "azul", "amarillo", "negro", "verde"]
        num_fichas = 72
        while 1:
           num_jugs = int(raw_input("Inserte numero de jugadores (maximo 5): "))
           if num_jugs > 5:
              print "Eres un poco tonto, prueba otra vez."
           else:
              break

        for i in range(1,num_jugs+1):
           nombre_jug = raw_input("Nombre jugador " + str(i) + ": ")
           while 1:
              color = raw_input("Color jugador " + str(i) + ": ").lower()
              if color not in colores:
                 print "Color invalido. Colores disponibles: " + ", ".join(colores)
              else:
                 colores.remove(color)
                 jug = Jugador(nombre_jug,color)
                 self.jugadores.append(jug)
                 break

    def pasar_turno(self, jugador):
        """
        Devuelve el siguiente jugador del array de jugadores.
        Si es el ultimo del array, devolvera el jugador de la primera posicion.
        """
        jugador.turno = False #ya se ha acabado el turno del jugador y tenemos que pasarselo al siguiente de la lista
        for i in range(4):
            if self.jugadores[i] == jugador: #hemos encontrado la posicion de ese jugador
                if i == len(self.jugadores)-1: #si la posicion corresponde al ultimo jugador de la lista
                    self.jugadores[0].turno = True #el turno vuelve al primero
                    return self.jugadores[0]
                else:
                    self.jugadores[i+1].turno = True #si no es el turno del siguiente jugador de la lista
                    return self.jugadores[i+1]
