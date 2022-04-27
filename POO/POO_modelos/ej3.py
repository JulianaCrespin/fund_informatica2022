# Los estudiantes (como ustedes) son como cualquier persona, las cuales recuperan energía si duermen o si comen, o la gastan al hacer ejercicio, sin embargo en particular los estudiantes también gastan energía al estudiar y se sienten felices al aprobar algún exámen. Resumiendo, las personan pueden:

# Decirnos cuánta energía tienen.
# Recuperar el máximo de energía (100) al dormir 8 horas, o el proporcional si duermen menos (si duermen 4 ganan la mitad de energía, es decir 50).
# Recuperar energía al comer, ganando de esta manera 10 puntos.
# Gastar energía al hacer ejercicio, siendo un gasto de 25 puntos por cada media hora de ejercicio.
# Como estado de ánimo pueden estar felices o no, pero por defecto no están felices.
# Además los estudiantes tienen el siguiente comportamiento:

# Al estudiar su energía disminuye 20 puntos por cada hora de estudio.
# Si aprueban su estado de ánimo pasa a ser "Feliz".
# Definí las clases Persona y Estudiante con los atributos y métodos correspondientes y hacé que esta última herede de la primera.

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