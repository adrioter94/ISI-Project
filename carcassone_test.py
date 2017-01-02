from Fichas import Fichas
from Fichas import ArrayFichas
from tablero import Tablero
import unittest
class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		expected="""TTT
PPP
PPP
PPP
TTT
"""
		self.assertEqual(expected,Fichas('P','T','T','T'
,'T','T','T','P','P','P','P','P','P').imprimir())

	def test_second_ficha(self):
		expected="""TTT
PTP
PTP
PTP
TTT
"""
		self.assertEqual(expected,Fichas('T','T','T','T'
,'T','T','T','P','P','P','P','P','P').imprimir())

	def test_create_array_of_18(self):
		expected ="""TTT
TCT
TCT
TCT
TTT
TTT
TTT
TTT
TTT
PPP
TTT
TTT
TTT
TTT
PPP
TTT
TTT
TTT
TTT
PPP
TTT
TTT
TTT
TTT
PPP
PPP
TTT
TTT
TTT
PPP
PPP
TTT
TTT
TTT
PPP
PPP
TTT
TTT
TTT
PPP
TTT
PPT
PPT
PPT
PPP
TTT
PPT
PPT
PPT
PPP
TTT
PPT
PPT
PPT
PPP
TTT
PPT
PPT
PPT
PPP
TTT
PPT
PPT
PPT
PPP
TTT
TPP
TPP
TPP
PPP
TTT
TPP
TPP
TPP
PPP
PPP
TPT
TPT
TPT
PPP
PPP
TPT
TPT
TPT
PPP
PPP
TPT
TPT
TPT
PPP
"""
		self.assertEqual(expected,ArrayFichas().imprimir())
	def test_tablero_filas(self):
		self.assertEqual(72,len(Tablero().tablero))
	def test_tablero_columnas(self):
		self.assertEqual(72,len(Tablero().tablero[0]))

if __name__ == '__main__':
	unittest.main()
