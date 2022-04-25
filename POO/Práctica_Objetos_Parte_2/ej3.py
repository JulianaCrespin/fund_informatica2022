class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_en_equilibrio(self):
    return 150 < self.energia and self.energia < 300

class Gorrion:
    def __init__(self):
        self.gramosActuales = 0
        self.kmsActuales = 0
        self.listaGramos = []
        self.listaKms = []

    def volar(self, kms):
        self.listaKms.append(kms)
        self.kmsActuales += kms

    def comer(self, gramos):
        self.listaGramos.append(gramos)
        self.gramosActuales += gramos

    def CSS(self):
        if self.gramosActuales > 0:
            self.kmsActuales / self.gramosActuales
        else:
            return None

    def CSSP(self):
        return max(self.listaKms) / max(self.listaGramos)

    def CSSV(self):
        return len(self.listaKms) / len(self.listaGramos)

    def estaEnEquilibrio(self):
        return 0.5 <= self.CSS() <=2
    
class Ornitologo:
    def __init__(self):
        self.aves = []

    def estudiarAve(self, ave):
        self.aves.append(ave)

    def AvesEnEstudio(self):
        return self.aves

    def avesEnEquilibrio(self):
        return [self.aves[i].estaEnEquilibrio() for i in range(len(self.aves))]


    def realizarRutinaSobreAves(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]
    
ornitologo = Ornitologo()
golondrina1 = Golondrina(80)
golondrina2 = Golondrina(75)
gorrion1 = Gorrion()
gorrion2 = Gorrion()

print("la energia inicial de la golondrina es: ", golondrina1.energia)
ornitologo.estudiarAve(golondrina1)
ornitologo.estudiarAve(gorrion1)
ornitologo.estudiarAve(gorrion2)
print(ornitologo.AvesEnEstudio())
ornitologo.realizarRutinaSobreAves()
print("la energia final de la golondrina es: ", golondrina1.energia)