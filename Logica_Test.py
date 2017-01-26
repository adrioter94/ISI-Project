from Partida import Partida
from Fichas import Fichas
from Jugador import Jugador
from Array_Fichas import ArrayFichas
from Logica import Logica
import unittest


class LogicaTest(unittest.TestCase):

    def test_ficha_camino(self):
        expected = "con_C"
        ficha = ArrayFichas().sacar_ficha(66) #tipo18
        self.assertEqual(expected, Logica().que_ficha_es(ficha))
        Logica().que_ficha_es(ficha)


    def test_ficha_aldea(self):
        expected = "con_A"
        ficha = ArrayFichas().sacar_ficha(0) #tipo1
        self.assertEqual(expected, Logica().que_ficha_es(ficha))
        Logica().que_ficha_es(ficha)


    def test_ficha_aldea_y_camino(self):
        expected = "con_CA"
        ficha = ArrayFichas().sacar_ficha(35) #tipo11
        self.assertEqual(expected, Logica().que_ficha_es(ficha))
        Logica().que_ficha_es(ficha)

    def test_ficha_no_aldea_no_camino(self):
        expected = "sin_CA"
        ficha = ArrayFichas().sacar_ficha(70) #tipo19
        self.assertEqual(expected, Logica().que_ficha_es(ficha))
        Logica().que_ficha_es(ficha)


    def test_ficha_bifurcacion(self):
        expected = "con_B"
        ficha = ArrayFichas().sacar_ficha(49) #tipo16
        self.assertEqual(expected, Logica().que_ficha_es(ficha))
        Logica().que_ficha_es(ficha)


if __name__ == '__main__':
	unittest.main()
