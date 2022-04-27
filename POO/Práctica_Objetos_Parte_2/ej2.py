# Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def estaEnEquilibrio(self):
    return 150 < self.energia and self.energia < 300