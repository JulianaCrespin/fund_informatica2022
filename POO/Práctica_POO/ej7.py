class Gorriones:
    def __init__(self, energia):
        self.energia = energia
        self.vuelo = 0
        self.comida = 0
    #El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, 
    # por la cantidad total de gramos de comida que ingiere. 
    def volar(self, km):
        self.vuelo += km

    def comer(self, gramos):
        self.comida += gramos

    def CSS(self):
        self.vuelo / self.comida
# CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió.
    def CSSP(self, mayor_vuelo, mayor_comida):
        self.mayor_vuelo /self.mayor_comida

    def CSSV(self):
        self.cantidad_vuelos / self.cantidad_comidas

    def equilibrio(self):
        self.CSS > 0.5 and self.CSS < 2