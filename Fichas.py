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


