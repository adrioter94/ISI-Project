
class Tablero:
	def __init__(self):
		self.tablero = [None] * 72 #numero de filas
		for i in range(72): #numero de filas
			self.tablero[i] = ['X'] * 72 #numero de columnas


	def imprimir_tablero(self):
		i=0
		resultado = ""
		for fila in self.tablero:
			while i < 72:
				resultado += str(fila[i])
				i = i + 1
			i = 0
			resultado += "\n"
		return resultado
	
