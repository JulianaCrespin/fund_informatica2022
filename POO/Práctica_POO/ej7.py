class Gorriones:
    def __init__(self):
        self.gramosActuales = 0
        self.kmsActuales = 0
        self.listaGramos = []
        self.listaKms = []
    #El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, 
    # por la cantidad total de gramos de comida que ingiere. 
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

# CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió.
    def CSSP(self):
        return max(self.listaKms) / max(self.listaGramos)

#El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió
    def CSSV(self):
        return len(self.listaKms) / len(self.listaGramos)

    def estaEnEquilibrio(self):
        return 0.5 <= self.CSS() <=2
        #self.CSS > 0.5 and self.CSS < 2