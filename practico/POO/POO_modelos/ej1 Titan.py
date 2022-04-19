class Titan():
    def __init__(self, salud): #definir atributos
        self.salud = salud
        self.correr = False #no sabe correr

    def salud_actual(self):
        return self.salud
    
    def recibir_ataque(self,cantidad):
        self.salud -= 1.5 * cantidad

    def grito(self):
        return "¡Aaaarrrg!"

    def cuantas_casas(self):
        return (self.salud * 8 / 100)

    def destruir_casas(self):
        if (self.cuantas_casas() > 1):
            if ((self.cuantas_casas() % 1) > 0):
                self.salud -= (self.cuantas_casas() // 1) * 12.5           
            else:
                self.salud -= (self.cuantas_casas() - 1) * 12.5
        else:
            print("No puede destruir ninguna casa")

def esta_vivo(self):
    return 