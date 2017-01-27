from Array_Fichas import ArrayFichas
from Tablero import Tablero
from Fichas import Fichas

class Logica:

    def __init__(self):
        self.array_caminos = []
        self.array_aldeas = []


    def contiene_camino(self, ficha):
        return ArrayFichas().type(ficha) in [10, 15, 16, 17, 18]


    def contiene_aldea(self, ficha):
        return ArrayFichas().type(ficha) in [1, 2, 3, 4, 5, 6, 7]


    def contiene_camino_y_aldea(self, ficha):
        return ArrayFichas().type(ficha) in [8, 9, 11, 12, 13, 14]


    def no_camino_no_aldea(self, ficha):
        return ArrayFichas().type(ficha) == 19


    def es_bifurcacion(self, ficha):
        return ArrayFichas().type(ficha) in [13, 15, 16]


    def es_limite_camino(self, ficha):
        return ArrayFichas().type(ficha) in [8, 10, 13, 15, 16]


    def que_ficha_es(self, ficha):
        if self.contiene_camino(ficha) and not self.es_bifurcacion(ficha):
            return "con_C"
        if self.contiene_aldea(ficha):
            return "con_A"
        if self.contiene_camino_y_aldea(ficha):
            return "con_CA"
        if self.no_camino_no_aldea(ficha):
            return "sin_CA"
        if self.es_bifurcacion(ficha):
            return "con_B"


    def dame_pos_contiguas(self, x, y):
        #Devuelve dos arrays con las posiciones de las fichas contiguas y sus direcciones
        pos_contiguas = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        lados = ["arriba", "abajo", "derecha", "izquierda"]
        return (pos_contiguas, lados)


    def dame_camino(self, pos):
        #Devuelve el camino dentro del array de todos los caminos
        #en el que se encuentre la posicion pasada como parametro
        for camino in self.array_caminos:
            if pos in camino:
                return camino #devolvemos el camino que contenga la posicion


    def dame_aldea(self, pos):
        #Devuelve la aldea dentro del array de todas las aldeas
        #en el que se encuentre la posicion pasada como parametro
        for aldea in self.array_aldeas:
            if pos in aldea:
                return aldea #devolvemos la aldea que contenga la posicion


    def continua_camino(self, tablero, pos, pos_contigua, lado): #lado: arriba,abajo,dcha,izda
        #Comprueba si la ficha que estamos colocando y una de las fichas contiguas
        #forman un mismo camino
        ficha_contigua = tablero.dame_ficha(pos_contigua)
        ficha_actual = tablero.dame_ficha(pos)
        response = False
        if lado == "arriba":
            if ficha_actual.territorio[1][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[1][1] == ficha_contigua.territorio[2][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "abajo":
            if ficha_actual.territorio[2][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[2][1] == ficha_contigua.territorio[1][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "derecha":
            if ficha_actual.territorio[3][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[3][1] == ficha_contigua.territorio[4][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "izquierda":
            if ficha_actual.territorio[4][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[4][1] == ficha_contigua.territorio[3][1]: #si la ficha contigua no es vacia
                    response = True
        return response


    def continua_aldea(self, tablero, pos, pos_contigua, lado): #lado: arriba,abajo,izda,dcha
        #Comprueba si la ficha que estamos colocando y una de las fichas contiguas
        #forman una misma aldea
        ficha_contigua = tablero.dame_ficha(pos_contigua)
        ficha_actual = tablero.dame_ficha(pos)
        response = False
        if lado == "arriba":
            if ficha_actual.territorio[1][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[1][1] == ficha_contigua.territorio[2][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "abajo":
            if ficha_actual.territorio[2][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[2][1] == ficha_contigua.territorio[1][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "derecha":
            if ficha_actual.territorio[3][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[3][1] == ficha_contigua.territorio[4][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "izquierda":
            if ficha_actual.territorio[4][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[4][1] == ficha_contigua.territorio[3][1]: #si la ficha contigua no es vacia
                    response = True
        return response


    def coloca_ficha_con_C(self, tablero, pos):
        #Busca si la ficha pertenece a algun camino existente
        #Si pertenece a un camino, incluye la posicion de la ficha en ese camino
        #Si pertenece a caminos inconexos, los une en un mismo camino
        #Si no pertence a ningun camino, crea un nuevo camino con la posicion de la ficha
        posiciones = [] #array en el que se iran agregrando las posiciones contiguas al camino
        pos_contiguas = self.dame_pos_contiguas(pos[0], pos[1])[0]
        lados = self.dame_pos_contiguas(pos[0], pos[1])[1]

        #Guardamos en posiciones las fichas adyacentes que continuen el camino
        for i in range(len(lados)):
            if self.continua_camino(tablero, pos, pos_contiguas[i], lados[i]): #si pertenece a un camino existente
                posiciones.append(pos_contiguas[i]) #agregamos esa posicionflag = False #es continuacion de un camino existente

        if posiciones == []: #no pertenece a un camino existente
            self.array_caminos.append([pos])
        elif len(posiciones) == 2: #pertenece a dos caminos que estaban inconexos
            camino1 = self.dame_camino(posiciones[0])
            camino2 = self.dame_camino(posiciones[1])
            self.array_caminos.remove(camino1) #eliminamos los antiguos caminos
            self.array_caminos.remove(camino2)
            camino1.append(pos)
            for elem in camino2:
                camino1.append(elem)
            self.array_caminos.append(camino1) #agregamos el camino completo
        else: #pertence a un solo camino existente
            camino = self.dame_camino(posiciones[0]) #busco el camino al que pertenece
            self.array_caminos.remove(camino) #eliminamos el antiguo camino
            camino.append(pos)
            self.array_caminos.append(camino) #agregamos el camino completo
