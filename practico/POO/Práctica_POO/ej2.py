class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
      if self.energia > 10:
          self.energia -= 10 + kms
      # else:
      #     print("no tiene energia suficiente")