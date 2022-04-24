#Escribí un programa que diga si un string empieza con un número específico.

import re

def comienzo(texto, numero):
    patron = ("^" + str(numero))
    if re.match(patron,texto) is not None:
        print("el string comienza con el numero " + str(numero))
    else:
        print("el string comienza con el numero " + str(numero))

comienzo("8 fgdhsjklñkjhg", 8)

