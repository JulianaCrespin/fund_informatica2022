def semana(): 
    dia = int(input("introduzca numero de dia de la semana: "))
    lista_dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    if dia>7 or dia<1: 
        print("número incorrecto")
    else:
        print(lista_dias[dia-1])
semana()