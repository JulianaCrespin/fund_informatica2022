class Contador:
    def __init__(self, valor):
        self.valor = valor
        self.valorInicial = valor

    def inc(self):
        self.valor += 1

    def dis(self):
        self.valor -= 1

    def reset(self):
        self.valor = self.valorInicial

    def valorActual(self):
        return self.valor

    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor

contador = Contador(10)

# contador.inc()
# contador.inc()
# contador.dis()
# contador.inc()
# print(contador.valorActual())
# contador.valorNuevo(27)
# contador.dis()
# contador.dis()
# print(contador.valorActual())


contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valorActual())
contador.reset()
print(contador.valorActual())