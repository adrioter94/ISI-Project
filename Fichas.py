class Fichas:

	def __init__(self,c,u1,u2,u3,b1,b2,b3,r1,r2,r3,l1,l2,l3,posSeguidores=[],escudo=False):
		arriba=[u1,u2,u3]
		abajo=[b1,b2,b3]
		derecha=[r1,r2,r3]
		izquierda=[l1,l2,l3]
		centro = [c,c,c]

		self.territorio=[arriba,derecha,izquierda,centro,abajo]
		self.posSeguidores=posSeguidores
		self.escudo=escudo

	def imprimir(self,posicion):
		lado=0
		i=0
		resultado = ""
		for lugar in posicion:
			if (lado == 0 or lado == 4):
				while (i < 3):
					resultado += lugar[i]
					i=i+1
				i=0
			else:
				resultado+=posicion[2][lado-1]+posicion[3][lado-1]+posicion[1][lado-1]
			if lado != 4:
				resultado += "\n"

			lado = lado + 1
		resultado += "\n"
		return resultado


	def girar(self):
		aux_arriba = self.territorio[0]
		aux_abajo = self.territorio[4]
		aux_derecha = self.territorio[1]
		aux_izquierda = self.territorio[2]
		self.territorio[0]=aux_izquierda
		self.territorio[1]=aux_arriba
		self.territorio[2]=aux_abajo
		self.territorio[4]=aux_derecha
