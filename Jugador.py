class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        #Color in ['azul', 'amarillo', 'rojo', 'negro', 'verde']
        self.turno = False
        self.puntuacion = 0
        self.seguidores = 8

    def imprimir(self):
        return("Nombre: " + self.nombre + ", Color: " + self.color)
