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

    # test anade jugadores al array --- meter 2 jugadores
    def test_mete_jugadores (self):
        p=Partida()
        self.assertEqual(len(p.jugadores),0)
        p.infoJugadores()
        self.assertGreater(len(p.jugadores), 1)


    # test para ckeck los jugadores anadidos al array no son None
    def test_notNone (self):
        p=Partida()
        p.infoJugadores()
        for jug in p.jugadores:
            self.assertIsNotNone(jug)


if __name__ == '__main__':
	unittest.main()
