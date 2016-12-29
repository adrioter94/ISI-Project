class Fichas:
	def __init__(self):
		up=['T','T','T']
		botton=['T','T','T']
		right=['P','P','P']
		left=['P','P','P']
		centro = ['P','P','P']
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
		return resultado
		print "FINAL"


