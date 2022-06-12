"""Ejercicio 5
Realizá un programa que verifique si una columna dada se encuentra presente en un DataFrame."""
import pandas as pd
dato = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]} 
df = pd.DataFrame(dato)
# print(df, "\n")
print(df.columns)
if 3 in df.columns:
    print("si")
else:
    print("no")
if 5 in df.columns:
    print("si")
else:
    print("no")