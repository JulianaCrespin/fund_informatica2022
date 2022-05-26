import requests
# para ver todos
pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
print(pedido.json()) 

# desafio 1
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(pedido.json()) 

# desafio 2
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/400') #me da error porque no hay 400 
print(pedido.json())

# Para saber cuántos hay hago:
pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
print(len(pedido.json()))

# headers me dice toda la metadata, toda la información relacionada a ese pedido 
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/400')
print(pedido.headers) # me devuelve: {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '0', 'Etag': 'W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"', 'Vary': 'Accept-Encoding', 'Date': 'Thu, 26 May 2022 14:38:18 GMT', 'Via': '1.1 vegur'}

# status code returns a number that indicates the status (200 is OK, 404 is Not Found)
pedido = requests.get('https://macowins-server.herokuapp.com/prendas')
print(pedido.status_code) # me devuelve: 200

# desafio 3
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/1")
print(pedido.headers) # me devuelve: {'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '50', 'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 'Vary': 'Accept-Encoding', 'Date': 'Thu, 26 May 2022 14:42:05 GMT', 'Via': '1.1 vegur'}
print(pedido.status_code) #me devuelve: 200

# desafio 4
pedido = requests.get("https://macowins-server.herokuapp.com/prindas/1")
print(pedido.headers) # HTTP/1.1 404 Not Found
print(pedido.status_code) # me devuelve: 404 (is Not Found)

# desafio
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/nueva-funcionalidad-que-a-veces-no-anda-bien")
print(pedido.headers)
print(pedido.content)
print(pedido.status_code) #devuelve: 404

# desafio 5
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/ventas")
print(pedido.json())
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/ventas/2") # me devuelve la venta con id:2

# desafio
pedido = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon') # me devuelve los pantalones #otro ej: /prendas?tipo=saco
print(pedido.json())

# desafio 6
pedido = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
print(pedido.json())

pedido = requests.get('https://macowins-server.herokuapp.com/prendas?talle=40') # talles
pedido = requests.get('https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon') # talle y tipo de prenda

# desafio 7
pedido = requests.get('https://macowins-server.herokuapp.com/prendas?talle=XS&tipo=remera')
print(pedido.json()) #[{'id': 11, 'tipo': 'remera', 'talle': 'XS'}]

"""  
desafio 8

cerebro://recuerdos:3403/recientes#hoy?tema=http 
protocolo: cerebro
dominio: recuerdos
puerto: 3403
ruta: recientes
fragmento: hoy
parametro: tema
valor: http 

"""

# desafio 9 
import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

""" desafio 10
HTTP/1.1 200 OK
X-Powered-By: Express
Vary: Origin, Accept-Encoding
Access-Control-Allow-Credentials: true
Cache-Control: no-cache
Pragma: no-cache
Expires: -1
X-Total-Count: 100
Access-Control-Expose-Headers: X-Total-Count, Link
Link: <https://macowins-server.herokuapp.com/posts/?_page=1>; rel="first", <https://macowins-server.herokuapp.com/posts/?_page=2>; rel="next", <https://macowins-server.herokuapp.com/posts/?_page=10>; rel="last"
X-Content-Type-Options: nosniff
Content-Type: application/json; charset=utf-8
Content-Length: 794
ETag: W/"31a-kfX25hKekB1DHqT0GE68BdzBP1Q"
Date: Sun, 19 Apr 2020 20:18:21 GMT
Connection: keep-alive 
"""

# desafio 10 
r = requests.get("https://macowins-server.herokuapp.com/home")
print(r.headers) #{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '0', 'Etag': 'W/"0-2jmj7l5rSw0yVb/vlWAYkK/YBwk"', 'Vary': 'Accept-Encoding', 'Date': 'Thu, 26 May 2022 15:43:48 GMT', 'Via': '1.1 vegur'}
# 'Content-Type': 'text/html; charset=utf-8'

# desafio 
data = {'id': 21}
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
# desafio 12
print(r.status_code) #devuelve 500 cuando un estado es creado

data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=data)

import json, requests
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)
print(r.status_code) #201
requests.get('https://macowins-server.herokuapp.com/prendas').json()
