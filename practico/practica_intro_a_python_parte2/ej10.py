contadores = {}
cadena = input("escribí una cadena: ")
for caracter in cadena:
    if caracter in contadores:
        contadores[caracter]+=1
    else:
        contadores[caracter]=1
for clave,valor in contadores.items():
    print(clave,valor)