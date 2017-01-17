class Fichas:
	def __init__(self,c,u1,u2,u3,b1,b2,b3,r1,r2,r3,l1,l2,l3):
		arriba=[u1,u2,u3]
		abajo=[b1,b2,b3]
		derecha=[r1,r2,r3]
		izquierda=[l1,l2,l3]
		centro = [c,c,c]
		self.posicion=[arriba,derecha,izquierda,centro,abajo]
	def imprimir(self):
		lado=0
		i=0
		resultado = ""
		for lugar in self.posicion:
			if (lado == 0 or lado == 4):
				while (i < 3):
					resultado += lugar[i]
					i=i+1
				i=0
			else:
				resultado+=self.posicion[2][lado-1]+self.posicion[3][lado-1]+self.posicion[1][lado-1]
			if lado != 4:
				resultado += "\n"

			lado = lado + 1
		resultado += "\n"
		return resultado

	def girar(self):
		aux_arriba = self.posicion[0]
		aux_abajo = self.posicion[4]
		aux_derecha = self.posicion[1]
		aux_izquierda = self.posicion[2]
		self.posicion[0]=aux_izquierda
		self.posicion[1]=aux_arriba
		self.posicion[2]=aux_abajo
		self.posicion[4]=aux_derecha

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
