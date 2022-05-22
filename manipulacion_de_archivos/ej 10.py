# Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
# os.listdir() # obtengo todos los archivos de una carpeta
import glob
import os
def funcion1(archivo, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob("*.txt") #primer glob: nombre biblioteca 2do glob:nombre del método

    with open(archivo, "a") as s:
        for f in lista_txt:
            file = open(f,"r")
            s.write(file.read())
            file.close()