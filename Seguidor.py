import random


class Seguidor:


    def __init__(self):
        self.seg="S";

    def dame_todos(self):
        for s in Color.color():
            return dame_seguidor(s)

    def dame_seguidor(self,col):
        if col in Color().color:
            return self.to_String(col);
        return "color no existe"

    def to_String(self,color):
        return self.seg+" "+color+"\n";

class Color:

    def __init__(self):
        self.color=["rojo","verde","azul","amarillo","negro"];
