""" Ciencia de datos """
import pandas as pd
personas = pd.read_csv("personas_2011.csv", sep=";") # con archivo en mi carpeta
# personas = pd.read_csv(r"C:\Users\usuario\Documents\personas_2011.csv", sep=";")
print(personas)
print(personas.head()) #imprimo 5 rows del df
print(personas.head(10))
personas.info() #qué tipo de datos tengo en cada columna: str, float, int
print(personas.describe()) #me hace un analisis de todas las columnas numéricas: count, promedio, min, max, cuartiles
print(personas.edad)
print(personas['edad'].head())
print(personas.loc[2, 'persona_id'])
print(personas.loc[2, 'edad']) 
print(personas['edad'].tolist())
#4
print(personas["seniority_level"]) #booleano
print(personas["seniority_level"].count()) #me dice cuantos seniority levels hay
print(personas.groupby("seniority_level").count()) #me agrupa todas las que tienen el mismo valor de seniority level 
print(personas.groupby("seniority_level").count("A"), "contar A")
print(personas.groupby("seniority_level")[["persona_id"]].count()) #me agrupa por categoría de seniority level y me dice cuántos id tiene cada categoria
personas[personas["sexo_id"] == 2] # 1) llamo a la tabla 2)llamo a la columna #para que me aparezcan solo los sexo_id que son 2
print(personas['edad'] * 2)   #la edad * 2
print(personas['edad'] + 2)   #la edad +2
print(personas['edad'] > 2 )  #un booleano. 
print(personas[personas['edad'] < 35 ])
# 5
personas.info()
# Filtro personas de sexo == 1 y menor de edad 40
personas[(personas["sexo_id"]) == 1 & (personas["edad"] < 40)]["producciones_ult_4_anios"].mean()
personas.describe() # me hace un analisis de todas las columnas numéricas: count, promedio, min, max, cuartiles
personas.info() # me dice qué tipo de datos son, si son str, float, int
"""  cómo convertir un float a str: """
personas["seniority_level"].astype("string")
personas.info()
""" filtrado, limpieza, ploteo 
vimos archivos:
pandas.md
Limpieza_de_datos_con_pandas.md """

