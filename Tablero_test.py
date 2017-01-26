from Tablero import Tablero
from Fichas import Fichas
from Array_Fichas import ArrayFichas
import unittest

class CarcassoneTest(unittest.TestCase):

    # Long saco (0-70)
    # test constructor ficha inicial
    def test_constructor(self):
        t=Tablero()
        expected="""A2 A2 A2
P4 C1 P4
C1 C1 C1
P3 C1 P3
P3 P3 P3
"""
        self.assertEqual(expected,t.tablero[int(round((t.w-1)/2.0))][int(round((t.h-1)/2.0))].imprimir())

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
        ficha1 = ArrayFichas().sacar_ficha(0) #Todo aldea
        t.insertar(ficha1, 1, 1)
        ficha2 = ArrayFichas().sacar_ficha(70) #tipo19
        ficha3 = ArrayFichas().sacar_ficha(1)  #tipo2
        self.assertFalse(t.es_valida(ficha2, 1, 2))
        self.assertTrue(t.es_valida(ficha3, 1, 2))

    def test_todas_pos_validas(self):
        t = Tablero()
        ficha1 = ArrayFichas().sacar_ficha(0) #Todo aldea
        t.insertar(ficha1, 2, 2)
        ficha2 = ArrayFichas().sacar_ficha(22) #Solo un lado con aldea
        expected = [[3, 2]]
        self.assertEqual(expected, t.todas_pos_validas(ficha2))


    # hay que contar que ya esta puesta la ficha inicial
    def test_comprobacion_ficha_valida(self):
        t = Tablero()
        ficha1 = ArrayFichas().sacar_ficha(21) # tipo7 Aldea por arriba y el resto pradera
        t.insertar(ficha1, 2, 2)
        ficha2 = ArrayFichas().sacar_ficha(24) # tipo8 Aldea por 3 lados y camino por abajo
        ficha3 = ArrayFichas().sacar_ficha(48) #tipo 15Todo camino
        self.assertTrue(t.comprobacion_ficha_valida(ficha2))



if __name__ == '__main__':
	unittest.main()
