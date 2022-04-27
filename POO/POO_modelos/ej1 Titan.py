# En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima o un número proporcional si su salud es menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes. Además instanciá a un Titan y ejecutá las siguientes líneas:
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


titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())
# cuyo resultado tiene que ser:

# True
# 55
# 4.4
# "¡Aaaarrrg!"
# 5.0
# False
