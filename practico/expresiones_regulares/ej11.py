import re
lista_strings = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
patron = "(P\w*)\s(P\w*)"

for string in lista_strings:
    coincidencia = re.search(patron, string)
if coincidencia is not None:
    print(coincidencia.group())