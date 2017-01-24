from Tablero import Tablero
from Fichas import Fichas
import unittest

class CarcassoneTest(unittest.TestCase):

	def test_constructor(self):
		t=Tablero()
		expected="""-- -- --
-- -- --
-- -- --
-- -- --
-- -- --
"""
		for y in range(0,t.w): #w columnas
			 for x in range(0,t.h): # h filas
				 self.assertEqual(expected,t.tablero[x][y].imprimir())

if __name__ == '__main__':
	unittest.main()
