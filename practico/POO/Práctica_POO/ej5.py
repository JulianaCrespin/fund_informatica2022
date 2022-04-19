class Contador:
    def __init__(self,valor):
        self.valor = valor
        comando = "iniciar"

    def inc(self):
        self.valor += 1
        comando = "incremento"

    def dis(self):
        self.valor -= 1
        comando ="disminución"

    def reset(self):
        self.valor = valor
        comando = "reset"

    def valorActual(self):
        print(self.valor)
        comando = "chequear valor"

    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor
        comando = "actualización"

    def ultimoComando(self):
        print(comando)
        comando = "disminucion"