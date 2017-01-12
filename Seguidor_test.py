from Seguidor import Seguidor
from Seguidor import Grupo_segs
import unittest

class Seguidor_test(unittest.TestCase):

    def test_dame_seguidor_rojo (self):
        expected="S rojo\n";
        self.assertEqual(expected,Seguidor().dame_seguidor("rojo"));

    def test_dame_seguidor_verde (self):
        expected="S verde\n"
        self.assertEqual(expected,Seguidor().dame_seguidor("verde"));

    #Test color que no existe en los seguidores
    def test_seguidor_color_no (self):
        expected="color no existe"
        self.assertEqual(expected,Seguidor().dame_seguidor("rosa"));

    def test_dame_todos(self):
        expected="S rojo\nS verde\nS azul\nS amarillo\nS negro\n";

    def test_rellenar_color(self):
          grupo=Grupo_segs();
          grupo.rellenar_color("rojo")
          expected="S rojo\nS rojo\nS rojo\nS rojo\nS rojo\nS rojo\nS rojo\nS rojo\n"
          self.assertEqual(expected,grupo.print_saco(grupo.seg_r))


    def sacar_seg(self):
        index=random.randint(0,len(self.segs))
        seguidor=self.segs[index]
        self.segs.remove(seguidor)
        return seguidor

if __name__ == '__main__':
    unittest.main()
