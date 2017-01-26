from Partida import Partida
from Fichas import Fichas
from Jugador import Jugador
from Array_Fichas import ArrayFichas
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

     # Test para color "azul" -- meter azul de color
    def test_info_jugador_color(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         expected="azul"
         self.assertEqual(p.jugadores[0].color,expected)
         expected="verde"
         self.assertEqual(p.jugadores[1].color,expected)

    # Test compureba todo tanto nombre y colores ( que anade al jugador ) 5 jugadores
    def test_jugadores(self):
        p=Partida()
        p.info_jugadores(5,"Adrian","azul","Alberto","verde","Sandra","rojo","Diego","amarillo","Yo","negro")
        jugs=["Adrian","Alberto","Sandra","Diego","Yo"]
        cols=["azul","verde","rojo","amarillo", "negro"]

        for n in range(4):
            expected= jugs[n]
            self.assertEqual(p.jugadores[n].nombre,expected)
            expected2=cols[n]
            self.assertEqual(p.jugadores[n].color,expected2)

    # test anade jugadores al array
    def test_mete_jugadores (self):
       p=Partida()
       self.assertEqual(len(p.jugadores),0)
       p.info_jugadores(3,"Adrian","azul","Alberto","verde","Sandra","amarillo")
       self.assertEqual(len(p.jugadores), 3)


      # test para ckeck los jugadores anadidos al array no son None
    def test_notNone (self):
        p=Partida()
        p.info_jugadores(5,"Adrian","azul","Alberto","verde","Sandra","rojo","Diego","amarillo","Yo","negro")
        for jug in p.jugadores:
            self.assertIsNotNone(jug)

     #test para comprobar que pasa de turno a los jugadores. primer turno Adrian
    def test_pasar_turno(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         jugador=p.pasar_turno(p.jugadores[0])
         expected="Alberto"
         self.assertEqual(expected,jugador.nombre)


     # test pos valida
    def test_elegir_coord_correcta(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         expected="(12, 15)"
         self.assertEqual(expected,p.elegir([(12,15), (25,32), (25,39)],"(12, 15)"))


     # test para girar
    def test_elegir_coord_incorrecta(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         expected="G"
         self.assertEqual(expected,p.elegir([(12,15), (25,32), (25,39)],"G"))

    # test comprueba seguidores del jugador -1
    def test_colocar_seg(self):
        p=Partida()
        ficha=Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        jugador= Jugador('Adrian', 'rojo')
        expected=jugador.seguidores-1
        p.colocar_seguidor(ficha,jugador,0)
        self.assertEqual(expected,jugador.seguidores)

    # test comprueba que en el indice que indico si hay un 1 ( posicion que se puede poner seguidor) meto el seguidor
    def test_colocar_seg(self):
        p=Partida()
        ficha=Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        jugador= Jugador('Adrian', 'rojo')
        p.colocar_seguidor(ficha,jugador,0)
        expected=["r","r","r","r","r","r","r","r","r","r","r","r","r","r","r"]
        self.assertEqual(expected,ficha.posSeguidores)

    def test_actualizar_posSeguidores(self):
        p = Partida()
        jugador = Jugador('Adrian', 'rojo')
        ficha1 = ArrayFichas().sacar_ficha(70) #tipo19
        ficha2 = ArrayFichas().sacar_ficha(35) #tipo11
        p.tablero.insertar(ficha1, 6, 5)
        p.colocar_seguidor(ficha1, jugador, 3) #3 de arriba
        p.actualizar_posSeguidores(ficha2, (6, 6))
        p.tablero.insertar(ficha2, 6, 6)
        p.tablero.imprimir()
        expected = ["r","r","r",2,2,2,"r",3,4,"r",3,4,"r","r","r"]
        self.assertEqual(expected,ficha2.posSeguidores)


    def test_algoritmo_relleno(self):
        p = Partida()
        jugador = Jugador('Adrian', 'rojo')
        ficha1 = ArrayFichas().sacar_ficha(70) #tipo19
        ficha2 = ArrayFichas().sacar_ficha(35) #tipo11
        p.tablero.insertar(ficha1, 6, 5)
        p.tablero.insertar(ficha2, 6, 6)
        p.actualizar_posSeguidores(ficha2,(6,6))
        p.colocar_seguidor(ficha2, jugador, 13) #3 de arriba
        p.algoritmo_relleno(6,6)
        p.pintada_false()
        p.tablero.imprimir()
        expected = """A2 A2 A2
P4 C1 P4
C1 C1 C1
Pr C1 Pr
Pr Pr Pr
"""

        self.assertEqual(expected,p.tablero.tablero[5][5].imprimir())


if __name__ == '__main__':
	unittest.main()
