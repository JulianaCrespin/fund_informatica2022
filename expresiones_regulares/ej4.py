#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado
#  (el string no debe contener espacios).

import re
# string = "Realizá un programa que encuentre una palabra unida a otra con un guion_bajo"
# patron = '\w' + '_' + '\w'
# print(re.search(patron, string)) 

def palabras_unidas(texto):
    patron = '\w' + '_' + '\w'
    print(re.search(patron, texto)) 

palabras_unidas("Realizá un programa que encuentre una palabra unida a otra con un guion_bajo")