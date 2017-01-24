from Fichas import Fichas
from Array_Fichas import ArrayFichas
import unittest

class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		f=Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		expected="""A0 A0 A0
A0 A1 A0
A0 A0 A0
A0 A0 A0
A0 A0 A0
"""
		self.assertEqual(expected,f.imprimir())

	def test_second_ficha(self):
		f=Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
		expected="""A0 A0 A0
A0 A1 A0
A0 A0 A0
A0 A0 A0
P1 P0 P0
"""

		self.assertEqual(expected,f.imprimir())


	def test_ficha_3(self):
		f=Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A',[1,0,0,1,0,0,1,0,0,0,0,0,0,0,0])
		expected="""P1 P0 P0
A0 A1 A0
A0 A0 A0
A0 A0 A0
P1 P0 P0
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_4(self):
		f=Fichas('P','A','A','A','P','P','P','A','A','A','P','P','P',[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
		expected="""A1 A0 A0
P0 P1 A0
P0 P0 A0
P0 P0 A0
P0 P0 P0
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_5(self):
		f=Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A',[1,0,0,1,0,0,0,0,0,1,0,0,0,0,0])
		expected="""A1 A0 A0
A0 P1 P1
A0 P0 P0
A0 P0 P0
P0 P0 P0
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_6(self):
		f=Fichas('P','P','P','P','P','P','P','A','A','A','A','A','A',[1,0,0,0,0,0,0,0,0,1,0,0,1,0,0])
		expected="""P0 P0 P0
A1 P1 A1
A0 P0 A0
A0 P0 A0
P0 P0 P0
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_7(self):
		f=Fichas('P','A','A','A','P','P','P','P','P','P','P','P','P',[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
		expected="""A1 A0 A0
P0 P1 P0
P0 P0 P0
P0 P0 P0
P0 P0 P0
"""
		self.assertEqual(expected, f.imprimir())

	def test_ficha_8(self):
		f=Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A',[1,0,0,0,0,0,1,1,1,0,0,0,0,0,0])
		expected="""A0 A0 A0
A0 A1 A0
A0 A0 A0
A0 A0 A0
P1 C1 P1
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
		f=Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		expected="""A0 A0 A0
A0 A1 A0
A0 A0 A0
A0 A0 A0
A0 A0 A0
"""
		self.assertEqual(f.imprimir(),expected)


	def test_sacar_ult_ficha(self):
		f=ArrayFichas().sacar_ficha(70)
		expected="""P1 P0 P0
P0 I1 P0
P0 I0 P0
P0 I0 P0
P0 P0 P0
"""
		self.assertEqual(f.imprimir(),expected)

	def test_sacar_medio_ficha(self):
		f=ArrayFichas().sacar_ficha(25)
		expected="""A0 A0 A0
A0 A1 A0
A0 A0 A0
A0 A0 A0
P1 C1 P1
"""
		self.assertEqual(f.imprimir(),expected)


	def eliminar_ficha_saco(self):
		ficha = ArrayFichas().sacar_ficha(26)
		expected = len(ArrayFichas().saco)-1
		ArrayFichas().eliminar_ficha(ficha)
		self.assertEqual(len(ArrayFichas().saco),expected)


 	def test_girar_ficha(self):

 		f=Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
 		#f=Fichas('A','A','A','A','A','A','A','A','A','A','P','P','P',[100000000000100])
 		f.girar()
 		expected="""A0 A0 A0
P1 A1 A0
P0 A0 A0
P0 A0 A0
A0 A0 A0
"""
		self.assertEqual(expected,f.imprimir())

if __name__ == '__main__':
	unittest.main()
