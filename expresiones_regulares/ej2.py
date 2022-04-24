#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos.
#  Estos caracteres son a-z, A-Z y 0-9.

import re 
texto = "2. El repo de Ana me ayuda con python"
print(re.search('\W', texto))