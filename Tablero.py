
class Tablero:

	def __init__(self):
		"""
		Construye una matriz y la rellena con fichas de tipo vacia.
		"""


    def insertar(self, ficha, x, y):
		"""
		Inserta una ficha en una posición dada por sus dos coordenadas x e y.
		"""


    def es_valida(self, ficha, x, y):
		"""
		Devuelve True si una ficha es válida en una posición del tablero
		(dada por sus coordenadas x e y) en una orientación dada.
		"""


    def todas_pos_validas(self, ficha):
		"""
		Devuelve un array con todas las posiciones válidas en el tablero
		para una ficha en una orientación dada.
		"""


    def comprobación_ficha_valida(self, ficha):
        """
		Devuelve True si hay al menos una posición válida a lo largo de todo
		el tablero para todas las orientaciones de la ficha en cada posición
		(para descartarla directamente).
		"""


    def imprimir(self):
		"""
		Imprime el tablero en la situación actual.
		"""
