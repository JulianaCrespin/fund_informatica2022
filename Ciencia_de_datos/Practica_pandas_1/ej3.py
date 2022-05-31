""" Ejercicio 3
Escribí un programa para convertir un diccionario a una serie de Pandas.
listas son series
diccionarios son df
"""
import pandas as pd
dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
nueva_serie = pd.Series(dict1)
print(nueva_serie)