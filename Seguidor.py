import random

class Grupo_segs:

  def __init__(self):
      self.seg_r=[];
      self.seg_v=[];
      self.seg_azu=[];
      self.seg_ama=[];
      self.seg_neg=[];
      self.num=40;

  def rellenar_color (self,color):
      if color == "rojo":
          for n in range(self.num/len(Seguidor().color)):
              self.seg_r.append(Seguidor().dame_seguidor(color))
      elif color == "verde":
          for n in range(self.num/len(Seguidor().color)):
              self.seg_r.append(Seguidor().dame_seguidor(color))
      elif color == "azul":
        for n in range(self.num/len(Seguidor().color)):
            self.seg_azu.append(Seguidor().dame_seguidor(color))
      elif color == "ama":
         for n in range(self.num/len(Seguidor().color)):
             self.seg_ama.append(Seguidor().dame_seguidor(color))
      elif color == "neg":
        for n in range(self.num/len(Seguidor().color)):
            self.seg_neg.append(Seguidor().dame_seguidor(color))
      else:
        print "Color no disponible"

  def sacar_seg(self,seg):
        seguidor=seg.pop();
        return seguidor

  def print_saco(self,segs):
      saco=""
      for s in segs:

          saco+=s;
      return saco


class Seguidor:

    def __init__(self):
        self.seg="S";
        self.color=["rojo","verde","azul","amarillo","negro"];


    def dame_seguidor(self,col):
        if col in self.color:
            return self.to_String(col);
        return "color no existe"


    def dame_todos(self):
        result=""
        for s in self.color:
            result+=Seguidor().to_String(s)
        return result

    def to_String(self,color):
        return self.seg+" "+color+"\n";
