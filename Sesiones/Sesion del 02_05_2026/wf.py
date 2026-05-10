# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:58:20 2026

@author: eagel
"""

import my_queue

nueva_cola = my_queue.Queue()

nueva_cola.enqueue(99)
nueva_cola.enqueue("Hola chicos")
nueva_cola.enqueue(77)

print(nueva_cola)

