# Escribí un programa que lea un archivo, guarde las líneas 
# del archivo en una lista y luego imprima las n últimas.
def guardar_en_lista(archivo, lineas):
    lista=[]
    with open(archivo,"r") as file:
        for line in file:
            lista.append(line)
        for line in file[lineas-1:]:
            print(line)