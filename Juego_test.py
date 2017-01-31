from Partida import Partida
from Array_Fichas import ArrayFichas
from Logica import Logica
import unittest


class PartidaCompleta(unittest.TestCase):

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

        expected_diego=5
        expected_alberto=4
        expected_sandra=3


        p=Partida()
        l=Logica()
        p.info_jugadores(4,"Adrian","azul","Alberto","verde","Sandra","amarillo","Diego","negro")
        ficha1= p.saco.sacar_ficha(47)

        ficha2 = p.saco.sacar_ficha(35)

        ficha2.girar()
        ficha2.girar()

        print ficha2.imprimir()

        jugador = p.jugadores[0]#ADRIAN
        p.jugar_turno(jugador,[4,5],"NO",ficha2)
        l.coloca_ficha_con_A(p.tablero,(4,5)) # Da fallo AQUI!!!!!

        next_jugador = p.pasar_turno(jugador)#ALBERTO


        next_jugador = p.pasar_turno(next_jugador)

        print l.array_caminos
        #self.assertEqual(l.computar_puntos_turno(p.tablero,(4,5),p.jugadores),expected_diego)





if __name__ == '__main__':
	unittest.main()
