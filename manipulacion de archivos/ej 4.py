def contar_palabras(archivo):
    with open(archivo,"r") as file:
        contador = 0
        for line in file:
            for palabra in line:
                contador += 1

    print("la cantidad de palabras es: " + str(contador))