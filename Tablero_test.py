from tablero import Tablero
from Fichas import Fichas
import unittest

class CarcassoneTest(unittest.TestCase):
	def test_tablero_filas(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		self.assertEqual(145,len(Tablero(f).tablero))
	def test_tablero_columnas(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		self.assertEqual(145,len(Tablero(f).tablero[0]))
	def test_tablero_juego_filas(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		self.assertEqual(717,len(Tablero(f).tab_partida))
	def test_tablero_juego_columnas(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		self.assertEqual(431,len(Tablero(f).tab_partida[0]))
	def test_coordenadas_validas(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		expected=['7170', '7172', '7271', '7071']
		coor_validas = Tablero(f).coor_correctas()
		self.assertEqual(expected,coor_validas)
	def test_comprobar_extremo_inferior(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
		expected = "OK"
		self.assertEqual(expected,Tablero(f).comprobar_extremos(71,71,tipo1,0,4))
	def test_comprobar_extremo_superior(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
		expected = "ERROR"
		self.assertEqual(expected,Tablero(f).comprobar_extremos(71,71,tipo1,4,0))

	def test_comprobar_extremo_derecho(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
		expected = "ERROR"
		self.assertEqual(expected,Tablero(f).comprobar_extremos(71,71,tipo1,2,1))

	def test_comprobar_extremo_izquierdo(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
		expected = "ERROR"
		self.assertEqual(expected,Tablero(f).comprobar_extremos(71,71,tipo1,1,2))

	def test_insertar_tabpartida(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
		expected="""AAA
AAA
AAA
AAA
AAA
AAA
PCP
CCC
PCP
PPP
"""
		t = Tablero(f)
		t.insertar(71,70,tipo1)
		self.assertEqual(expected,t.imprimir_tabpartida())

	def test_insertar_correcta(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo6 = Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A')
		t = Tablero(f)
		expected="Ficha insertada en el tablero"
		self.assertEqual(expected,t.insertar(71,70,tipo6))

	def test_insertar_coor(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo6 = Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A')
		t = Tablero(f)
		expected="Coordenas incorrectas"
		self.assertEqual(expected,t.insertar(41,40,tipo6))

	def test_insertar_ficha_no_valida(self):
		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
		tipo11 = Fichas('I','P','P','P','P','C','P','P','P','P','P','P','P')
		t = Tablero(tipo1)
		expected="No valida"
		self.assertEqual(expected,t.insertar(71,70,tipo11))
	
	def test_insertar(self):
		f=Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A')
		t = Tablero(f)
		t.insertar(71,70,tipo1)
		tipo18 = Fichas('C','P','C','P','P','C','P','P','P','P','P','P','P')
		t.insertar(72,71,tipo18)
		expected="""AAA
AAA
AAA
AAA
AAA
AAAPPP
PCPPCP
CCCCCC
PCPPCP
PPPPPP
"""
		self.assertEqual(expected,t.imprimir_tabpartida())

if __name__ == '__main__':
	unittest.main()
