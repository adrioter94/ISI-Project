from Fichas import Fichas
from Array_Fichas import ArrayFichas
import unittest

class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		f=Fichas('P','A','A','A','A','A','A','P','P','P','P','P','P')
		expected="""AAA
PPP
PPP
PPP
AAA
"""
		self.assertEqual(expected,f.imprimir(f.territorio))

	def test_second_ficha(self):
		f=Fichas('A','A','A','A','A','A','A','P','P','P','P','P','P')
		expected="""AAA
PAP
PAP
PAP
AAA
"""

		self.assertEqual(expected,f.imprimir(f.territorio))


	def test_ficha_3(self):
		f=Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A')
		expected="""AAA
AAA
AAA
AAA
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_4(self):
		f=Fichas('P','A','A','A','P','C','P','P','C','P','A','A','A')
		expected="""AAA
APP
APC
APP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_5(self):
		f=Fichas('I','P','P','P','P','C','P','P','P','P','P','P','P')
		expected="""PPP
PIP
PIP
PIP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_6(self):
		f=Fichas('P','A','A','A','P','C','P','P','C','P','P','P','P')
		expected="""AAA
PPP
PPC
PPP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_7(self):
		f=Fichas('P','A','A','A','P','C','P','P','P','P','P','C','P')
		expected="""AAA
PPP
CPP
PPP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_8(self):
		f=Fichas('B','A','A','A','P','C','P','P','C','P','P','C','P')
		expected="""AAA
PBP
CBC
PBP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_9(self):
		f= Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P')
		expected="""AAA
PCP
CCC
PCP
PPP
"""
		self.assertEqual(expected,f.imprimir(f.territorio))

	def test_ficha_10(self):
		f=Fichas('I','P','P','P','P','P','P','P','P','P','P','P','P')
		expected="""PPP
PIP
PIP
PIP
PPP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_11(self):
		f = Fichas('C','P','P','P','P','C','P','P','P','P','P','C','P')
		expected="""PPP
PCP
CCP
PCP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_12(self):
		f=Fichas('C','P','C','P','P','C','P','P','P','P','P','P','P')
		expected="""PCP
PCP
PCP
PCP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_13(self):
		f=Fichas('B','P','P','P','P','C','P','P','C','P','P','C','P')
		expected="""PPP
PBP
CBC
PBP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))

	def test_ficha_14(self):
		f=Fichas('B','P','C','P','P','C','P','P','C','P','P','C','P')
		expected="""PCP
PBP
CBC
PBP
PCP
"""
		self.assertEqual(expected, f.imprimir(f.territorio))


	def test_long_array(self):

		self.assertEqual(len(ArrayFichas().saco),71)

	def test_sacar_ficha_primera(self):
		f=ArrayFichas().sacar_ficha(0)
		expected="""AAA
AAA
AAA
AAA
AAA
"""
		self.assertEqual(f.imprimir(f.territorio),expected)


	def test_sacar_ult_ficha(self):
		f=ArrayFichas().sacar_ficha(70)
		expected="""PPP
PBP
CBC
PBP
PCP
"""
		self.assertEqual(f.imprimir(f.territorio),expected)

	def test_sacar_medio_ficha(self):
		f=ArrayFichas().sacar_ficha(25)
		expected="""AAA
AAA
AAA
AAA
PCP
"""
		self.assertEqual(f.imprimir(f.territorio),expected)


	def eliminar_ficha_saco(self):
		ficha = ArrayFichas().sacar_ficha(26)
		expected = len(ArrayFichas().saco)-1
		ArrayFichas().eliminar_ficha(ficha)
		self.assertEqual(len(ArrayFichas().saco),expected)


	def test_girar_ficha(self):
		f=Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A')
		f.girar()
		expected ="""AAA
PAA
PAA
PAA
AAA
"""
		self.assertEqual(expected,f.imprimir(f.territorio))

if __name__ == '__main__':
	unittest.main()
