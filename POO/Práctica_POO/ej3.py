class Notebook:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, porcentaje):
        return self.precio - (self.precio * porcentaje)

hp = Notebook("HP","Lean" , 1000)
macbook = Notebook("Apple", "Air", 2000)

print(hp.descuento(0.3))