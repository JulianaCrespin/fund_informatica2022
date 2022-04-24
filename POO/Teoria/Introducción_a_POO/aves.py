class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia < 10

class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_debil(self):
    return self.energia < 50

class Entrenador:
    """Un entrenador tiene un equipo y puede admitir nuevos animal alado a su equipo""" 
    def __init__(self,equipo):
        self.equipo = equipo

    def el_equipo(self):
        return self.equipo
 
    def agregar_animal_alado(self,dragon):
        """Este metodo toma un objeto animal alado que tendra todos los atributos de esa clase"""
        self.equipo.append(dragon)

    def entrenar_dragon(self,dragon):
        for i in range(20):
            dragon.volar_en_circulos()
        dragon.comer_peces(3)

    def entrenar_equipo(self):
        for dragon in self.equipo:
            self.entrenar_dragon(self,dragon)


pepita = Golondrina(100)
juanita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
chimuelo = Dragon(200, 2000)

hipo = Entrenador([roberta])