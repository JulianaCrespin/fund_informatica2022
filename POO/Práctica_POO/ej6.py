class Calculadora:
    def __init__(self):
         self.valor = 0
    
    def cargar(self, numero):
        self.valor = numero

    def sumar(self, valor):
        self.valor += valor

    def restar(self, valor):
        self.valor -= valor

    def multiplicar(self, valor):
        self.valor *= valor

    def valorActual(self):
        return self.valor

        
calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print(calculadora.valorActual())