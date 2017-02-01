from Partida import Partida
from Array_Fichas import ArrayFichas
from Logica import Logica
import unittest


class PartidaCompleta(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_partida(self):
        p=Partida()
        p.info_jugadores(4,"Adrian","azul","Alberto","verde","Sandra","amarillo","Diego","negro")
        ficha1= p.saco.sacar_ficha(70) # FICHA IGLESIA
        ficha2= p.saco.sacar_ficha(20) # tipo7
        ficha3= p.saco.sacar_ficha(21) # tipo7
        ficha4= p.saco.sacar_ficha(24) #tipo8
        ficha5= p.saco.sacar_ficha(47) #tipo16
        ficha6= p.saco.sacar_ficha(51) #tipo18
        ficha7= p.saco.sacar_ficha(52) #tipo18
        ficha8 = p.saco.sacar_ficha(46) # tipo 15 --- bifurcacion 4 caminos
        ficha9= p.saco.sacar_ficha(18) # tipo 6

        ficha9.girar()
        ficha9.girar()

        ficha4.girar()
        ficha4.girar()
        ficha4.girar()

        ficha5.girar()
        ficha5.girar()

        ficha6.girar()

        ficha8.girar()
        ficha8.girar()

        ficha2.girar()
        ficha2.girar()

        ficha3.girar()

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[5,6],"NO",ficha6)
        next_jugador = p.pasar_turno(jugador)#ALBERTO
        p.jugar_turno(next_jugador,[5,4],"NO",ficha8)
        next_jugador = p.pasar_turno(next_jugador)#SANDRA
        p.jugar_turno(next_jugador,[5,3],"NO",ficha4)
        next_jugador = p.pasar_turno(next_jugador)#DIEGO
        p.jugar_turno(next_jugador,[4,4],"NO",ficha7)
        next_jugador = p.pasar_turno(next_jugador)#ADRIAN
        p.jugar_turno(next_jugador,[6,5],"NO",ficha1)
        next_jugador = p.pasar_turno(next_jugador)#ALBERTO
        p.jugar_turno(next_jugador,[7,5],"NO",ficha2)
        next_jugador = p.pasar_turno(next_jugador)#SANDRA

        p.jugar_turno(next_jugador,[7,6],"SI",ficha3,13)
        next_jugador = p.pasar_turno(next_jugador)#DIEGO
        p.jugar_turno(next_jugador,[4,5],"SI",ficha9,7)
        next_jugador = p.pasar_turno(next_jugador)
        expected="""An An An
P4 C1 P4
C1 C1 C1
Py C1 Py
Py Py Py
"""
        #p.tablero.imprimir()

        self.assertEqual(expected,p.tablero.tablero[5][5].imprimir())

    @unittest.skip("demonstrating skipping")
    def test_partida_2(self):
        expected = 7
        p=Partida()
        l = Logica()
        l.array_aldeas.append([(5,5)])
        p.info_jugadores(2,"Adrian","rojo","Alberto","verde")


        fichaA2 = p.saco.sacar_ficha(5) #tipo3 co
        fichaA3 = p.saco.sacar_ficha(21) #tipo7

        fichaA2.girar()

        fichaA3.girar()
        fichaA3.girar()

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[4,5],"SI",fichaA2,8)
        l.coloca_ficha_con_A(p.tablero,(4, 5))
        next_jugador = p.pasar_turno(jugador)
        p.jugar_turno(next_jugador,[3,5],"NO",fichaA3)
        l.coloca_ficha_con_A(p.tablero,(3, 5))
        next_jugador = p.pasar_turno(next_jugador)


        puntos = l.computar_puntos_turno(p.tablero,(3, 5),p.jugadores)
        self.assertEqual(p.jugadores[0].puntuacion,expected)


    @unittest.skip("demonstrating skipping")
    def test_partida_3(self):

        p=Partida()
        l = Logica()
        l.array_caminos.append([(5,5)])
        p.info_jugadores(2,"Adrian","rojo","Alberto","verde")


        fichaA1 = p.saco.sacar_ficha(52) #tipo3 co
        fichaA2 = p.saco.sacar_ficha(48)
        fichaA3 = p.saco.sacar_ficha(47) #tipo7

        fichaA1.girar()


        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[5,6],"SI",fichaA1,1)
        l.coloca_ficha_con_C(p.tablero,(5, 6))
        next_jugador = p.pasar_turno(jugador)

        p.jugar_turno(next_jugador,[5,7],"NO",fichaA2)
        l.coloca_ficha_con_B(p.tablero,(5, 7))

        next_jugador = p.pasar_turno(next_jugador)
        p.jugar_turno(next_jugador,[5,4],"NO",fichaA3)
        l.coloca_ficha_con_B(p.tablero,(5, 4))

        puntos = l.computar_puntos_turno(p.tablero,(5,4 ),p.jugadores)
        expected=5
        self.assertEqual(p.jugadores[0].puntuacion,expected)


    @unittest.skip("demonstrating skipping")
    def test_partida_4(self):

        p=Partida()
        l = Logica()
        l.array_caminos.append([(5,5)])
        p.info_jugadores(2,"Adrian","rojo","Alberto","verde")

        fichaA1 = p.saco.sacar_ficha(52) #tipo3 co
        fichaA2 = p.saco.sacar_ficha(32)
        fichaA3 = p.saco.sacar_ficha(31)

        fichaA1.girar()

        fichaA2.girar()

        fichaA3.girar()
        fichaA3.girar()
        fichaA3.girar()

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[5,6],"SI",fichaA1,1)
        l.coloca_ficha_con_C(p.tablero,(5, 6))
        next_jugador = p.pasar_turno(jugador)

        p.jugar_turno(next_jugador,[5,7],"NO",fichaA2)
        l.coloca_ficha_con_C(p.tablero,(5, 7))

        next_jugador = p.pasar_turno(next_jugador)
        p.jugar_turno(next_jugador,[5,4],"NO",fichaA3)
        l.coloca_ficha_con_C(p.tablero,(5, 4))

        puntos = l.computar_puntos_turno(p.tablero,(5,4),p.jugadores)
        expected=5
        self.assertEqual(p.jugadores[0].puntuacion,expected)

    @unittest.skip("demonstrating skipping")
    def test_partida_5(self):

        p=Partida()
        l = Logica()
        l.array_caminos.append([(5,5)])
        p.info_jugadores(2,"Adrian","rojo","Alberto","verde")

        fichaA1 = p.saco.sacar_ficha(52) #tipo3 co
        fichaA2 = p.saco.sacar_ficha(24)
        fichaA3 = p.saco.sacar_ficha(25)

        fichaA1.girar()

        fichaA2.girar()

        fichaA3.girar()
        fichaA3.girar()
        fichaA3.girar()

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[5,6],"SI",fichaA1,1)
        l.coloca_ficha_con_C(p.tablero,(5, 6))
        next_jugador = p.pasar_turno(jugador)

        p.jugar_turno(next_jugador,[5,7],"NO",fichaA2)
        l.coloca_ficha_con_C(p.tablero,(5, 7))
        l.coloca_ficha_con_A(p.tablero,(5, 7))


        next_jugador = p.pasar_turno(next_jugador)
        p.jugar_turno(next_jugador,[5,4],"NO",fichaA3)
        l.coloca_ficha_con_C(p.tablero,(5, 4))
        l.coloca_ficha_con_A(p.tablero,(5, 4))

        puntos = l.computar_puntos_turno(p.tablero,(5,4),p.jugadores)
        expected=5
        self.assertEqual(p.jugadores[0].puntuacion,expected)

    @unittest.skip("demonstrating skipping")
    def test_partida_6(self):

        p=Partida()
        l = Logica()
        l.array_caminos.append([(5,5)])
        p.info_jugadores(2,"Adrian","rojo","Alberto","verde")

        fichaA1 = p.saco.sacar_ficha(68) #tipo3 co

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[6,5],"SI",fichaA1,1)

        puntos = l.computar_puntos_turno(p.tablero,(6,5),p.jugadores)
        expected=1
        self.assertEqual(p.jugadores[0].puntuacion,expected)

    @unittest.skip("demonstrating skipping")
    def test_partida_7(self):

        p=Partida()
        l = Logica()
        l.array_caminos.append([(5,5)])
        l.array_aldeas.append([(5,5)])
        p.info_jugadores(2,"Adrian","rojo","Alberto","verde")

        fichaA1 = p.saco.sacar_ficha(68) #tipo3 co
        fichaA2 = p.saco.sacar_ficha(52)
        fichaA3 = p.saco.sacar_ficha(25)
        fichaA4 = p.saco.sacar_ficha(31)

        fichaA2.girar()

        fichaA3.girar()

        fichaA4.girar()
        fichaA4.girar()
        fichaA4.girar()

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[6,5],"SI",fichaA1,1)
        next_jugador = p.pasar_turno(jugador)

        l.computar_puntos_turno(p.tablero,(6,5),p.jugadores)

        p.jugar_turno(next_jugador,[5,6],"SI",fichaA2,1)
        l.coloca_ficha_con_C(p.tablero,(5, 6))
        next_jugador = p.pasar_turno(next_jugador)

        l.computar_puntos_turno(p.tablero,(5,6),p.jugadores)

        p.jugar_turno(next_jugador,[5,7],"NO",fichaA3)
        l.coloca_ficha_con_C(p.tablero,(5, 7))
        l.coloca_ficha_con_A(p.tablero,(5, 7))
        next_jugador = p.pasar_turno(next_jugador)

        l.computar_puntos_turno(p.tablero,(5,7),p.jugadores)

        p.jugar_turno(next_jugador,[5,4],"SI",fichaA4,1)
        l.coloca_ficha_con_C(p.tablero,(5, 4))
        next_jugador = p.pasar_turno(next_jugador)

        l.computar_puntos_turno(p.tablero,(5,4),p.jugadores)

        j1 = 1
        j2 = 6

        self.assertEqual(p.jugadores[0].puntuacion, j1)
        self.assertEqual(p.jugadores[1].puntuacion, j2)


    def test_partida_8(self):

        p=Partida()
        l = Logica()
        l.array_caminos.append([(5,5)])
        l.array_aldeas.append([(5,5)])

        p.info_jugadores(2,"Adrian","rojo","Alberto","verde")

        fichaA1 = p.saco.sacar_ficha(38) #tipo3 co
        fichaA2 = p.saco.sacar_ficha(19)
        fichaA3 = p.saco.sacar_ficha(12) #tipo3 co
        fichaA4 = p.saco.sacar_ficha(8)

        fichaA3.girar()
        fichaA3.girar()

        fichaA4.girar()
        fichaA4.girar()
        fichaA4.girar()

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[5,6],"SI",fichaA1,4)
        l.coloca_ficha_con_A(p.tablero,(5, 6))
        l.coloca_ficha_con_C(p.tablero,(5, 6))
        next_jugador = p.pasar_turno(jugador)

        l.computar_puntos_turno(p.tablero,(5,6),p.jugadores)

        p.jugar_turno(next_jugador,[5,7],"SI",fichaA2,4)
        l.coloca_ficha_con_A(p.tablero,(5, 7))
        next_jugador = p.pasar_turno(next_jugador)

        l.computar_puntos_turno(p.tablero,(5,7),p.jugadores)


        p.jugar_turno(next_jugador,[4,6],"NO",fichaA3)
        l.coloca_ficha_con_A(p.tablero,(4, 6))
        next_jugador = p.pasar_turno(next_jugador)

        l.computar_puntos_turno(p.tablero,(4,6),p.jugadores)

        p.jugar_turno(next_jugador,[4,7],"NO",fichaA4)
        l.coloca_ficha_con_A(p.tablero,(4, 7))
        next_jugador = p.pasar_turno(next_jugador)

        l.computar_puntos_turno(p.tablero,(4,7),p.jugadores)

        j1 = 11
        j2 = 11

        self.assertEqual(p.jugadores[0].puntuacion, j1)
        self.assertEqual(p.jugadores[1].puntuacion, j2)


if __name__ == '__main__':
	unittest.main()
