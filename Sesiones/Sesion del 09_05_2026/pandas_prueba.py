import pandas as pd
import numpy as np

edades = pd.Series([25, 30, 35, 40], name='Edad')
nombres = pd.Series(["Fulanito", "Juanito", "Ajalas", "Mike"], name='Nombre')

tabla = pd.concat([nombres, edades], axis=1)

data = {
        'Motor': ['AC_Standar', 'Servo', 'Stepper', 'DC_Brushless'],
        'Voltaje': [220, 24, 12, 5],
        'Corriente': [5.5, 2.1, 1.8, 0.8],
        'Eficiente': [True, True, False, True]
        }

df = pd.DataFrame(data)

""" Manejo de Archivos """
df = pd.read_csv('Inputs/automobile_parts.csv')



### Inpeccion de datos

print(df.head(5), end = "\n\n")   # Encabezado
print(df.tail(3), end = "\n\n")   # Cola o imprimimos lo de hasta abajo

print(df.info(), end = "\n\n")
print(df.describe(), end = "\n\n")      # Funcion muy interesabte para saver rapido la media y desviacion estandar

description = df.describe()




### Seleccion y Filtrado (Indexing & Slicing)

# Imprimir columnas
keys = df.keys()
print(keys)
print(df.columns)
print(list(df.columns))


for i, j in zip(df.columns, list(df.columns)):
    print(i, "-", j, end = ", ")



print(df["TYPE"])
print(df["TYPE"][4], df.loc[4, "TYPE"])  #Ambas cosas hacen lo mismo, pero la segunda forma me suena a matriz mas natural

print(df.loc[4]) # Nos da la fila con indice 4

print(df.iloc[0:2, 0:3]) # Muestra una ventana de rangos

articulos_caros = df[df["PRICE"] > 400]
print(articulos_caros)

solo_audi = df[(df["MANUFACTURER"] == "Audi") & (df["PRICE"] > 450)]
print(solo_audi)



### Manipulacion y Limpieza 



df["Qty"] = 0
for i in range(len(df)):
    df.loc[i, "Qty"] = np.random.randint(1, 10)
    
df["Qty_2"] = [np.random.randint(10, 15) for _ in range(len(df))]

# df["Model"] = "A"
# import random 
# df_tempo = df[df["MANUFACTURER"] == "BMW"]

# for i in range(len(df_tempo)):
#     df_tempo.loc[i, "Model"] = random.choice(["A", "B", "C"])



df = df[["PART ID", "TYPE", "MANUFACTURER", "YEAR", "Qty", "PRICE"]]
# df.insert(4, "Qty", df.pop("Qty"))       # Estudiar mas
df["SUBTOTAL INVENTORY"] = df["Qty"]*df["PRICE"]

df = df.rename(columns = {"PRICE": "PRECIO"})

df["ACTIVE"] = [np.random.choice([True, False, np.nan]) for _ in range(len(df))]

df.loc[len(df)] = ["PARTXXXX", "Amortiguador", "Nissan", 2026, np.nan, 100.11, np.nan, 1] # Añade hasta el final
print(df.iloc[[-1]])

df = df.iloc[:-1] # Eliminar el ultimo



# Exportación de los resultados

df.to_csv("Inventario_modificado.csv", index = False)
