# Python/Prueba

## Rgresion lineal

<img width="521" height="355" alt="Regresion_lineal" src="https://github.com/user-attachments/assets/76c4d705-3c87-4c98-b3ed-595096d52c38" />


## **Objetivo**
* Construir una regresion lineal con la libreria sklearn

## **Descripción**
* Este código lee un archivo CSV, para que por medio de codigo de python cree un Dashboard. 

## **Qué voy a Aprender?** 
Al final de la prueba seremos capaces de:
* Descargar las bibliotecas necesarias para crear una regresion con python
* Crear un bloque de codigo con la bilioteca sklearn
* Leer archivos mediante pandas, Numpy, matplotlib

## **Servicios de AWS a Utilizar**
* [VSC]    (https://code.visualstudio.com/)
* [Pandas] (https://pandas.pydata.org/)
* [Numpy]  (https://numpy.org/)

## **Explicación del Código**
A continuación voy a explicar detalladamente el código del archivo Python


## 1. Importación de librerías
```
# Importacion de librerias necesarias para el analisis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
```

* Pandas → Manipulacion de datos
* Numpy → Creacion de vectores y matrices
* Marplotlib → Visualizacion de datos 
* Sklearn → Aprendizaje automatico

## 2. Cargar los datos desde Excel
```
df = pd.read_csv(r"C:\Users\99dcorredorm\OneDrive - Sonova\Desktop\pruebasql.csv")
```
* Lee el archivo Excel y lo guarda en un DataFrame (df).


## 3. Resumen de datos 
```
# Información general (tipos de datos y valores nulos)
print("Información general:")
df.info()
print("\n","\n")

# Conteo de valores nulos por columna
print("Valores nulos por columna:")
print(df.isnull().sum(), "\n", "\n")

# Porcentaje de valores nulos por columna
print("Porcentaje de valores nulos por columna:")
print((df.isnull().mean() * 100).round(2), "\n","\n")

# Estadísticas básicas de las variables numéricas
print("Estadísticas descriptivas:")
print(df.describe().T)
```
* Resumen de datos para ver datos nulos
* Estadisticas basicas de los datos

## 4. Remplazar datos nulos por cero
```
# Reemplazar todos los valores nulos por 0
df = df.fillna(0)
```
* Se remplazan los valores nulos, faltantes por un valor especifico, en esta caso por el numero cero

## 5. Creacion del modelo de regresion lineal 

## Paso #1
```
# Normalizar nombre de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("#", "")

# Convertir a fecha
df["periodo"] = pd.to_datetime(df["periodo"], errors="coerce")

# Convertir revenue a numérico
df["net_revenue_in"] = pd.to_numeric(df["net_revenue_in"], errors="coerce")

# Eliminar nulos
df = df.dropna(subset=["periodo", "net_revenue_in"])

# Crear columna de año
df["anio"] = df["periodo"].dt.year

# Agrupar por año y sumar net revenue
df_anual = df.groupby("anio", as_index=False)["net_revenue_in"].sum()

# Crear variable numérica para el modelo (X)
df_anual["anio_num"] = df_anual["anio"]
```
* Se manipulan las columnas de los datos para que se pueda crear un modelo de evaluacion, para asi poder crear la regresion lineal


## Paso #2
```
#Configuracion de los campos de la regresion lineal
X = df_anual["anio_num"].values.reshape(-1, 1)
y = df_anual["net_revenue_in"].values

model = LinearRegression()
model.fit(X, y)
```

* Se dan valores a los ejes X & Y

## Paso #3
```
anios_futuros = np.arange(df_anual["anio"].max() + 1, 2028).reshape(-1, 1)
predicciones = model.predict(anios_futuros)

# Crear dataframe con predicciones
df_pred = pd.DataFrame({
    "anio": anios_futuros.flatten(),
    "net_revenue_predicho": predicciones
})

df_total = pd.concat([
    df_anual.rename(columns={"net_revenue_in": "net_revenue_real"}),
    df_pred
], ignore_index=True)
```

* Se crea el pronostico para tener la informacion de 2 años hacia adelante


## Paso #4
```
plt.figure(figsize=(8,5))
plt.scatter(df_anual["anio"], df_anual["net_revenue_in"], color="blue", label="Datos reales")
plt.plot(df_total["anio"], df_total["net_revenue_predicho"], color="red", linestyle="--", label="Proyección lineal")
plt.title("Tendencia anual del Net Revenue (Regresión lineal)")
plt.xlabel("Año")
plt.ylabel("Net Revenue IN")
plt.legend()
plt.grid(True)
plt.show()
```
* Creacion del grafico para ver las predicciones de manera grafica



