#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, 
# mayúsculas, espacios y números.


import re
string = input("ingrese una frase: ")
patron = "[a-zA-Z0-9(\s)]"
coincidencias = []

for caracter in string:
    coincidencias.append(re.findall(patron, caracter))
  
    if len(coincidencias) == len(string):
        print("todos los caracteres de la frase son o letras mayusculas, o letras minusculas, o numeros, o espacios")
    else:
        print("al menos un caracter no es una letra mayuscula o minuscula, numero o espacio")
