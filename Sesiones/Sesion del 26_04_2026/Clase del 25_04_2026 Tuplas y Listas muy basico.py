# Mutable
lista = [1, 2, "Hola", 3.1415, 5]


# No mutable
tupla = (1, 2, "Hola", 3.1415, 5)


print(lista[1], tupla[1])


## Vemos el error que no podemos modificar la tupla
lista[1] = 99
#tupla[1] = 88

print(lista[1], tupla[1])





# Vamos a ver un ejemplo con trampa

lista = [1, 2, "Hola", 3.1415, 5]
tupla = (1, 2, "Hola", 3.1415, 5, lista)
print(lista, tupla)

lista[1] = 99
print(lista, tupla)
