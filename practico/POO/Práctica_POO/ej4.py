class Contador:
    def __init__(self,valor):
        self.valor = valor
        
    def inc(self):
        self.valor += 1

    def dis(self):
        self.valor -= 1

    def reset(self):
        self.valor = valor

    def valorActual(self):
        print(self.valor)

    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor