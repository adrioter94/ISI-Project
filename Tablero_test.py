
from tablero import Tablero
import unittest

def test_tablero_filas(self):
  self.assertEqual(72,len(Tablero().tablero))
def test_tablero_columnas(self):
  self.assertEqual(72,len(Tablero().tablero[0]))
def test_tablero_matriz(self):
  i = 0
  z = 0
  expected = ""
  while z < 72:
    while i < 72:
      expected += 'X'
      i = i + 1
    i = 0
    expected += '\n'
    z = z +1
  self.assertEqual(expected,Tablero().imprimir_tablero())


if __name__ == '__main__':
	unittest.main()
