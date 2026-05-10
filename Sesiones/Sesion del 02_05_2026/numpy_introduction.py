# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:30:23 2026

@author: eagel
"""

import numpy as np


arr_1 = np.array([1, 2, 3, 4, 5])

lista_normal = [1, 2, 3, 4, 5]

arr_2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


arr_1[2] = 99
arr_2[1][2] = 111

#arr_2.shape = (1,9)

arr_int8 = np.array(
    [11, 22, 33, 44, 55, 66, 77, 88, 99],
    dtype = "int8"
    )



cero_1 = np.zeros(3)
cero_2 = np.zeros((2,2))

unos_1 = np.ones((4,5))


identidad = np.identity(4)

eye_matrix = np.eye(3, 4)




a = np.array([
    [1,2,3],
    [4,5,6]
], dtype = np.int32)


unos_2 = np.ones_like(a)

pasos_1 = np.arange(11, 100, 11)
# lista = [i for i in range(11, 100, 11)]
# pasos_2 = np.arange(11, 100, 11).reshape(3, 3)
pasos_2 = pasos_1.reshape(3, 3)


lineal = np.linspace(0, 1, 5)


#
arr_3 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])



print("Propiedades de los arreglos", "\n")

print(f"Forma (shape): {arr_3.shape}")
print(f"Dimensiones (ndim): {arr_3.ndim}")
print(f"Tipo de Datps (dtype): {arr_3.dtype}")
print(f"Numero de elementos (size): {arr_3.size}")



### Operaciones matematicas ###
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])


print("Operaciones matematicas", "\n")
print(f"Suma: {arr1 + arr2}")
print(f"Multiplicacion: {arr1 * arr2}")
print(f"Potencia: {arr1**2}")
print(f"Seno: {np.sin(np.radians(arr2))}")



arr3 = np.arange(1, 10).reshape((3,3))
arr4 = np.arange(11, 100, 11).reshape((3,3))


print("Operaciones matematicas", "\n")
print(f"Suma: {arr3 + arr4}")
print(f"Multiplicacion: {arr3 * arr4}")
print(f"Potencia: {arr3**2}")
print(f"Coseno: {np.cos(np.radians(arr4))}")





# Indexacion y Slicing (Rebanado)

matriz = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(matriz[1,2])
print(matriz[0,:])
print(matriz[:,1], end="\n \n")
print(matriz[:2,:2], end="\n \n")


######## Manipulacion de dimensiones (Rshaping)

original = np.arange(12)
reestructurado = original.reshape((3,4)) 
transpuesta = reestructurado.T


### Estadistica y Agregacion


data = np.array([
    [1,2],
    [3,4],
])

print(np.sum(data))
print(np.mean(data))
print(np.std(data))
print("Suma por columnas:", np.sum(data, axis = 0))
print("Suma por filas:", np.sum(data, axis = 1))
print("Maximo: ", np.max(data), "y Minimo", np.min(data))



### Mascaras booleanas
numeros = np.array([1, 15, 8, 20, 3, 17, 10])
mayores_a10 = numeros[numeros > 10]
print(mayores_a10)

numeros.sort()
print(numeros)

a = np.array([11, 22, 33, 44])
b = np.array([55, 66, 77, 88])

print(np.concatenate((a,b)))

a1 = np.array(
    [
     [1,1],
     [2,2]
    ]
    )

a2 = np.array(
    [
     [3,3],
     [4,4]
    ]
    )


print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))


a = np.array([11, 11, 22, 33])

print(np.unique(a))