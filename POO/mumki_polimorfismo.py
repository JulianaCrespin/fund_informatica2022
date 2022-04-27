### Zombis
class Sobreviviente:
  def __init__(self, adrenalina):
    self.adrenalina = adrenalina
    
  def atacar(self, tipo_de_zombi):
    if tipo_de_zombi.es_un_peligro() is not True:
      tipo_de_zombi.recibir_danio(self.adrenalina/2)
      self.adrenalina += 20
    else:
      raise Exception("Es peligroso atacar a este zombi")


### 12- Chau apocalipsis

class Pasta:
  def __init__(self):
    self.ajies = 0
  
  def ser_picanteado(self):
    if self.ajies < 10:
      self.ajies += 5
    else:
      raise Exception("El plato ya está demasiado picante")
  
  def ser_suavizado(self):
    self.ajies -= 1
  
class Pizza:
  def __init__(self):
    self.condimento = "adobo"
    
  def ser_picanteado(self):
    if self.condimento != "cayena":
      self.condimento = "cayena"
    else:
      raise Exception("El plato ya está demasiado picante")

  def ser_suavizado(self):
    self.condimento = "oregano"
    
class Chef:
  def __init__(self, plato_del_dia):
    self.plato_del_dia = plato_del_dia
    
  def picantear(self):
    self.plato_del_dia.ser_picanteado()
    
  
class AyudanteDeCocina:
  def suavizar(self, plato):
    plato.ser_suavizado()

class Perro:
  def cruzarse_con(self, un_perro):
    self.mover_la_cola()
    self.oler(un_perro)

class PerroCascarrabias(Perro):
  def cruzarse_con(self, un_perro):
    super().cruzarse_con(un_perro)
    self.ladrar()

    