# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:41:56 2026

@author: eagel
"""

class Queue:
    def __init__(self):
        self.lista = []
        
        
    def enqueue(self, data):
        self.lista.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            return self.lista.pop(0)
        return None
        
    def is_empty(self):
        respuesta_booleana = False
        
        if not self.lista:
            respuesta_booleana = True
            
        return respuesta_booleana
    
    
    def imprimir(self):
        string_out = ""
        
        for e in self.lista:
            string_out += str(e) + ", "
            
        print(string_out)
        
        
    def __str__(self):
        string_out = ""
        
        for e in self.lista:
            string_out += str(e) + ", "
            
        return string_out
        
        
cola = Queue()

print(cola.is_empty())

cola.enqueue(11)
cola.enqueue(22)
cola.enqueue(33)
cola.enqueue(44)
cola.enqueue(55)


print(cola.is_empty())


cola.imprimir()



while not cola.is_empty():
    print(cola.dequeue())
    cola.imprimir()