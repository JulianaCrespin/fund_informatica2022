""""Ejercicio 2
Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series 
de números de Pandas.
"""
import pandas as pd
serie1 = [3, 7, 9, 14, 25]
serie2 = [1, 7, 10, 16, 19]
ds1 = pd.Series(serie1)
ds2 = pd.Series(serie2)

print("\nSon iguales")
print(ds1 == ds2)
print("Serie 1 es mayor a Serie 2")
print(ds1 > ds2)
print("\nSerie 1 es menor a Serie 2")
print(ds1 < ds2)

