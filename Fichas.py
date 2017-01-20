class Fichas:

	def __init__(self,c,u1,u2,u3,b1,b2,b3,r1,r2,r3,l1,l2,l3, posSeguidores, escudo=False):
		arriba=[u1,u2,u3]
		abajo=[b1,b2,b3]
		derecha=[r1,r2,r3]
		izquierda=[l1,l2,l3]
		centro = [c,c,c]
		self.territorio=[centro, arriba, abajo, derecha, izquierda]
		self.posSeguidores=posSeguidores
		self.escudo=escudo


	def imprimir(self):
		 ter = self.territorio
		 seg = self.posSeguidores
		 resultado = ""
		 resultado += ter[1][0] + str(seg[3]) + " " + ter[1][1]+ str(seg[4]) + " " + ter[1][2] + str(seg[5]) +"\n"
		 resultado += ter[4][0] + str(seg[12])+ " " + ter[0][0]+ str(seg[0]) + " " + ter[3][0] + str(seg[9]) +"\n"
		 resultado += ter[4][1] + str(seg[13])+ " " + ter[0][1]+ str(seg[1]) + " " + ter[3][1] + str(seg[10])+"\n"
		 resultado += ter[4][2] + str(seg[14])+ " " + ter[0][2]+ str(seg[2]) + " " + ter[3][2] + str(seg[11])+"\n"
		 resultado += ter[2][0] + str(seg[6]) + " " + ter[2][1]+ str(seg[7]) + " " + ter[2][2] + str(seg[8]) +"\n"
		 return resultado


	def girar(self):#falta modificar incluyendo los seguidores
	 	aux_arriba = self.territorio[1]
	 	aux_abajo = self.territorio[2]
	 	aux_derecha = self.territorio[3]
	 	aux_izquierda = self.territorio[4]
	 	self.territorio[1]=aux_izquierda
	 	self.territorio[3]=aux_arriba
	 	self.territorio[4]=aux_abajo
	 	self.territorio[2]=aux_derecha

		aux_arr=self.posSeguidores[3:6]
	 	aux_aba=self.posSeguidores[6:9]
	 	aux_der= self.posSeguidores[9:12]
	 	aux_izq=self.posSeguidores[12:15]

		self.posSeguidores[3:6]=aux_izq
		self.posSeguidores[6:9]=aux_der
		self.posSeguidores[9:12]=aux_arr
		self.posSeguidores[12:15]=aux_aba
