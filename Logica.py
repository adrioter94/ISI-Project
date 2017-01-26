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
        lados = ["arriba", "derecha", "abajo", "izquierda"]
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
