
class Tablero:
	def __init__(self,ficha_inicial):
		self.tablero = [None] * 145 #numero de filas
		for i in range(145): #numero de filas
			self.tablero[i] = ['X'] * 145#numero de columnas

		self.tab_partida = [None] * 717 #numero de filas 143*5+2
		for i in range(717): #numero de filas
			self.tab_partida[i] = [''] * 431#numero de columnas 143*3+2

		self.tablero[71][71]=ficha_inicial #self.tablero[y][x]
		self.insertar_tabpartida(71,71,ficha_inicial)

	def insertar_tabpartida(self,x,y,ficha):
		primera_y=(y*5)-4
		primera_x = (x*3)-2
		
		i=0
		while i < 3:
			self.tab_partida[primera_y][primera_x+i]=ficha.territorio[0][i]
			i = i + 1
		i = 0
		while i < 3:	
			self.tab_partida[primera_y+1+i][primera_x]=ficha.territorio[2][i]
			self.tab_partida[primera_y+1+i][primera_x+1]=ficha.territorio[3][i]
			self.tab_partida[primera_y+1+i][primera_x+2]=ficha.territorio[1][i]
			i = i + 1
		i = 0
		while i < 3:
			self.tab_partida[primera_y+4][primera_x+i]=ficha.territorio[4][i]
			i = i + 1
			
			
	
	def imprimir_tabpartida(self):
		resultado = ''
		i = 0
		espacio = "false"
		for fila in self.tab_partida:
			while i < 431:
				if fila[i] != '':
					espacio = "true"
				resultado += fila[i]
				i = i +1
			if espacio == "true":
				resultado += "\n"
			espacio = "false"
			i = 0
			 
		
		return resultado
			
	def comprobar_extremos(self,x,y,ficha,zona_comprobar,l_fichacolocar):
		i = 0
		lados_aptos=[]
		if self.tablero[y][x] == 'X':
			lados_aptos=[0,1,2,4]
			return "OK"
		else:
			while i < 3:
				
				if self.tablero[y][x].territorio[zona_comprobar][i]!=ficha.territorio[l_fichacolocar][i]:
					correcto = 'false'
					break
				correcto='true'
				i = i + 1
			i = 0
			if correcto == 'true':
				return "OK"
			else:
				return "ERROR"



	def coor_correctas(self):
		coordenadas_validas=[]
		i = 0
		fila = 0
		while fila < 145:
			while i<145:		
				if self.tablero[fila][i]!='X':
					coor=str(i)+str(fila-1)
					coordenadas_validas.append(coor)
					coor=str(i)+str(fila+1)
					coordenadas_validas.append(coor)
					coor=str(i+1)+str(fila)
					coordenadas_validas.append(coor)
					coor=str(i-1)+str(fila)
					coordenadas_validas.append(coor)
				i = i + 1
			i = 0
			fila = fila + 1
		return coordenadas_validas

	def insertar(self,x,y,ficha):
		vuelta  = 0		
		coordenadas = str(x)+str(y)
		coordenadas_correctas = self.coor_correctas()

		if coordenadas in coordenadas_correctas:
			if y < 144 and y > 0 and x < 144 and x > 0:
				while vuelta < 4:
					#arriba
					arriba = self.comprobar_extremos(x,y-1,ficha,4,0)
					#abajo
					abajo = self.comprobar_extremos(x,y+1,ficha,0,4)
					#izquierda
					izquierda = self.comprobar_extremos(x-1,y,ficha,1,2)
					#derecha
					derecha = self.comprobar_extremos(x+1,y,ficha,2,1)
					 
					if  self.tablero[y][x] == "X" and arriba=="OK" and abajo=="OK"and izquierda=="OK" and derecha=="OK":
						self.tablero[y][x]=ficha
						self.insertar_tabpartida(x,y,ficha)
						return "Ficha insertada en el tablero"
					else:
						ficha.girar()
						vuelta = vuelta + 1
				return "No valida"
		return "Coordenas incorrectas"
	
