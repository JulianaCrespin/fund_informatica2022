#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
def contar_palabras(archivo):
    with open(archivo,"r") as file:
        contador = 0
        for line in file:
            for palabra in line:
                contador += 1

    print("la cantidad de palabras es: " + str(contador))