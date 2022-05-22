# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
def eliminar_saltos(entrada,salida):
    with open(entrada,"r") as f, open(salida,"w") as s:
        for line in f:
            s.write(line.strip("\n"))