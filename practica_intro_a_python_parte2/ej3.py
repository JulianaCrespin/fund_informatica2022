def dado():
    numero = int(input("ingrese número del dado: "))
    if numero < 1 or numero > 6:
        print("número incorrecto")
    else:
        print("el número que está en la cara opuesta del dado es " + str(7-numero))

dado()