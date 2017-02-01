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








if __name__ == '__main__':
	unittest.main()
