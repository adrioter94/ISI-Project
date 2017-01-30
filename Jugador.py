#Clase que representa a un jugador
class Jugador:

    #Cada jugador tiene la siguiente informacion: nombre, color de sus seguidores,
    #numero de seguidores en un determinado momento u su puntuacion.
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        #Color in ['azul', 'amarillo', 'rojo', 'negro', 'verde']
        self.turno = False
        self.puntuacion = 0
        self.seguidores = 8

    #Imprime al jugador como nombre + color
    def imprimir(self):
        return("Nombre: " + self.nombre + ", Color: " + self.color)
