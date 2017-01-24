from Partida import Partida
import unittest


class PArtidaTest(unittest.TestCase):

    # Test para Nombre Adrian-- meter Adrian de nombre
    def test_info_jugador_nombre(self):
        p=Partida()
        p.info_jugadores(2,"Adrian","azul","Alberto","verde")
        expected="Adrian"
        self.assertEqual(p.jugadores[0].nombre,expected)
        expected="Alberto"
        self.assertEqual(p.jugadores[1].nombre,expected)
#
#     # Test para color "azul" -- meter azul de color
#     def test_info_jugador_color(self):
#         p=Partida()
#         p.infoJugadores()
#         expected="azul"
#         self.assertEqual(p.jugadores[0].color,expected)
#
#
# # test anade jugadores al array --- meter 2 jugadores
#     def test_mete_jugadores (self):
#       p=Partida()
#       self.assertEqual(len(p.jugadores),0)
#       p.infoJugadores()
#       self.assertGreater(len(p.jugadores), 1)
#
#
#      # test para ckeck los jugadores anadidos al array no son None
#     def test_notNone (self):
#        p=Partida()
#        p.infoJugadores()
#        for jug in p.jugadores:
#            self.assertIsNotNone(jug)
#
#     #test para comprobar que pasa de turno a los jugadores.(3 jugadores Alberto // Adrian // Sandra)
#     def test_pasar_turno(self):
#         p=Partida()
#         p.info_jugadores()
#         jugador=p.pasar_turno(p.jugadores[0])
#         expected="Adrian"
#         self.assertEqual(expected,jugador.nombre)
#
#
#     # test pos valida
#     def test_elegir_coord_correcta(self):
#         p=Partida()
#         p.info_jugadores()
#         expected="(12, 15)"
#         self.assertEqual(expected,p.elegir([(12,15), (25,32), (25,39)]))
#
#     # test para girar
#     def test_elegir_coord_incorrecta(self):
#         p=Partida()
#         p.info_jugadores()
#         expected="G"
#         self.assertEqual(expected,p.elegir([(12,15), (25,32), (25,39)]))

if __name__ == '__main__':
	unittest.main()
