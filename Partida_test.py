from prueba import Partida
import unittest


class PArtidaTest(unittest.TestCase):

    # Test para Nombre Adrian-- meter Adrian de nombre
    def test_info_jugador_nombre(self):
        p=Partida()
        p.infoJugadores()
        expected="Adrian"
        self.assertEqual(p.jugadores[0].nombre,expected)

    # Test para color "azul" -- meter azul de color
    def test_info_jugador_color(self):
        p=Partida()
        p.infoJugadores()
        expected="azul"
        self.assertEqual(p.jugadores[0].color,expected)

    


if __name__ == '__main__':
	unittest.main()
