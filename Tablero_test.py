from Tablero import Tablero
from Fichas import Fichas
from Array_Fichas import ArrayFichas
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

    def insertar_ficha_tablero(self):
        t = Tablero()
        ficha = ArrayFichas().tipo1
        t.insertar(ficha, 2, 2)
        expected = """A0 A0 A0
A0 A1 A0
A0 A0 A0
A0 A0 A0
A0 A0 A0
"""
        self.assertEqual(expected,t.tablero[2][2].imprimir())


if __name__ == '__main__':
	unittest.main()
