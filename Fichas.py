class Fichas:
	def __init__(self,c,u1,u2,u3,b1,b2,b3,r1,r2,r3,l1,l2,l3):
		up=[u1,u2,u3]
		botton=[b1,b2,b3]
		right=[r1,r2,r3]
		left=[l1,l2,l3]
		centro = [c,c,c]
		self.posicion=[up,right,left,centro,botton]
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
				resultado+=self.posicion[1][lado-1]+self.posicion[3][lado-1]+self.posicion[2][lado-1]
			if lado != 4:
				resultado += "\n"

			lado = lado + 1
		resultado += "\n"	
		return resultado

class ArrayFichas:
	def __init__(self):
		self.fichas = []
		self.fichas.append(Fichas('I','T','T','T','T','T','T','T','T','T','T','T','T'))
		for i in range(4):
			self.fichas.append(Fichas('T','T','T','T','P','P','P','T','T','T','T','T','T'))
		for i in range(3):
			self.fichas.append(Fichas('T','P','P','P','P','P','P','T','T','T','T','T','T'))
		for i in range(5):
			self.fichas.append(Fichas('P','T','T','T','P','P','P','P','P','P','T','T','T'))
		for i in range(2):
			self.fichas.append(Fichas('P','T','T','T','P','P','P','T','T','T','P','P','P'))
		for i in range(3):
			self.fichas.append(Fichas('P','P','P','P','P','P','P','T','T','T','T','T','T'))
		for i in range(5):
			self.fichas.append(Fichas('P','T','T','T','P','P','P','P','P','P','P','P','P'))
	def imprimir(self):
		resultado = ''
		i = 0
		while i < 18:
			resultado += str(self.fichas[i].imprimir())
			i = i + 1
		return resultado
