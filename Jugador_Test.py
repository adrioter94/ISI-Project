from Jugador import Jugador

    def test_nuevo_Jugador1(self):
        j = Jugador('Adrian', 'Rojo');
        expected = "Nombre: Adrian, Color: Rojo";
        self.assertEqual(expected, j.imprimir());

    def test_nuevo_Jugador2(self):
        j = Jugador('Sandra', 'Amarillo');
        expected = "Nombre: Sandra, Color: Amarillo";
        self.assertEqual(expected, j.imprimir());
