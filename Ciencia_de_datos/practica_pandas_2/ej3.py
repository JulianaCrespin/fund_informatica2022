""" Ejercicio 3
Realizá un programa que agregue datos a un DataFrame vacío.
"""
import pandas as pd
# dato = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]} 

df = pd.DataFrame()
print(df, "\n")

s1 = pd.Series( [1, 4, 3, 4, 5])
print(s1)

df = df.append(s1, ignore_index=True)
print(df)