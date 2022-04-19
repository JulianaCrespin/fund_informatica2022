#Escribí un programa que verifique si un string tiene al menos un carácter permitido. 
# Estos caracteres son a-z, A-Z y 0-9.

import re

def caracter_permitido(texto1):
    patron1="[A-Z0-9a-z]+"
    coincidencias=re.findall(patron1, texto1)
    print(coincidencias)
    print(len(coincidencias))


caracter_permitido("A la grande le puse -Cuca-, 123456789")