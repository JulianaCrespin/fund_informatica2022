""" Ejercicio 4
Escribí un programa que elimine las primeras n filas de un DataFrame. Pista: el DataFrame original no debe modificarse."""
import pandas as pd
dato = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]} 
df = pd.DataFrame(dato)
print(df, "\n")
df1 = df.loc[1:]
print(df1)