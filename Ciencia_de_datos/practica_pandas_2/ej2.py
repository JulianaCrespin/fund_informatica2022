""" Ejercicio 2
Escribí un programa que guarde en una lista una columna de un DataFrame."""
import pandas as pd
dato = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]} 
df = pd.DataFrame(dato)
print(df, "\n")
lista = (df[1]).to_list()
print(lista)