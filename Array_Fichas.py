from Fichas import Fichas

class ArrayFichas:
	def __init__(self):
		self.fichas = []
		self.fichas.append(Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A'))
		self.fichas.append(Fichas('X','P','C','P','P','C','P','P','C','P','P','C','P'))
		for i in range(4):
			self.fichas.append(Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A'))
		for i in range(3):
			self.fichas.append(Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A'))
		for i in range(5):
			self.fichas.append(Fichas('P','A','A','A','P','P','P','A','A','A','P','P','P'))
		for i in range(2):
			self.fichas.append(Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A'))
		for i in range(3):
			self.fichas.append(Fichas('P','P','P','P','P','P','P','A','A','A','A','A','A'))
		for i in range(5):
			self.fichas.append(Fichas('P','A','A','A','P','P','P','P','P','P','P','P','P'))
		for i in range(3):
			self.fichas.append(Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A'))
		for i in range(5):
			self.fichas.append(Fichas('P','A','A','A','P','C','P','P','C','P','A','A','A'))
		for i in range(2):
			self.fichas.append(Fichas('I','P','P','P','P','C','P','P','P','P','P','P','P'))
		for i in range(3):
			self.fichas.append(Fichas('P','A','A','A','P','C','P','P','C','P','P','P','P'))
		for i in range(3):
			self.fichas.append(Fichas('P','A','A','A','P','C','P','P','P','P','P','C','P'))
		for i in range(3):
			self.fichas.append(Fichas('X','A','A','A','P','C','P','P','C','P','P','C','P'))
		for i in range(4):
			self.fichas.append(Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P'))
		for i in range(4):
			self.fichas.append(Fichas('I','P','P','P','P','P','P','P','P','P','P','P','P'))
		for i in range(9):
			self.fichas.append(Fichas('C','P','P','P','P','C','P','P','P','P','P','C','P'))
		for i in range(8):
			self.fichas.append(Fichas('C','P','C','P','P','C','P','P','P','P','P','P','P'))
		for i in range(4):
			self.fichas.append(Fichas('X','P','P','P','P','C','P','P','C','P','P','C','P'))

	def imprimir(self):
		resultado = ''
		i = 0
		while i < 23:
			resultado += str(self.fichas[i].imprimir())
			i = i + 1
		return resultado
