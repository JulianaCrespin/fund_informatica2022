# Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

# comienzan con una cantidad que podemos establecer de combustible

# los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido

# las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

# pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

# saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

# Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

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