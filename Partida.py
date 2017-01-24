from Jugador import Jugador
import sys

class Partida:

    def __init__(self):
        self.jugadores = []

    def info_jugadores(self,num_jugs,jug1,col1,jug2,col2,jug3=None,col3=None,jug4=None,col4=None,jug5=None,col5=None,):
        color_recibido=[]
        colores = ["rojo", "azul", "amarillo", "negro", "verde"]

        if col1 != None :
            color_recibido.append(col1)
        if col2 != None:
            color_recibido.append(col2)
        if col3 !=None:
            color_recibido.append(col3)
        if col4 != None:
            color_recibido.append(col4)
        if col5 != None:
            color_recibido.append(col5)

        nombre_jug=[jug1,jug2,jug3,jug4,jug5]
        num_fichas = 72

        #num_jugs = int(raw_input("Inserte numero de jugadores (maximo 5): "))
        if num_jugs > 5 and num_jugs < 2:
            print "Maximo 5 jugadores, minimo 2 jugadores"
            sys.exit(0)

        for i in range(0,num_jugs):

            if color_recibido[i] not in colores:
                print color_recibido
                print "Color invalido. Colores disponibles: " + ", ".join(colores)
                sys.exit(0)
            else:
                colores.remove(color_recibido[i])
                jug = Jugador(nombre_jug[i],color_recibido[i])
                self.jugadores.append(jug)


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

    # Devuelve True si la pos pasada como parametro se encuentra dentro del array pos_validas
    def pos_valida(self, pos_validas, pos):
       response = False
       for i in pos_validas:
           if str(i) != pos:
               continue
           else:
               response = True
       return response

      
    def elegir(self, pos_validas,eleccion=None):
        error = False
        print "Posiciones Validas: "
        for i in pos_validas:
            print i
        print "Girar (G)"

        while eleccion != "G" and not self.pos_valida(pos_validas, eleccion):
            print "Formatos validos: [x, y] || G. Por favor vuelve a intentarlo."
            print "Posiciones Validas: "
            for i in pos_validas:
                print i
            print "Girar (G)"
            #eleccion = raw_input()
        return eleccion
