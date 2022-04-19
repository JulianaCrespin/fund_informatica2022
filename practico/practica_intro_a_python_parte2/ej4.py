#ej 4
peso = int(input("introducir el peso en gramos: "))
costo = 0
if peso > 5000:
    print("pedido rechazado")
else:
    zona = int(input("si la zona es América del Sur presione 1, para america central 2, para america del norte 3, para europa 4, para asia 5: "))
    if zona == 1:
        costo += 10
        costototal= costo * peso
    elif zona == 2:
        costo += 15
        costototal= costo * peso
    elif zona == 3:
        costo += 18
        costototal= costo * peso
    elif zona == 4:
        costo += 24
        costototal= costo * peso
    elif zona == 5:
        costo += 30
        costototal= costo * peso
costototal= costo * peso
print ("el costo es: " + str(costo*peso))
