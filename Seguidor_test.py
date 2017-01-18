from Seguidor import Seguidor
from Seguidor import Grupo_segs
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

    # test para que me devuelva 8 seguidores rojo
    def test_rellenar_color(self):
              grupo=Grupo_segs();
              grupo.rellenar_color("rojo")
              expected="S rojo\nS rojo\nS rojo\nS rojo\nS rojo\nS rojo\nS rojo\nS rojo\n"
              self.assertEqual(expected,grupo.print_saco(grupo.seg_r))


    # test para que me devuelva 8 seguidores azul
    def test_rellenar_color(self):
              grupo=Grupo_segs();
              grupo.rellenar_color("azul")
              expected="S azul\nS azul\nS azul\nS azul\nS azul\nS azul\nS azul\nS azul\n"
              self.assertEqual(expected,grupo.print_saco(grupo.seg_azu))



    def test_sacar_seguidor(self):
         grupo=Grupo_segs();
         grupo.rellenar_color("rojo")
         grupo.sacar_seg(grupo.seg_r)
         self.assertEqual(len(grupo.seg_r),7)

         grupo.sacar_seg(grupo.seg_r)
         self.assertEqual(len(grupo.seg_r),6)


if __name__ == '__main__':
    unittest.main()
