from Array_Fichas import ArrayFichas
class Tablero:

    def __init__(self):
        """
        Construye una matriz y la rellena con fichas de tipo vacia.
        """
    	self.w = 4
        self.h = 4
        ficha = ArrayFichas().vacia
        self.tablero = [[ficha for y in range(0,self.w)] for x in range(0,self.h)]

    def insertar(self, ficha, x, y):
		"""
		Inserta una ficha en una posicion dada por sus dos coordenadas x e y.
		"""


    def es_valida(self, ficha, x, y):
		"""
		Devuelve True si una ficha es valida en una posicion del tablero
		(dada por sus coordenadas x e y) en una orientacion dada.
		"""


    def todas_pos_validas(self, ficha):
		"""
		Devuelve un array con todas las posiciones validas en el tablero
		para una ficha en una orientacion dada.
		"""


    def comprobacion_ficha_valida(self, ficha):
        """
		Devuelve True si hay al menos una posicion valida a lo largo de todo
		el tablero para todas las orientaciones de la ficha en cada posicion
		(para descartarla directamente).
		"""


    def imprimir(self):
		"""
		Imprime el tablero en la situacion actual.
		"""
