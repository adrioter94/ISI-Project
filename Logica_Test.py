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


    def test_ficha_aldea(self):
        expected = "con_A"
        ficha = ArrayFichas().sacar_ficha(0) #tipo1
        self.assertEqual(expected, Logica().que_ficha_es(ficha))


    def test_ficha_aldea_y_camino(self):
        expected = "con_CA"
        ficha = ArrayFichas().sacar_ficha(35) #tipo11
        self.assertEqual(expected, Logica().que_ficha_es(ficha))

    def test_ficha_no_aldea_no_camino(self):
        expected = "sin_CA"
        ficha = ArrayFichas().sacar_ficha(70) #tipo19
        self.assertEqual(expected, Logica().que_ficha_es(ficha))


    def test_ficha_bifurcacion(self):
        expected = "con_B"
        ficha = ArrayFichas().sacar_ficha(49) #tipo16
        self.assertEqual(expected, Logica().que_ficha_es(ficha))


    def test_ficha_bifurcacion_y_aldea(self):
        expected = "con_BA"
        ficha = ArrayFichas().sacar_ficha(40) #tipo13
        self.assertEqual(expected, Logica().que_ficha_es(ficha))


    def test_dame_pos_contiguas(self):
        expected = [(2,3), (4,3), (3,4), (3,2)]
        self.assertEqual(expected, Logica().dame_pos_contiguas(3,3)[0])


    def test_dame_camino(self):
        l = Logica()
        l.array_caminos.append([(2,2), (2,3)])
        l.array_caminos.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(4,3)])
        expected = [(2,2), (2,3)]
        self.assertEqual(expected, l.dame_camino((2,2)))


    def test_dame_aldea(self):
        l = Logica()
        l.array_aldeas.append([(3,2), (3,3)])
        l.array_aldeas.append([(1,1)])
        l.array_aldeas.append([(4,3), (4,2)])
        expected = [(4,3), (4,2)]
        self.assertEqual(expected, l.dame_aldea((4,2)))


    def test_continua_camino(self):
        p = Partida()
        l = Logica()
        l.array_caminos.append([(2,2), (2,3)]) #camino de ficha1 y ficha2
        l.array_caminos.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(57) #tipo17
        ficha1.girar()
        p.tablero.insertar(ficha1, 2, 3)

        ficha2 = ArrayFichas().sacar_ficha(65) #tipo18
        ficha2.girar()
        ficha2.girar()
        ficha2.girar()
        p.tablero.insertar(ficha2, 2, 2)

        mi_ficha = ArrayFichas().sacar_ficha(66) #tipo18
        p.tablero.insertar(mi_ficha, 2, 4) # a la derecha de la ficha1

        self.assertTrue(l.continua_camino(p.tablero, (2,4), (2,3), "izquierda"))


    def test_no_continua_camino(self):
        p = Partida()
        l = Logica()
        l.array_caminos.append([(2,2), (2,3)]) #camino de ficha1 y ficha2
        l.array_caminos.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(57) #tipo17
        ficha1.girar()
        p.tablero.insertar(ficha1, 2, 3)

        ficha2 = ArrayFichas().sacar_ficha(65) #tipo18
        ficha2.girar()
        ficha2.girar()
        ficha2.girar()
        p.tablero.insertar(ficha2, 2, 2)

        mi_ficha = ArrayFichas().sacar_ficha(70) #tipo19
        p.tablero.insertar(mi_ficha, 2, 4) # a la derecha de la ficha1

        self.assertFalse(l.continua_camino(p.tablero, (2,4), (2,3), "izquierda")) #la (2,3) esta a la izda de (2,4)


    def test_continua_aldea(self):
        p = Partida()
        l = Logica()
        l.array_aldeas.append([(3,3), (3,2)]) #aldea de la ficha1 y ficha2
        l.array_aldeas.append([(1,1), (2,1), (3,1)])
        l.array_aldeas.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(5) #tipo3
        p.tablero.insertar(ficha1, 3, 3)

        ficha2 = ArrayFichas().sacar_ficha(18) #tipo7
        ficha2.girar()
        p.tablero.insertar(ficha2, 3, 2)

        mi_ficha = ArrayFichas().sacar_ficha(18) #tipo18
        mi_ficha.girar()
        mi_ficha.girar()
        mi_ficha.girar()
        p.tablero.insertar(mi_ficha, 3, 4) #a la derecha de la ficha1

        self.assertTrue(l.continua_aldea(p.tablero, (3,4), (3,3), "izquierda")) #la (3,3) esta a la izda de (3,4)


    def test_no_continua_aldea(self):
        p = Partida()
        l = Logica()
        l.array_caminos.append([(2,2), (2,3)]) #aldea de la ficha1 y ficha2
        l.array_caminos.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(5) #tipo3
        p.tablero.insertar(ficha1, 3, 3)

        ficha2 = ArrayFichas().sacar_ficha(18) #tipo7
        ficha2.girar()
        p.tablero.insertar(ficha2, 3, 2)

        mi_ficha = ArrayFichas().sacar_ficha(70) #tipo19
        mi_ficha.girar()
        mi_ficha.girar()
        mi_ficha.girar()
        p.tablero.insertar(mi_ficha, 3, 4) #a la derecha de la ficha1

        self.assertFalse(l.continua_aldea(p.tablero, (3,4), (3,3), "izquierda")) #la (3,3) esta a la izda de (3,4)



    def test_coloca_ficha_con_C_caminosInconexos(self):
        p = Partida()
        l = Logica()
        l.array_caminos.append([(2,2)]) #camino de la ficha1
        l.array_caminos.append([(2,4)]) #camino de la ficha2
        l.array_caminos.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(65) #tipo18
        ficha1.girar()
        ficha1.girar()
        ficha1.girar()
        p.tablero.insertar(ficha1, 2, 2)

        ficha2 = ArrayFichas().sacar_ficha(66) #tipo18
        p.tablero.insertar(ficha2, 2, 4)

        mi_ficha = ArrayFichas().sacar_ficha(57) #tipo17
        mi_ficha.girar()
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la ficha1 y la ficha2

        l.coloca_ficha_con_C(p.tablero, (2,3))

        expected = [(2,4), (2,3), (2,2)]

        self.assertEqual(expected, l.dame_camino((2,3)))


    def test_coloca_ficha_con_C_unionUnSoloCamino(self):
        p = Partida()
        l = Logica()
        l.array_caminos.append([(2,4)]) #camino de la ficha1
        l.array_caminos.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(57) #tipo17
        ficha1.girar()
        ficha1.girar()
        ficha1.girar()
        p.tablero.insertar(ficha1, 2, 4)

        ficha2 = ArrayFichas().sacar_ficha(70) #tipo19
        p.tablero.insertar(ficha2, 2, 2)

        mi_ficha = ArrayFichas().sacar_ficha(66) #tipo18
        mi_ficha.girar()
        mi_ficha.girar()
        mi_ficha.girar()
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la ficha1 y la ficha2

        l.coloca_ficha_con_C(p.tablero, (2,3))

        expected = [(2,4), (2,3)]

        self.assertEqual(expected, l.dame_camino((2,3)))


    def test_coloca_ficha_con_C_sinUnion(self):
        p = Partida()
        l = Logica()
        l.array_caminos.append([(4,4), (4,5)])
        l.array_caminos.append([(1,1), (2,1), (3,1)])

        ficha1 = ArrayFichas().sacar_ficha(69) #tipo19
        p.tablero.insertar(ficha1, 2, 4)

        ficha2 = ArrayFichas().sacar_ficha(70) #tipo19
        p.tablero.insertar(ficha2, 2, 2)

        mi_ficha = ArrayFichas().sacar_ficha(57) #tipo17
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la ficha1 y la ficha2

        l.coloca_ficha_con_C(p.tablero, (2,3))

        expected = [(2,3)]

        self.assertEqual(expected, l.dame_camino((2,3)))


    def test_coloca_ficha_con_A_aldeasInconexas(self):
        p = Partida()
        l = Logica()
        l.array_aldeas.append([(2,2)]) #aldea de la ficha1
        l.array_aldeas.append([(2,4)]) #aldea de la ficha2
        l.array_aldeas.append([(1,1), (2,1), (3,1)])
        l.array_aldeas.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(1) #tipo2
        p.tablero.insertar(ficha1, 2, 2)

        ficha2 = ArrayFichas().sacar_ficha(2) #tipo2
        p.tablero.insertar(ficha2, 2, 4)

        mi_ficha = ArrayFichas().sacar_ficha(5) #tipo3
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la ficha1 y la ficha2

        l.coloca_ficha_con_A(p.tablero, (2,3))

        expected = [(2,4), (2,3), (2,2)]

        self.assertEqual(expected, l.dame_aldea((2,3)))


    def test_coloca_ficha_con_A_unionUnaSolaAldea(self):
        p = Partida()
        l = Logica()
        l.array_aldeas.append([(2,4)]) #aldea de la ficha1
        l.array_aldeas.append([(1,1), (2,1), (3,1)])
        l.array_aldeas.append([(4,3)])

        ficha1 = ArrayFichas().sacar_ficha(1) #tipo2
        p.tablero.insertar(ficha1, 2, 4)

        ficha2 = ArrayFichas().sacar_ficha(70) #tipo19
        p.tablero.insertar(ficha2, 2, 2)

        mi_ficha = ArrayFichas().sacar_ficha(18) #tipo6
        mi_ficha.girar()
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la ficha1 y la ficha2

        l.coloca_ficha_con_A(p.tablero, (2,3))

        expected = [(2,4), (2,3)]

        self.assertEqual(expected, l.dame_aldea((2,3)))


    def test_coloca_ficha_con_A_sinUnion(self):
        p = Partida()
        l = Logica()
        l.array_aldeas.append([(4,4), (4,5)])
        l.array_aldeas.append([(1,1), (2,1), (3,1)])

        ficha1 = ArrayFichas().sacar_ficha(69) #tipo19
        p.tablero.insertar(ficha1, 2, 4)

        ficha2 = ArrayFichas().sacar_ficha(70) #tipo19
        p.tablero.insertar(ficha2, 2, 2)

        mi_ficha = ArrayFichas().sacar_ficha(18) #tipo6
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la ficha1 y la ficha2

        l.coloca_ficha_con_A(p.tablero, (2,3))

        expected = [(2,3)]

        self.assertEqual(expected, l.dame_aldea((2,3)))


    def test_comprueba_Ficha_conA(self):
        p = Partida()
        l = Logica()
        l.array_aldeas.append([(2,2)]) #aldea de la fichaA1
        l.array_aldeas.append([(2,4)]) #aldea de la fichaA2
        l.array_aldeas.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(5,2), (5,3)])
        l.array_caminos.append([(4,3)]) #camino de la fichaC1

        fichaA1 = ArrayFichas().sacar_ficha(1) #tipo2
        p.tablero.insertar(fichaA1, 2, 2)

        fichaA2 = ArrayFichas().sacar_ficha(2) #tipo2
        p.tablero.insertar(fichaA2, 2, 4)

        fichaC1 = ArrayFichas().sacar_ficha(57) #tipo17
        fichaC1.girar()
        p.tablero.insertar(fichaC1, 4, 3)

        mi_ficha = ArrayFichas().sacar_ficha(5) #tipo3
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la fichaA1 y la fichaA2

        l.comprueba_ficha(p.tablero, (2,3), mi_ficha)

        expected = [(2,4), (2,3), (2,2)]

        self.assertEqual(expected, l.dame_aldea((2,3)))


    def test_comprueba_Ficha_conC(self):
        p = Partida()
        l = Logica()
        l.array_aldeas.append([(2,2)]) #aldea de la fichaA1
        l.array_aldeas.append([(2,4)]) #aldea de la fichaA2
        l.array_aldeas.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(5,2), (5,1)])
        l.array_caminos.append([(4,3)]) #camino de la fichaC1

        fichaA1 = ArrayFichas().sacar_ficha(1) #tipo2
        p.tablero.insertar(fichaA1, 2, 2)

        fichaA2 = ArrayFichas().sacar_ficha(2) #tipo2
        p.tablero.insertar(fichaA2, 2, 4)

        fichaC1 = ArrayFichas().sacar_ficha(57) #tipo17
        p.tablero.insertar(fichaC1, 4, 3)

        mi_ficha = ArrayFichas().sacar_ficha(57) #tipo17
        p.tablero.insertar(mi_ficha, 5, 3) #coloco mi_ficha debajo de la fichaC1

        l.comprueba_ficha(p.tablero, (5,3), mi_ficha)

        expected = [(4,3), (5,3)]

        self.assertEqual(expected, l.dame_camino((5,3)))


    def test_comprueba_Ficha_conCA(self):
        todos = []
        p = Partida()
        l = Logica()
        l.array_aldeas.append([(2,2)]) #aldea de la fichaA1
        l.array_aldeas.append([(2,4)]) #aldea de la fichaA2
        l.array_aldeas.append([(1,1), (2,1), (3,1)])
        l.array_caminos.append([(5,2), (5,3)])
        l.array_caminos.append([(4,3)]) #camino de la fichaC1
        l.array_caminos.append([(3,3)]) #camino de la fichaC2

        fichaA1 = ArrayFichas().sacar_ficha(1) #tipo2
        p.tablero.insertar(fichaA1, 2, 2)

        fichaA2 = ArrayFichas().sacar_ficha(2) #tipo2
        p.tablero.insertar(fichaA2, 2, 4)

        fichaC1 = ArrayFichas().sacar_ficha(57) #tipo17
        fichaC1.girar()
        p.tablero.insertar(fichaC1, 4, 3)

        fichaC2 = ArrayFichas().sacar_ficha(56) #tipo17
        p.tablero.insertar(fichaC2, 3, 3)

        mi_ficha = ArrayFichas().sacar_ficha(23) #tipo8
        p.tablero.insertar(mi_ficha, 2, 3) #coloco mi_ficha entre la fichaA1 y la fichaA2 y encima de la fichaC2

        l.comprueba_ficha(p.tablero, (2,3), mi_ficha)
        todos.append(l.dame_aldea((2,3)))
        todos.append(l.dame_camino((2,3)))

        expected = [[(2,4), (2,3), (2,2)], [(3,3), (2,3)]]

        self.assertEqual(expected, todos)


    def test_dame_camino_valido_B(self):
        todos = []
        p = Partida()
        l = Logica()
        l.array_caminos.append([(4,3), (5,3)])
        l.array_caminos.append([(4,3), (3,3), (3,2)])
        l.array_caminos.append([(4,3)]) #la bifuracion se encuentra en la posicion (4,3)

        expected = [(4,3)]

        self.assertEqual(expected, l.dame_camino_valido_B((4,3)))


    def test_coloca_ficha_con_B(self):
        todos = []
        p = Partida()
        l = Logica()

        #mi_ficha = ArrayFichas().sacar_ficha(44) #tipo15
        mi_ficha = ArrayFichas().sacar_ficha(48) #tipo16
        p.tablero.insertar(mi_ficha, 2, 3)

        l.comprueba_ficha(p.tablero, (2,3), mi_ficha)

        expected = [[(2,3)], [(2,3)], [(2,3)]]

        self.assertEqual(expected, l.array_caminos)


    def test_coloca_ficha_con_B2(self):

        p = Partida()
        l = Logica()
        l.array_caminos.append([(2,4)]) #camino de la fichaC1

        fichaC1 = ArrayFichas().sacar_ficha(66) #tipo18
        p.tablero.insertar(fichaC1, 2, 4)

        #mi_ficha = ArrayFichas().sacar_ficha(44) #tipo15
        mi_ficha = ArrayFichas().sacar_ficha(48) #tipo16
        p.tablero.insertar(mi_ficha, 2, 3)

        l.comprueba_ficha(p.tablero, (2,3), mi_ficha)

        expected = [[(2,3)], [(2,4), (2,3)], [(2,3)]]

        self.assertEqual(expected, l.array_caminos)


    #test 2 bifurcaciones
    def test_coloca_B2(self):
        p=Partida();
        l = Logica()
        l.array_caminos.append([(2,2)]) #camino de la fichaC1
        l.array_caminos.append([(2,2)]) #camino de la fichaC1
        l.array_caminos.append([(2,2),(2,1)]) #camino de la fichaC1 y fichaC4
        l.array_caminos.append([(2,4)]) #camino de la fichaC2
        l.array_caminos.append([(3,3)]) #camino de la fichaC3
        l.array_caminos.append([(3,3)]) #camino de la fichaC3
        l.array_caminos.append([(3,3)]) #camino de la fichaC3
        l.array_caminos.append([(3,3)]) #camino de la fichaC3

        fichaC1 = ArrayFichas().sacar_ficha(41) #tipo13
        fichaC2 = ArrayFichas().sacar_ficha(60) #tipo18
        fichaC3 = ArrayFichas().sacar_ficha(45) #tipo15
        fichaC4 = ArrayFichas().sacar_ficha(35) #tipo11
        mi_ficha = ArrayFichas().sacar_ficha(48) #tipo16

        p.tablero.insertar(mi_ficha, 2, 3)
        p.tablero.insertar(fichaC1, 2, 2)
        p.tablero.insertar(fichaC2, 2, 4)
        p.tablero.insertar(fichaC3, 3, 3)
        p.tablero.insertar(fichaC3, 2, 1)

        l.comprueba_ficha(p.tablero, (2,3), mi_ficha)

        expected=[[(2, 2)], [(2, 2), (2, 1)], [(3, 3)], [(3, 3)], [(3, 3)], [(3, 3), (2, 3)], [(2, 4), (2, 3)], [(2, 2), (2, 3)]]


        self.assertEqual(expected, l.array_caminos)


    def test_camino_no_completado(self):
        p=Partida();
        l = Logica()

        l.array_caminos.append([(2,2), (3,2)]) #camino de las fichas

        fichaC1 = ArrayFichas().sacar_ficha(23) #tipo8
        fichaC2 = ArrayFichas().sacar_ficha(55) #tipo17

        p.tablero.insertar(fichaC1, 2, 2)
        p.tablero.insertar(fichaC2, 3, 2)

        self.assertFalse(l.camino_completado(p.tablero,l.dame_camino((2,2))))

    def test_camino_completado(self):
        p=Partida();
        l = Logica()

        l.array_caminos.append([(2,2), (3,2), (4,2)]) #camino de las fichas

        fichaC1 = ArrayFichas().sacar_ficha(24) #tipo8
        fichaC2 = ArrayFichas().sacar_ficha(55) #tipo17
        fichaC3 = ArrayFichas().sacar_ficha(46) #tipo15

        p.tablero.insertar(fichaC1, 2, 2)
        p.tablero.insertar(fichaC2, 3, 2)
        p.tablero.insertar(fichaC3, 4, 2)

        self.assertTrue(l.camino_completado(p.tablero,l.dame_camino((2,2))))


    def test_aldea_no_completada(self):
        p=Partida();
        l = Logica()

        l.array_aldeas.append([(2,2), (2,3)]) #aldea de las fichas

        fichaC1 = ArrayFichas().sacar_ficha(14) #tipo5
        fichaC2 = ArrayFichas().sacar_ficha(6) #tipo3


        p.tablero.insertar(fichaC1, 2, 2)
        p.tablero.insertar(fichaC2, 2, 3)


        self.assertFalse(l.aldea_completada(p.tablero,l.dame_aldea((2,2))))

    def test_aldea_completada(self):
        p=Partida();
        l = Logica()

        l.array_aldeas.append([(2,2), (2,3), (2,4)]) #aldea de las fichas

        fichaC1 = ArrayFichas().sacar_ficha(21) #tipo7
        fichaC1.girar()

        fichaC2 = ArrayFichas().sacar_ficha(5) #tipo3

        fichaC3 = ArrayFichas().sacar_ficha(22) #tipo7
        fichaC3.girar()
        fichaC3.girar()
        fichaC3.girar()


        p.tablero.insertar(fichaC1, 2, 2)
        p.tablero.insertar(fichaC2, 2, 3)
        p.tablero.insertar(fichaC3, 2, 4)


        self.assertTrue(l.aldea_completada(p.tablero,l.dame_aldea((2,2))))

    def test_aldea_completada(self):
        p=Partida();
        l = Logica()

        l.array_aldeas.append([(2,2), (2,3), (2,4)]) #aldea de las fichas

        fichaC1 = ArrayFichas().sacar_ficha(14) #tipo5
        fichaC2 = ArrayFichas().sacar_ficha(5) #tipo3
        fichaC3 = ArrayFichas().sacar_ficha(16) #tipo6

        p.tablero.insertar(fichaC1, 2, 2)
        p.tablero.insertar(fichaC2, 2, 3)
        p.tablero.insertar(fichaC3, 2, 4)

        self.assertTrue(l.aldea_completada(p.tablero,l.dame_aldea((2,2))))


if __name__ == '__main__':
	unittest.main()
