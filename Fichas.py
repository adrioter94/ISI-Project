
#Clase que representa una ficha
class Fichas:

	#Una ficha se descomcompone en 5 partes: centro, arriba, abajo, derecha e izquierda.
	#Ademas, cada ficha tine zonas: pradera (P), aldea (A), camino (C), iglesia (I), y
	#bifurcacion (B). La zona se representa como un array de 15 numeros, cada numero relacionado
	#con una misma zona de la ficha.
	def __init__(self,c,u1,u2,u3,b1,b2,b3,r1,r2,r3,l1,l2,l3, zona, escudo=False):
		arriba = [u1 ,u2 ,u3]
		abajo = [b1, b2, b3]
		derecha = [r1, r2, r3]
		izquierda = [l1, l2, l3]
		centro = [c, c, c]
		self.territorio = [centro, arriba, abajo, derecha, izquierda]
		self.zona = zona
		self.escudo = escudo
		self.pintada = False


    #Dada una zona de la ficha y un color de seguidor, pinta esa zona con dicho color.
	def pintar_ficha(self,zona,seguidor):
		i=0
		while i < 15:
			if self.zona[i] == zona:
				self.zona[i] = seguidor
			i = i + 1


    #Imprime la ficha con las siguiente informacion: por cada parte de la ficha,
	#el tipos de zona (A, C,..) y la zona a la que pertenece en dicha ficha (1, 2, ..),
	#o si ya esta pintada, el color de esa zona.
	def imprimir(self):
		 ter = self.territorio
		 seg = self.zona
		 resultado = ""
		 resultado += ter[1][0] + str(seg[3]) + " " + ter[1][1]+ str(seg[4]) + " " + ter[1][2] + str(seg[5]) +"\n"
		 resultado += ter[4][0] + str(seg[12])+ " " + ter[0][0]+ str(seg[0]) + " " + ter[3][0] + str(seg[9]) +"\n"
		 resultado += ter[4][1] + str(seg[13])+ " " + ter[0][1]+ str(seg[1]) + " " + ter[3][1] + str(seg[10])+"\n"
		 resultado += ter[4][2] + str(seg[14])+ " " + ter[0][2]+ str(seg[2]) + " " + ter[3][2] + str(seg[11])+"\n"
		 resultado += ter[2][0] + str(seg[6]) + " " + ter[2][1]+ str(seg[7]) + " " + ter[2][2] + str(seg[8]) +"\n"
		 return resultado


    #Gira la ficha en el sentido de las agujas del reloj
	def girar(self):#falta modificar incluyendo los seguidores
	 	aux_arriba = self.territorio[1]
	 	aux_abajo = self.territorio[2]
	 	aux_derecha = self.territorio[3]
	 	aux_izquierda = self.territorio[4]

	 	self.territorio[1] = aux_izquierda
	 	self.territorio[3] = aux_arriba
	 	self.territorio[4] = aux_abajo
	 	self.territorio[2] = aux_derecha

		aux_arr = self.zona[3:6]
	 	aux_aba = self.zona[6:9]
	 	aux_der = self.zona[9:12]
		aux_der = [aux_der[2], aux_der[1], aux_der[0]]
	 	aux_izq = self.zona[12:15]
		aux_izq = [aux_izq[2], aux_izq[1], aux_izq[0]]

		self.zona[3:6] = aux_izq
		self.zona[6:9] = aux_der
		self.zona[9:12] = aux_arr
		self.zona[12:15] = aux_aba
