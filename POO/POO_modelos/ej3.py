class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.feliz = False
        # self.estadoDeAnimo = "No feliz"
    
    def energia_actual(self):
        return self.energia

    def dormir(self, horas):
        self.energia += horas * 50 / 4
        if self.energia > 100:
            self.energia = 100
        else:
            return self.energia
        
    def comer(self):
        self.energia += 10
        if self.energia > 100:
            self.energia = 100
        else:
            return self.energia

    def hacer_ejercicio(self, minutos):
        media_hora = int(minutos/30)
        self.energia -= media_hora * 25

class Estudiante(Persona):
    def estudiar(self, horas):
        self.energia -= 20 * horas

    def aprobar(self):
        self.feliz = True
        return self.feliz
        # self.estadoDeAnimo = "Feliz"

estudiante = Estudiante(100)

estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())