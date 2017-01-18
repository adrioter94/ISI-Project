from Seguidor import Seguidor
import unittest

class Seguidor_test(unittest.TestCase):

    # test pido seguidor de color y me devuelve ese seguidor de ese color si esta en colores(hay 5 colores).
    def test_dame_seguidor_rojo (self):
        expected="S rojo\n";
        self.assertEqual(expected,Seguidor().dame_seguidor("rojo"));


    def test_dame_seguidor_verde (self):
           expected="S verde\n"
           self.assertEqual(expected,Seguidor().dame_seguidor("verde"));


   # Test color que no existe en los seguidores
    def test_seguidor_color_no (self):
        expected="color no existe"
        self.assertEqual(expected,Seguidor().dame_seguidor("rosa"));

    # Test que muestra los colores de los seguidores posibles
    def test_dame_todos(self):
       expected="S rojo\nS verde\nS azul\nS amarillo\nS negro\n";
       self.assertEqual(expected,Seguidor().dame_todos())

if __name__ == '__main__':
    unittest.main()
