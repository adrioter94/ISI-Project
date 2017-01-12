from Fichas import Fichas
from Fichas import ArrayFichas
import unittest

class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		expected="""AAA
PPP
PPP
PPP
AAA
"""
		self.assertEqual(expected,Fichas('P','A','A','A'
,'A','A','A','P','P','P','P','P','P').imprimir())

	def test_second_ficha(self):
		expected="""AAA
PAP
PAP
PAP
AAA
"""

		self.assertEqual(expected,Fichas('A','A','A','A'
,'A','A','A','P','P','P','P','P','P').imprimir())

	def test_create_array_of_23(self):
		expected ="""AAA
AAA
AAA
AAA
AAA
AAA
AAA
AAA
AAA
PPP
AAA
AAA
AAA
AAA
PPP
AAA
AAA
AAA
AAA
PPP
AAA
AAA
AAA
AAA
PPP
PPP
AAA
AAA
AAA
PPP
PPP
AAA
AAA
AAA
PPP
PPP
AAA
AAA
AAA
PPP
AAA
PPA
PPA
PPA
PPP
AAA
PPA
PPA
PPA
PPP
AAA
PPA
PPA
PPA
PPP
AAA
PPA
PPA
PPA
PPP
AAA
PPA
PPA
PPA
PPP
AAA
APP
APP
APP
PPP
AAA
APP
APP
APP
PPP
PPP
APA
APA
APA
PPP
PPP
APA
APA
APA
PPP
PPP
APA
APA
APA
PPP
AAA
PPP
PPP
PPP
PPP
AAA
PPP
PPP
PPP
PPP
AAA
PPP
PPP
PPP
PPP
AAA
PPP
PPP
PPP
PPP
AAA
PPP
PPP
PPP
PPP
"""
		
		self.assertEqual(expected,ArrayFichas().imprimir())

if __name__ == '__main__':
	unittest.main()
