from Array_Fichas import ArrayFichas
import copy

class Tablero:

    def __init__(self):

        #Construye una matriz y la rellena con fichas de tipo vacia.
        #La matriz funciona con un margen de una fila por cada lado
    	self.w = 6
        self.h = 6
        ficha = ArrayFichas().vacia
        self.tablero = [[ficha for y in range(0,self.w)] for x in range(0,self.h)]

    def insertar(self, ficha, x, y):

        #Inserta una ficha en una posicion dada por sus dos coordenadas x e y.

        self.tablero[x][y] = ficha


    def es_valida(self, ficha, x, y):

	    #Devuelve True si una ficha es valida en una posicion del tablero
	    #(dada por sus coordenadas x e y) en una orientacion dada.

        u = self.tablero[x-1][y].territorio[2][1] #up
        b = self.tablero[x+1][y].territorio[1][1] #bottom
        r = self.tablero[x][y+1].territorio[4][1] #right
        l = self.tablero[x][y-1].territorio[3][1] #left
        if u == '-' and b == '-' and \
            r == '-' and l == '-':
            return False
        elif (u == ficha.territorio[1][1] or u == '-') and \
            (b == ficha.territorio[2][1] or b == '-') and \
            (r == ficha.territorio[3][1] or r == '-') and \
            (l == ficha.territorio[4][1] or l == '-'):
            return True
        else:
            return False


    def todas_pos_validas(self, ficha):

		#Devuelve un array con todas las posiciones validas en el tablero
		#para una ficha en una orientacion dada.

        pos_validas = []
        for y in range(1,self.w-1):
            for x in range(1,self.h-1):
                if self.es_valida(ficha, x, y):
                    pos = [x, y]
                    pos_validas.append(pos)
        return pos_validas


    def comprobacion_ficha_valida(self, ficha):

		#Devuelve True si hay al menos una posicion valida a lo largo de todo
		#el tablero para todas las orientaciones de la ficha en cada posicion
		#(para descartarla directamente).
        ficha_aux = copy.deepcopy(ficha)  # de la ficha (para descartarla diretamente)
        i = 1
        while i <= 4:
            ficha_aux.girar()
            for y in range(1,self.w-1):
                for x in range(1,self.h-1):
                    if self.es_valida(ficha_aux, x, y):
                        return True
            i += 1
        return False


    def imprimir(self):

		#Imprime el tablero en la situacion actual.
        pass
