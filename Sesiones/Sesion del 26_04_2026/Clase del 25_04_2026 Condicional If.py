"""
a = 5
b = 7
c = 3

print(a, b, c)

print(f"Valor a = {a}, Valor b = {b},  Valor c = {c}")
print("Valor a = ", a, ", Valor b = ", b, ", Valor c = ", c)


if a > b:
    print("El mas grande entre a y b es: ", a)
elif c > b:
    print("El mas grande entre c y b es: ", c)
else:
    print("El mas de los tres es: ", b)
"""

"""
Estructuras de control if - elis - else
operadores para sentencias logicas: <, >, <=, >=, ==, !=, and, or, not
"""


a = 5
b = 7 
c = 3

def mayor_de_tres_numeros(a, b, c):
    verificacion = a - b

    if verificacion <= 0:
        guardar = b
    else:
        guardar = a

    verificacion2 = c - guardar

    if verificacion2 <= 0:
        mayor = guardar
    else:
        mayor = c

    return mayor


resultado = mayor_de_tres_numeros(a, b, c)


## Forma mas optima
def mayor_de_tres_numeros(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
        
    


    
    
    
    
    




