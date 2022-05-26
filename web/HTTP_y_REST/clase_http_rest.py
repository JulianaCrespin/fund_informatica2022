import requests
# para ver todos
# pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
# print(pedido.json()) 

# #1
# pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
# print(pedido.json())

# #2
# pedido = requests.get("https://macowins-server.herokuapp.com/prendas/400")
# print(pedido.json())
# # no hay
# # Para saber cuántos hay hago:
# pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
# print(len(pedido.json()))
# print(pedido.headers) # me dice toda la metadata, toda la información relacionada a ese pedido 

#3
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(pedido.json())

# #400
# pedido = requests.get("https://macowins-server.herokuapp.com/prendas/400")
# print(pedido) # me da <Response [404]> que es Error404

# pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
# # pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
# print(pedido.status_code) #status code
