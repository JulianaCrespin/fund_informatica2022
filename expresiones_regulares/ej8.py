#Escribí un programa que separe y devuelva los caracteres númericos de un string.

import re
string = input("escriba algo: ")
patron = '\d'
lista = []

for caracter in string:
    lista = re.findall(patron, string)

print(lista)
