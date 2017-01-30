from Jugador import Jugador
from Array_Fichas import ArrayFichas
from Tablero import Tablero
import sys

class Partida:

    def __init__(self):
        self.jugadores = []
        self.tablero = Tablero()
        self.saco = ArrayFichas()

    def info_jugadores(self,num_jugs,jug1,col1,jug2,col2,jug3=None,col3=None,jug4=None,col4=None,jug5=None,col5=None):
        #Rellena el array de jugadores con los valores para cada uno
        color_recibido=[]
        nombre_jug=[]
        colores = ["rojo", "azul", "amarillo", "negro", "verde"]

        # anade colores != None
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

        # anade jugadores != None
        if jug1 != None:
            nombre_jug.append(jug1)
        if jug2 != None:
            nombre_jug.append(jug2)
        if jug3 != None:
            nombre_jug.append(jug3)
        if jug4 != None:
            nombre_jug.append(jug4)
        if jug5 != None:
            nombre_jug.append(jug5)

        num_fichas = 72


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
        #Devuelve el siguiente jugador del array de jugadores.
        #Si es el ultimo del array, devolvera el jugador de la primera posicion.
        jugador.turno = False #ya se ha acabado el turno del jugador y tenemos que pasarselo al siguiente de la lista
        for i in range(4):
            if self.jugadores[i] == jugador: #hemos encontrado la posicion de ese jugador
                if i == len(self.jugadores)-1: #si la posicion corresponde al ultimo jugador de la lista
                    self.jugadores[0].turno = True #el turno vuelve al primero
                    return self.jugadores[0]
                else:
                    self.jugadores[i+1].turno = True #si no es el turno del siguiente jugador de la lista
                    return self.jugadores[i+1]


    def colocar_seguidor(self,ficha,jugador,indice):
        #coloca un seguidor del color del jugador que se le pasa como parametro
        #si en esa posicion se puede colocar un seguidor
        seguidor=""
        if jugador.color == "verde":
            seguidor = 'v'
        if jugador.color == "rojo":
            seguidor = 'r'
        if jugador.color == "azul":
            seguidor = 'a'
        if jugador.color == "negro":
            seguidor = 'n'
        if jugador.color == "amarillo":
            seguidor = 'y'
        if ficha.zonas[indice] != 'v' and ficha.zonas[indice] != 'r' and ficha.zonas[indice] != 'a' \
        and ficha.zonas[indice] != 'n' and ficha.zonas[indice] != 'y' and ficha.zonas[indice] != '0':
            numero_zonas=ficha.zonas[indice] #la zona donde hemos colocado la ficha
            ficha.pintar_ficha(numero_zonas,seguidor)
            jugador.seguidores -= 1
        return ficha

    def actualizar_zonas(self, ficha, posicion):
        #Actualiza las zonas de una ficha con el color que corresponda
        #cuando se vaya a poner en una posicion dada del tablero.
        i = 0
        colores = ['r', 'a', 'y', 'n', 'v']
        x = posicion[0]
        y = posicion[1]
        u = self.tablero.tablero[x-1][y] #up
        b = self.tablero.tablero[x+1][y] #bottom
        r = self.tablero.tablero[x][y+1] #right
        l = self.tablero.tablero[x][y-1] #left

        if u.territorio[0][1] != '-':
            while i < 3:
                if u.zonas[6 + i] in colores:
                    zona1 = ficha.zonas[3 + i]
                    if zona1 in colores:
                        pass
                    else:
                        ficha.pintar_ficha(zona1,u.zonas[6 + i])
                i += 1
        i = 0
        if b.territorio[0][1] != '-':
            while i < 3:
                if b.zonas[3 + i] in colores:
                    zona1 = ficha.zonas[6 + i]
                    if zona1 in colores:
                        pass
                    else:
                        ficha.pintar_ficha(zona1,b.zonas[3 + i])
                i += 1
        i = 0
        if r.territorio[0][1] != '-':
            while i < 3:
                if r.zonas[12 + i] in colores:
                    zona1 = ficha.zonas[9 + i]
                    if zona1 in colores:
                        pass
                    else:
                        ficha.pintar_ficha(zona1,r.zonas[12 + i])
                i += 1
        i = 0
        if l.territorio[0][1] != '-':
            while i < 3:
                if l.zonas[9 + i] in colores:
                    zona1 = ficha.zonas[12 + i]
                    if zona1 in colores:
                        pass
                    else:
                        ficha.pintar_ficha(zona1,l.zonas[9 + i])
                i += 1


    def algoritmo_relleno(self,x, y):
        #Pinta las zonas de las fichas del tablero que corresponda al poner un seguidor
        #en una ficha.
        if self.tablero.tablero[x][y].territorio[0][1] == '-' or self.tablero.tablero[x][y].pintada == True : # the base case
            return
        self.actualizar_zonas(self.tablero.tablero[x][y],(x,y))
        self.tablero.tablero[x][y].pintada = True
        self.algoritmo_relleno(x - 1, y) # arriba
        self.algoritmo_relleno(x + 1, y) # abajo
        self.algoritmo_relleno(x, y + 1) # derecha
        self.algoritmo_relleno(x, y - 1) # izquierd

    def pintada_false(self):
        #Metodo que se utiliza junto a algoritmo_relleno
        i = 0
        z = 0
        while i < self.tablero.w:
            while z < self.tablero.h:
                self.tablero.tablero[i][z].pintada = False
                z = z + 1
            i = i + 1
            z = 0

    def jugar_turno(self, jugador, posicion_elegida, quiere_seguidor, ficha, posicion_seguidor=None):
        #Cada vez que sea el turno de un jugador:
        #1)  La idea es hacer un test llamando a este metodo 72 veces porque hay 72 piezas y nosotros le vamos pasando
		# la posicion elegida a mano que en caso de juego original nos la tandria que pasar la interfaz grafica,
		# y la ficha que nos pasaria tendria que ser valida porque la interfaz grafica se encargara de probar que es valida
        # esa ficha antes de mostrarla y la posicion que nos pase tambien tiene que ser valida porque la interfaz
        # grafica solo nos deberia dejar poner la ficha en posiciones validas.
        # Si el jugador quiere girar la ficha deberia tener un boton la interfaz grafica que se
        # encarge de girar la ficha llamando al metodo girar de la clase ficha y ya nos pasaria la ficha a este metodo
        #
        #Y luego si quiere colocar seguidor que nos pase un "SI" o un "NO" en la variable quiere_seguidor
		# en el caso de que sea que "SI" que nos pase tambien su posicion.
        pos_validas = self.tablero.todas_pos_validas(ficha) #posiciones validas para una posicion concreta (NO todos los giros)
        if posicion_elegida in pos_validas:
            self.actualizar_zonas(ficha, posicion_elegida)
            self.saco.eliminar_ficha(ficha)
            if jugador.seguidores != 0:
                if quiere_seguidor == "SI":
                    self.colocar_seguidor(ficha, jugador,posicion_seguidor)
            self.tablero.insertar(ficha,posicion_elegida[0], posicion_elegida[1])
            self.algoritmo_relleno(posicion_elegida[0], posicion_elegida[1])
            self.pintada_false()
            return "OK"
        return "ERROR"
