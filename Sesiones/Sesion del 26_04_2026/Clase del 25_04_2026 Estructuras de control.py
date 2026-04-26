"""
Estructuras de Control
Ciclos / Loops: for y while
"""

### Manejo de listas

lista1 = [1, 2, 3, 4, 5]
print(lista1, lista1[2])
# print(lista1[5])   


lista2 = [33, 11, 22, "Hola a todos", 3.14159261, 4 + 3j]
print(lista2)

lista1.append(9)
print(lista1)

lista1.append(lista2)
print(lista1)

lista1.insert(3, "Item en index 3-1")
print(lista1)




### Estructuras de control

for i in range(10):
    print(i, end = ", ")
    

print("\n")
for i in range(3, 10):
    print(i, end = ", ")
    
print("\n")
for i in range(3, 10, 2):
    print(i, end = ", ")
    
print("\n\n\n")

lista3 = [1,"Hola",3.1415,"Mundo",5]
for i in lista3:
    print(i, end=", ")
    


j = 10
while j >= 3:
    print("Valor de j actual = ", j)
    j = j - 1
    
    
    
print("\n\n\n")
j = 10
while j >= 3:
    if j ==5:
        break
    
    if j == 8:
        j -= 1
        continue
    
    print("Valor de j actual = ", j)
    j = j - 1
    
    


print("\n\n\n")
for i in range(3):
    for j in range(5):
        print(j, end=" ")
        
    print()
    
 
    
## Ejercicio 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("\n\n\n")
for i in range(1, 6):
    for j in range(1, i +1):
        print(j, end=" ")
        
    print()
    
    
    

 ## Ejercicio 2
 
#     *
#    ***
#   *****
#  *******
# *********
print("\n\n\n")
for i in range(1, 7):
    for j in range(1, i +1):
        print("*", end=" ")
        
    print()

