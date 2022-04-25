class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible
    
    def combustibleActual(self):
        return self.combustible

    def entran(self, personas):
        return personas <= self.maxPersonas()

    def cargarCombustible(self, cantidad):
        self.combustible += cantidad


class Moto(MedioDeTransporte):
    def maxPersonas(self):
        return 2

    def recorrer(self, kms):
        self.combustible -= kms

class Auto(MedioDeTransporte):
    def maxPersonas(self):
        return 5

    def recorrer(self, kms):
        self.combustible -= kms*0.5

auto = Auto(100)
moto = Moto(89)
print(auto.entran(3))
auto.recorrer(50)
print(auto.combustibleActual())