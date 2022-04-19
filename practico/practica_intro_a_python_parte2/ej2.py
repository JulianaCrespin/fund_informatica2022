def analizar_numero():
    numero = int(input("introduzca un número: "))
    print(signo(numero))
    print(paridad(numero))

def signo(numero):    
    if numero > 0:
        return("es positivo")
    elif numero == 0:
        return("es cero")
    else:
        return("es negativo")
        
def paridad(numero):
    if numero % 2 != 0:
        return("es impar")
    else: 
        return("es par")

analizar_numero()