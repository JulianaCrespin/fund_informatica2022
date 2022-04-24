class Contador:
    def __init__(self,valor_actual):
        self.valor = valor_actual
        
    def inc(self):
        self.valor += 1

    def dis(self):
        self.valor -= 1

    def reset(self):
        self.valor = self.valor_actual

    def valorActual(self):
        print(self.valor)

    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor

contador=Contador(10)

contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valorActual())
contador.valorNuevo(27)
contador.dis()
contador.dis()
print(contador.valorActual())
