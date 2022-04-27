# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.
dict1 = {}

def word_counter(archivo):
    frecuencias = {}
    with open(archivo,"r") as file:
        word_list = file.read().split()
        for palabra in word_list:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1 #si no está en el diccionario lo crea y le asigna el valor 1
        for word in frecuencias.keys(): #puedo no poner "keys"
            frecuencias[word] = round(frecuencias[word]) / len(word_list,3)
    print(frecuencias)