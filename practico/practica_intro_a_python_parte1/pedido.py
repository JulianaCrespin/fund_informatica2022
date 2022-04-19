pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
pedido.keys()
lista_comensales = pedido.keys()
def empanadas_por_gusto():
  for i in lista_comensales:
    print(pedido[i])