""" Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.

""" 
import pandas as pd
serie1 = [3, 7, 12, 15, 21]
serie2 = [1, 4, 10, 14, 19] 
ds1 = pd.Series(serie1)
ds2 = pd.Series(serie2)

print("Suma:")
print(ds1 + ds2)
print("\nResta:")
print(ds1-ds2)
print("\nMultiplicación:")
print(ds1 * ds2)
print("\nDivisión:")
print(ds1 / ds2)