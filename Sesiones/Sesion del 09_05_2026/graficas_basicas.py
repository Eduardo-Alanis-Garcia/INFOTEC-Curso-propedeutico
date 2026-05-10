import matplotlib.pyplot as plt
import numpy as np

### Grafica Curva Simple
plt.plot([1,2,3], [4,5,6])
plt.show()

### Grafica de barras simple
x = [1,2,3]
y = [4,5,6]
plt.bar(x, y)
plt.show()


### Grafico de dispersion
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y)


plt.xticks(np.arange(2, 19, 1))
plt.yticks(np.arange(min(y), max(y), 10))
plt.title("Dispersion")
plt.xlabel("Aqui son las Xs")
plt.ylabel("Aqui son las Ys")

plt.savefig("mi_grafico.png", dpi=300, bbox_inches="tight")
plt.show()



### Tambien se pueden otros valores en los ejes
frutas = ["Manzanas", "Mangos", "Fresas"]
ventas = [10, 15, 7]

plt.bar(frutas, ventas)
plt.show()


### Mas variaciones de graficas
x = np.array([_ for _ in range(30)])
y = np.array([np.random.randint(0,100) for _ in range(30)])

plt.plot(x,y)
plt.title("Prueba")
plt.xlabel("X: 0 a 100")
plt.ylabel("Y: lo que sea")
plt.show()



x = np.linspace(-1, 1, 100)
f1 = np.copy(x)

print(hex(id(x)), hex(id(f1)))


f2 = np.copy(x)**2
f3 = np.copy(x)**3



plt.figure(figsize = (5,3))
plt.subplot(131)
plt.plot(x, f1)
plt.title("Función no. 1")
plt.xlabel("X")
plt.ylabel("f1")

plt.subplot(132)
plt.plot(x, f2)
plt.title("Función no. 2")
plt.xlabel("X")
plt.ylabel("f2")

plt.subplot(133)
plt.plot(x, f3)
plt.title("Función no. 3")
plt.xlabel("X")
plt.ylabel("f3")

plt.show()




fig, ax = plt.subplots(figsize = (5,3))
ax.plot(x, f1, label = "lineal")
ax.plot(x, f2, label = "cuadratica")
ax.plot(x, f3, label = "cubica")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Prueba de plots")
ax.legend()






n_f = np.sin(np.linspace(0, 10, 100))
x = np.arange(len(n_f))
fig, ax = plt.subplots(figsize = (5,3))
ax.plot(x, n_f, color = "purple", linewidth = 1, linestyle = ":")
plt.show()


