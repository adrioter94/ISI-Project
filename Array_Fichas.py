from Fichas import Fichas

class ArrayFichas:

	saco = []
	inicial = Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
	tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
	tipo2 = Fichas('X','P','C','P','P','C','P','P','C','P','P','C','P')
	tipo3 = Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A')
	tipo4 = Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A')
	tipo5 = Fichas('P','A','A','A','P','P','P','A','A','A','P','P','P')
	tipo6 = Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A')
	tipo7 = Fichas('P','P','P','P','P','P','P','A','A','A','A','A','A')
	tipo8 = Fichas('P','A','A','A','P','P','P','P','P','P','P','P','P')
	tipo9 = Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A')
	tipo10 = Fichas('P','A','A','A','P','C','P','P','C','P','A','A','A')
	tipo11 = Fichas('I','P','P','P','P','C','P','P','P','P','P','P','P')
	tipo12 = Fichas('P','A','A','A','P','C','P','P','C','P','P','P','P')
	tipo13 = Fichas('P','A','A','A','P','C','P','P','P','P','P','C','P')
	tipo14 = Fichas('X','A','A','A','P','C','P','P','C','P','P','C','P')
	tipo15 = Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
	tipo16 = Fichas('I','P','P','P','P','P','P','P','P','P','P','P','P')
	tipo17 = Fichas('C','P','P','P','P','C','P','P','P','P','P','C','P')
	tipo18 = Fichas('C','P','C','P','P','C','P','P','P','P','P','P','P')
	tipo19 = Fichas('X','P','P','P','P','C','P','P','C','P','P','C','P')



	def __init__(self):
		self.saco.append(self.tipo1)
		self.saco.append(self.tipo2)
		for i in range(4):
			self.saco.append(self.tipo3)
		for i in range(3):
			self.saco.append(self.tipo4)
		for i in range(5):
			self.saco.append(self.tipo5)
		for i in range(2):
			self.saco.append(self.tipo6)
		for i in range(3):
			self.saco.append(self.tipo7)
		for i in range(5):
			self.saco.append(self.tipo8)
		for i in range(3):
			self.saco.append(self.tipo9)
		for i in range(5):
			self.saco.append(self.tipo10)
		for i in range(2):
			self.saco.append(self.tipo11)
		for i in range(3):
			self.saco.append(self.tipo12)
		for i in range(3):
			self.saco.append(self.tipo13)
		for i in range(3):
			self.saco.append(self.tipo14)
		for i in range(3):
			self.saco.append(self.tipo15)
		for i in range(4):
			self.saco.append(self.tipo16)
		for i in range(9):
			self.saco.append(self.tipo17)
		for i in range(8):
			self.saco.append(self.tipo18)
		for i in range(4):
			self.saco.append(self.tipo19)

	# def imprimir(self):
	# 	resultado = ''
	# 	i = 0
	# 	while i < 23:
	# 		resultado += str(self.saco[i].imprimir())
	# 		i = i + 1
	# 	return resultado
