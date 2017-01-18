from Seguidor import Seguidor
import unittest

class Seguidor_test(unittest.TestCase):

    # test pido seguidor de color y me devuelve ese seguidor de ese color si esta en colores(hay 5 colores).
    def test_dame_seguidor_rojo (self):
        expected="S rojo\n";
        self.assertEqual(expected,Seguidor().dame_seguidor("rojo"));


if __name__ == '__main__':
    unittest.main()
