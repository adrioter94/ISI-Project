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


    def pos_valida(self, pos_validas, pos):
        # Devuelve True si la pos pasada como parametro se encuentra dentro del array pos_validas
        response = False
        for i in pos_validas:
            if str(i) != pos:
                continue
            else:
                response = True
        return response


    def elegir(self, pos_validas, eleccion=None):
        #Comprueba que la eleccion del jugador en cada turno sea valida,
        #es decir, que elija una posicion valida donde colocar la ficha
        #o girarla.
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

        return eleccion


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
        if ficha.zona[indice] != 'v' and ficha.zona[indice] != 'r' and ficha.zona[indice] != 'a' \
        and ficha.zona[indice] != 'n' and ficha.zona[indice] != 'y' and ficha.zona[indice] != '0':
            numero_zona=ficha.zona[indice] #la zona donde hemos colocado la ficha
            ficha.pintar_ficha(numero_zona,seguidor)
            jugador.seguidores -= 1
        return ficha

    def actualizar_zona(self, ficha, posicion):
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
                if u.zona[6 + i] in colores:
                    zona1 = ficha.zona[3 + i]
                    if zona1 in colores:
                        return
                    ficha.pintar_ficha(zona1,u.zona[6 + i])
                i += 1
        i = 0
        if b.territorio[0][1] != '-':
            while i < 3:
                if b.zona[3 + i] in colores:
                    zona1 = ficha.zona[6 + i]
                    if zona1 in colores:
                        return
                    ficha.pintar_ficha(zona1,b.zona[3 + i])
                i += 1
        i = 0
        if r.territorio[0][1] != '-':
            while i < 3:
                if r.zona[12 + i] in colores:
                    zona1 = ficha.zona[9 + i]
                    if zona1 in colores:
                        return
                    ficha.pintar_ficha(zona1,r.zona[12 + i])
                i += 1
        i = 0
        if l.territorio[0][1] != '-':
            while i < 3:
                if l.zona[9 + i] in colores:
                    zona1 = ficha.zona[12 + i]
                    if zona1 in colores:
                        return
                    ficha.pintar_ficha(zona1,l.zona[9 + i])
                i += 1


    def algoritmo_relleno(self,x, y):
        #Pinta las zonas de las fichas del tablero que corresponda al poner un seguidor
        #en una ficha.
        if self.tablero.tablero[x][y].territorio[0][1] == '-' or self.tablero.tablero[x][y].pintada == True : # the base case
            return
        self.actualizar_zona(self.tablero.tablero[x][y],(x,y))
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

    def jugar_turno(self, jugador):
        #Cada vez que sea el turno de un jugador:
        #1)  Sacara una ficha del saco.
        #2)  Se comprobara si esa ficha se puede colocar en el tablero, si no se puede se sacara otra ficha.
        #3)  Si se puede colocar en alguna posicion del tablero, se le mostrara al jugador para que elija
        #    las posiciones disponibles para esa ficha colocada tal cual esta, o bien puede elegir 'Girarla'.
        #4)  Si elige 'Girarla', de nuevo se recalcularan las posiciones en las que se puede colocar esa ficha
        #    girada y se le mostraran para que elija entre las posiciones disponibles, o 'Girarla' de nuevo.
        #5)  En el momento en el que elija colocar la ficha en una de las posiciones mostradas, se recalcularan
        #    las posiciones de los seguidores para esa ficha teniendo en cuenta la posicion que ocupa dentro del
        #    tablero (p.e. no se pueden poner dos granjeros del mismo jugador dentro de la misma pradera).
        #6)  Con las posiciones posibles de los seguidores actualizadas, se le da al jugador la posibilidad de
        #    colocar un seguidor en su turno, si dispone de seguidores para colocar.
        #7)  Se comprobara si hay que sumarle puntos al jugador en ese turno.
        #8)  El turno pasara al siguiente jugador.

        while len(self.saco) <= 71:
            ficha = self.saco.sacar_ficha()
            if not self.tablero.comprobacion_ficha_valida(ficha): #valida para todos los giros en todas las posiciones que hay disponibles
                continue
            while True:
                pos_validas = self.tablero.todas_pos_validas(ficha) #posiciones validas para una posicion concreta (NO todos los giros)
                eleccion = self.elegir(pos_validas) #pinta las posiciones validas y 'Girar' para que el jugador elija
                if eleccion == 'G':
                    ficha.girar()
                    continue
                elif eleccion not in pos_validas:
                    print "No hay ninguna posicion valida que coincida con tu eleccion."
                    continue
                self.actualizar_zona(ficha, eleccion)
                self.saco.eliminar_ficha(ficha)
                if jugador.seguidores != 0:
                    ficha = self.colocar_seguidores(ficha, jugador) #te devuelve una ficha con el vector pos_seguidores actualizado
                self.tablero.insertar(eleccion[0], eleccion[1], ficha)
                self.algoritmo_relleno(eleccion[0],eleccion[1])
                #self.computar_puntos_turno(tablero, ficha, jugador)
                next_jugador = self.pasar_turno(jugador)
                break
            self.jugar_turno(next_jugador)
