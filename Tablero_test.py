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

    def test_es_valida(self):
        t = Tablero()
        ficha1 = ArrayFichas().tipo1 #Todo aldea
        t.insertar(ficha1, 1, 1)
        ficha2 = ArrayFichas().tipo19
        ficha3 = ArrayFichas().tipo2
        self.assertFalse(t.es_valida(ficha2, 1, 2))
        self.assertTrue(t.es_valida(ficha3, 1, 2))


if __name__ == '__main__':
	unittest.main()
