from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

import pandas as pd
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)


presicion = accuracy_score(y_test, predicciones)

print(f"La presición del modelo es: {presicion * 100:.2f}")



"""
Ejemplo: [cm] -> R: "Setosa"
Largo del Sepalo = 5.1
Ancho del Sepalo = 3.5
Largo del Petalo = 1.4
Ancho del Petalo = 0.2
"""

nueva_flor = pd.Series({
    "sepal length (cm)": 5.1,
    "sepal width (cm)": 3.5,
    "petal length (cm)": 1.4,
    "petal width (cm)": 0.2
    })

nueva_flor_array = nueva_flor.values.reshape(1, -1)
prediccion = modelo.predict(nueva_flor_array)

especie = iris.target_names[prediccion[0]]
print(f"La flor ingresada pertenece a {especie}")