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

if __name__ == '__main__':
    p = Partida()
    p.info_jugadores()
    #for i in range (0, len(p.jugadores)):
    #    print p.jugadores[i].imprimir()
