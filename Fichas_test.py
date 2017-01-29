from Fichas import Fichas
from Array_Fichas import ArrayFichas
import unittest

class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		f = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],True)
		expected="""A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
"""
		self.assertEqual(expected,f.imprimir())

	def test_second_ficha(self):
		f=Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,2,2,1,1,1,1,1,1],False)
		expected="""A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
P2 P2 P2
"""

		self.assertEqual(expected,f.imprimir())


	def test_ficha_3(self):
		f=Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,2,2,2,2,2,2,1,1,1,1,1,1],False)
		expected="""P2 P2 P2
A1 A1 A1
A1 A1 A1
A1 A1 A1
P2 P2 P2
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_4(self):
		f=Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A',[1,1,1,2,2,2,1,1,1,1,1,1,2,2,2],False)
		expected="""A2 A2 A2
A2 P1 P1
A2 P1 P1
A2 P1 P1
P1 P1 P1
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_5(self):
		f=Fichas('P','A','A','A','P','P','P','A','A','A','P','P','P',[1,1,1,2,2,2,1,1,1,3,3,3,1,1,1],False)
		expected="""A2 A2 A2
P1 P1 A3
P1 P1 A3
P1 P1 A3
P1 P1 P1
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_6(self):
		f=Fichas('P','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2],False)
		expected="""P1 P1 P1
A2 P1 A2
A2 P1 A2
A2 P1 A2
P1 P1 P1
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_7(self):
		f=Fichas('P','A','A','A','P','P','P','P','P','P','P','P','P',[1,1,1,2,2,2,1,1,1,1,1,1,1,1,1],False)
		expected="""A2 A2 A2
P1 P1 P1
P1 P1 P1
P1 P1 P1
P1 P1 P1
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_8(self):
		f=Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,3,4,1,1,1,1,1,1],False)
		expected="""A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
P2 C3 P4
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_vacia(self):
		f=Fichas('-','-','-','-','-','-','-','-','-','-','-','-','-',['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],False)
		expected="""-- -- --
-- -- --
-- -- --
-- -- --
-- -- --
"""
		self.assertEqual(f.imprimir(),expected)

	def test_long_array(self):

		self.assertEqual(len(ArrayFichas().saco),71)

	def test_sacar_ficha_primera(self):
		f = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],True)
		expected="""A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
"""
		self.assertEqual(f.imprimir(),expected)


	def test_sacar_ult_ficha(self):
		f=ArrayFichas().sacar_ficha(70)
		expected="""P2 P2 P2
P2 I1 P2
P2 I1 P2
P2 I1 P2
P2 P2 P2
"""
		self.assertEqual(f.imprimir(),expected)

	def test_sacar_medio_ficha(self):
		f=ArrayFichas().sacar_ficha(25)
		expected="""A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
P2 C3 P4
"""
		self.assertEqual(f.imprimir(),expected)


	def eliminar_ficha_saco(self):
		ficha = ArrayFichas().sacar_ficha(26)
		expected = len(ArrayFichas().saco)-1
		ArrayFichas().eliminar_ficha(ficha)
		self.assertEqual(len(ArrayFichas().saco),expected)


 	def test_girar_ficha(self):

 		f=Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,2,2,1,1,1,1,1,1],False)
 		f.girar()
 		expected="""A1 A1 A1
P2 A1 A1
P2 A1 A1
P2 A1 A1
A1 A1 A1
"""
		self.assertEqual(expected,f.imprimir())

	def test_girar_bif(self):
		f = Fichas('B','P','C','P','P','C','P','P','C','P','P','C','P',[0,0,0,1,2,3,4,5,6,3,7,6,1,8,4],False)
		f.girar()
		expected="""P4 C8 P1
P4 B0 P1
C5 B0 C2
P6 B0 P3
P6 C7 P3
"""
		self.assertEqual(expected,f.imprimir())

if __name__ == '__main__':
	unittest.main()
