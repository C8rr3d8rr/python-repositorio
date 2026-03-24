# Importacion de librerias necesarias para el analisis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargamos el archivo 
df = pd.read_csv(r"C:\Users\99dcorredorm\OneDrive - Sonova\Desktop\pruebasql.csv")

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

# Reemplazar todos los valores nulos por 0
df = df.fillna(0)

# Verificar el resultado
print("Valores nulos por columna después del reemplazo:")
print(df.isnull().sum())

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

X = df_anual["anio_num"].values.reshape(-1, 1)
y = df_anual["net_revenue_in"].values

model = LinearRegression()
model.fit(X, y)

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

plt.figure(figsize=(8,5))
plt.scatter(df_anual["anio"], df_anual["net_revenue_in"], color="blue", label="Datos reales")
plt.plot(df_total["anio"], df_total["net_revenue_predicho"], color="red", linestyle="--", label="Proyección lineal")
plt.title("Tendencia anual del Net Revenue (Regresión lineal)")
plt.xlabel("Año")
plt.ylabel("Net Revenue IN")
plt.legend()
plt.grid(True)
plt.show()
