# Escribí un programa que lea un archivo e imprima las primeras n líneas.
def imprimir_primeras_lineas(lineas, archivo):
    with open(archivo,"r") as file:
        for i in range(0, lineas):
            for line in file:
                print(line)


def imprimir_primeras_lineas(lineas, archivo):
    with open(archivo,"r") as file:
            print(file[:lineas])