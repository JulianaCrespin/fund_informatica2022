class Enterprise:
    def __init__(self):
        self.potencia = 50
        self.coraza = 5
    
    def potencia(self):
        return self.potencia
    
    def coraza(self):
        return self.coraza

    def encontrarPilaAtomica(self):
        self.potencia += 25
        if self.potencia > 100:
            self.potencia = 100

    def encontrarEscudo(self):
        self.coraza += 10
        if self.coraza > 20:
            self.coraza = 20

    def recibirAtaque(self, puntos):
        if self.coraza >= puntos:
            self.coraza -= puntos
        else:
            puntos_restantes = puntos - self.coraza
            self.potencia -= puntos_restantes
            self.coraza = 0
            if self.potencia < 0:
                self.potencia = 0

    def fortalezaDefensiva(self):
        return self.coraza + self.potencia

    def necesitaFortalecerse(self):
        self.coraza == 0 and self.potencia < 20

    def fortalezaOfensiva(self):
        if self.potencia < 20:
            return 0
        else:
            return (self.potencia - 20) / 2.

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
# print(enterprise.potencia())
# print(enterprise.coraza())