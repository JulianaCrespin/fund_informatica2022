import re
string = "la palabra hola esta en la frase"
patron = "-(.*?)-"
print(re.findall(patron, string))