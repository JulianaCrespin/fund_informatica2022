import re
string = "hola  mi nombre es    sol bertinat"
patron = "[\s]"
print(re.sub(patron, ";", string))