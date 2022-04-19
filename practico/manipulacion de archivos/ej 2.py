def imprimir_primeras_lineas(lineas,archivo):
    with open(archivo,"r") as file:
        for i in range(0, lineas):
            for line in file:
                print(line)