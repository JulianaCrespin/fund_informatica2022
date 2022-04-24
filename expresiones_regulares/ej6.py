#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

import re
# strings = ["hola", "te", "hoy"]
# frase = "hola como te sentis hoy?"
# for palabra in strings:
#     patron = palabra
# if re.search(patron, frase) is not None:
#     print("la palabra esta en la frase")
# else:
#     print("la palabra no esta en la frase")

def encontrar(lista, frase):
    for palabra in lista:
        patron = palabra
        if re.search(palabra, frase) is not None:
            print("la palabra " +  palabra + " esta en la frase")
        else:
            print("la palabra " + palabra + "NO esta en la frase")

encontrar(["hola", "te", "hofghjk"], "hola como te sentis hoy?")