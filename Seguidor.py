import random

class Seguidor:


    def __init__(self):
        self.seg="S";
        self.color=["rojo","verde","azul","amarillo","negro"];


    def dame_seguidor(self,col):
        if col in self.color:
            return self.to_String(col);
        return "color no existe"

    def to_String(self,color):
        return self.seg+" "+color+"\n";
