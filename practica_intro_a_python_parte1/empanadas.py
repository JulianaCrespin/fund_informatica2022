pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
pedido.keys()
lista_comensales = pedido.keys()
def empanadas_por_gusto():
  for i in lista_comensales:
    print(pedido[i])
#Ahora solo nos faltaría sumar +1 a la lista veggies si el valor es "veganas" o sumar +1 a la lista no_veggies si el valor se corresponde con "no veggie".
no_veggies= []
veganas=[]
def empanadas