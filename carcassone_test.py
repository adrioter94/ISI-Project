from Fichas import Fichas
import unittest
class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		expected="""TTT
PPP
PPP
PPP
TTT"""
		self.assertEqual(expected,Fichas().imprimir())

if __name__ == '__main__':
	unittest.main()
