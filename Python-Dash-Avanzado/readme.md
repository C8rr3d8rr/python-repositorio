# Python-Dash-Principiantes

## Dashboard

<img width="1023" height="415" alt="Dash_board_avanzado_3" src="https://github.com/user-attachments/assets/be9a7171-a955-4687-b2d8-df16cd9fc5b0" />
<img width="1006" height="365" alt="Dash_board_avanzado_2" src="https://github.com/user-attachments/assets/de986259-3766-45d5-93e9-6d6fab9f6230" />
<img width="1025" height="371" alt="Dash_board_avanzado_1" src="https://github.com/user-attachments/assets/8fd8091b-c60c-412f-b1a8-4b92fd85d364" />



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

## 1. Importacion de librerias
```
import dash from dash
import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
```

## 2. Carga de datos 
```
df = pd.read_excel(r"C:\...\Prueba_dash.xlsx")
```
* Importas un Excel con columnas como Ventas, Costos, Mes, Categoria.
* Este df es la fuente de todos los cálculos y gráficos.

## 3. Inicialización de la App
```
app = dash.Dash(__name__)
app.title = "Dashboard Avanzado"
```
* Creas la app de Dash y le das un título que aparece en el navegador.

## 4. Layout principal con Tabs
```
dcc.Tabs(
    id="tabs",
    value="tab_kpi",
    children=[ ... ])
```
* Tienes tres pestañas: KPIs, Gráficos y Distribución.
* Cada una carga contenido distinto en contenido_tabs vía callback.

## 5. Callback principal de Tabs
```
@app.callback(
    [Output("grafico_lineas", "figure"),
     Output("grafico_barras", "figure")],
    Input("filtro_categoria", "value"),
    prevent_initial_call=True)
```

```
df_filtrado = df[df["Categoria"] == categoria]
```
* Este callback actualiza dos gráficos según la categoría elegida en el dropdown.
* prevent_initial_call=True evita que se ejecute antes de elegir algo.

```
df_filtrado = df[df["Categoria"] == categoria]
```
* Filtra los datos por la categoría seleccionada.

```
fig_line = px.line(df_filtrado, x="Mes", y=["Ventas", "Costos"], ...)
fig_bar = px.bar(df_filtrado, x="Mes", y="Ventas", ...)
```
* Gráfico de línea → compara Ventas vs Costos por mes.
* Gráfico de barras → muestra Ventas por mes.
* Dependiendo de la pestaña seleccionada (tab_kpi, tab_graficos, tab_pie), devuelve un layout distinto:
   * KPIs: sumas de Ventas, Costos y cálculo de Utilidad.
   * Gráficos: dropdown para filtrar por categoría + dos gráficos dinámicos.  
   * Distribución: un gráfico de torta de participación por categoría.

## 6. Ejecución del servidor
```
app.run(debug=True, port=8052)
```
* Levantas el servidor en el puerto 8052 (así evitas conflicto con otros Dash en 8050 o 8051).





