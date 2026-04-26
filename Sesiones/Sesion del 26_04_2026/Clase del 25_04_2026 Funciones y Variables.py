def sumar_dos_numeros(a, b):
    c = a + b
    return c

resultado = sumar_dos_numeros(11, 22)




def funcion_prueba():
    return 1, 5, 4, 3, 2, "Hola", "Mundo"

print(funcion_prueba())
    
val1, val2, val3, val4, val5, val6, val7 = funcion_prueba()

print(val1, val2, val3, val4, val5, val6, val7 )













##### Profesor

a = 111
b = 222

def suma_dos_numeros():
    global a, b
    
    a = -11
    b = -22
    
    c = a + b
        
    return c

""" Aquí imprimimos valores originales de globales """
print(a, b)
print()

resultado = suma_dos_numeros()
print(resultado)
print()

""" Aquí imprimimos valores modificados de globales """
print(a, b)
print()


def funcion_prueba():
    return 1, 5, 4, 3, 2, "Hola", "Mundo"

print(funcion_prueba())

val1, val2, val3, val4, val5, val6, val7 = funcion_prueba()
print(val1, val2, val3, val4, val5, val6, val7)