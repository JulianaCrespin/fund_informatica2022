# Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:

# implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

# comprobar el código que se escribió con esta secuencia:

# definir un ornitólogo, dos golondrinas y dos gorriones,
# inicializar las aves con valores conocidos,
# decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
# decirle al ornitólogo que realice su rutina sobre aves,
# verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.

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