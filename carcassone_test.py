from Fichas import Fichas
import unittest
class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		expected="""TTT
PPP
PPP
PPP
TTT
"""
		self.assertEqual(expected,Fichas('P','T','T','T'
,'T','T','T','P','P','P','P','P','P').imprimir())

	def test_second_ficha(self):
		expected="""TTT
PTP
PTP
PTP
TTT
"""
		self.assertEqual(expected,Fichas('T','T','T','T'
,'T','T','T','P','P','P','P','P','P').imprimir())

	

if __name__ == '__main__':
	unittest.main()
