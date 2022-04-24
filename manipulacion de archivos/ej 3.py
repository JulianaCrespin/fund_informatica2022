def guardar_en_lista(archivo, lineas):
    lista=[]
    with open(archivo,"r") as file:
        for line in file:
            lista.append(line)
        for line in file[lineas-1:]:
            print(line)