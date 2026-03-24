# Python-Dash-Principiantes

## Dashboard

<img width="944" height="380" alt="Lineas Barras" src="https://github.com/user-attachments/assets/f55fd402-f30d-4824-a875-dc9750256c82" />
<img width="916" height="320" alt="Pastel" src="https://github.com/user-attachments/assets/e995f6d1-16b3-4efd-a57c-84ca7d348e00" />


## **Objetivo**
* Construir un dashboard con python con la biblioteca de Dash.

## **Descripción**
* Este código lee un archivo xlxs, para que por medio de codigo de python cree un Dashboard. 

## **Qué voy a Aprender?** 
Al final del laboratorio seremos capaces de:
* Descargar las bibliotecas necesarias para crear un dashboard con python
* Crear un bloque de codigo con la bilioteca Dash
* Leer archivos mediante pandas 

## **Servicios de AWS a Utilizar**
* [VSC]    (https://code.visualstudio.com/)
* [Pandas] (https://pandas.pydata.org/)
* [DASH]   (https://dash.plotly.com/)

## **Explicación del Código**
A continuación voy a explicar detalladamente el código del archivo Python_Dash

## 1. Importación de librerías

```
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
```
* dash → la librería que permite crear dashboards.
* dcc (Dash Core Components) → se usa para componentes como gráficos.
* html → se usa para crear elementos visuales como títulos (H1, H3) o contenedores (Div).
* plotly.express → para generar gráficos interactivos (líneas, barras, pasteles, etc.).
* pandas → para manejar datos en forma de tablas (DataFrame).

## 2. Cargar datos desde Excel
```
df = pd.read_excel(r"tu ruta del archivo")
```
* Usamos pandas para leer el archivo Excel que contiene tus datos.
* La r delante de la ruta evita problemas con las barras invertidas (\).
* El archivo debe tener las columnas: Mes, Ventas, Costos, Categoria.

## 3. Crear gráficos con Plotly
```
fig_line = px.line(
    df,
    x="Mes",
    y=["Ventas", "Costos"],
    title="Comparación Ventas vs Costos"
)
```
* Gráfico de líneas que compara Ventas vs Costos mes a mes.
* Dos curvas aparecen en el mismo gráfico.

```
fig_bar = px.bar(df, x="Mes", y="Costos", title="Costos por Mes", color="Mes")
```
* Gráfico de barras que muestra los Costos por cada Mes.
* color="Mes" da un color diferente a cada barra.
```
fig_pie = px.pie(df, names="Categoria", title="Distribución por Categoría")
```
Gráfico de pastel que muestra cómo se distribuyen los datos según la columna Categoria.

## 4. Inicializar la aplicación
```
app = dash.Dash(__name__)
```
* app = dash.Dash(__name__)
* Aquí creamos la aplicación Dash.
* Es como decir: "voy a empezar un dashboard".

## 5. Definir el layout (estructura visual)
```
app.layout = html.Div(
    style={"backgroundColor": "#111111", "padding": "20px"},
    children=[
        html.H1(
            "Dashboard de Ejemplo con Excel",
            style={
                "textAlign": "center",
                "fontWeight": "bold",
                "textDecoration": "underline",
                "color": "white"
            }
        ),
```
* html.Div → contenedor principal del dashboard.
* Le ponemos fondo oscuro (#111111) y padding (espaciado interno).
* html.H1 → el título principal.
* Centrado, negrita, subrayado y blanco.

## 5.1 Subdivisiones con títulos + gráficos
```
html.Div([
    html.H3("📈 Ventas vs Costos (Líneas)",
            style={
                "textAlign": "center",
                "fontWeight": "bold",
                "textDecoration": "underline",
                "color": "white"
            }),
    dcc.Graph(figure=fig_line)
], style={"width": "48%", "display": "inline-block"}),
```
* Cada bloque html.Div contiene:
* Un subtítulo (html.H3).
* Un gráfico (dcc.Graph(figure=...)).
* El estilo "width": "48%", "display": "inline-block" permite que los gráficos se acomoden uno al lado del otro.
* Se repite igual para el gráfico de barras y el de pastel.


## 6. Ejecutar el servidor
```
if __name__ == "__main__":
    app.run(debug=True)
```
* Esto levanta un servidor local en tu computadora.
* Abres el navegador en http://127.0.0.1:8050/ y verás el dashboard.
* Con debug=True → si cambias el código y guardas, el servidor se actualiza solo.

### Resumen
* Importamos librerías necesarias.
* Leemos el archivo Excel con tus datos.
* Creamos gráficos interactivos con Plotly.
* Definimos el layout visual con Dash (Div, H1, H3, Graph).
* Personalizamos los estilos (fondo oscuro, títulos en blanco, centrados y subrayados).
* Ejecutamos el servidor para ver el dashboard en el navegador.




