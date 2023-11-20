import pandas as pd
import plotly.express as px
import csv
import streamlit as st
import os

new_directory = 'D:/CURSOS/PRACTICUM/notebooks'
os.chdir(new_directory)
current_directory_after_change = os.getcwd()
print("Nuevo directorio actual:", current_directory_after_change)


def parse_custom_date(date_str):
    try:
        # Intenta analizar el formato "01/01/1900"
        return pd.to_datetime(date_str, format='%d/%m/%Y')
    except ValueError:
        try:
            # Intenta analizar el formato "1900"
            return pd.to_datetime(date_str, format='%Y')
        except:
            # Si no coincide con ninguno de los formatos, devuelve un valor nulo
            return pd.NaT

with open('Tailings Dam Failures 1915 - 2022 as of 31Jan23.csv', 'r', encoding='latin-1') as file:
    reader = csv.reader(file)
    header = next(reader)
    tailing_data = list(reader)

# Convierte la lista de listas a un DataFrame de Pandas utilizando los encabezados leídos
df = pd.DataFrame(tailing_data, columns=header)

# Convierte la columna "INCIDENT DATE" utilizando la función de análisis personalizada
df["INCIDENT YEAR"] = df["INCIDENT YEAR"].apply(parse_custom_date)

#Modifica el nombre de la columna
df = df.rename(columns={'ï»¿SEVERITY CODE': 'SEVERITY CODE'})

st.header('Data of Tailings Dam Failures 1915 - 2022 as of 31Jan23')

df = df.loc[:,~df.columns.duplicated()]
st.dataframe(df)

st.write('histogram for height of tailings dam failure from 1915 - 2022')
# crear un histograma
figdh = px.histogram(df, x="DAM HEIGHT (meters)")
        
# mostrar un gráfico Plotly interactivo
st.plotly_chart(figdh, use_container_width=True) 

build_histogram = st.checkbox('Make a histogram for tailings dam failure from 1915 - 2022')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Make a histogram for the tailings dam failure')
            
    # crear un histograma
    fig = px.histogram(df, x="INCIDENT YEAR")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 

hist_button2 = st.button('Built a scatter plot of severity of dam failures', key='hist_button2')
if hist_button2: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Make a scatter plot for the  severity of tailings dam failure')
            st.write('SEVERITY CODE')
            st.write('1 : Very Serious Tailings Dam Failures = multiple loss of life and/or release of ≥ 1,000,000 m3 total discharge, and/or release travel of 20 km or more')
            st.write('2 : Serious Tailings Dam Failures = loss of life and/or release of ≥ 100,000 m3 discharge')
            st.write('3 : Other Tailings Dam Failures = Engineering/facility failures other than those classified as Very Serious or Serious, no loss of life')
            st.write('4 : Waste-Related Accidents = Related facility tailings failures (e.g. sinkholes, pipelines), and non-tailings incidents (e.g. mine plug failures, waste rock failures, etc.)')
            
            # crear un histograma
            fig2 = px.scatter(df, x="INCIDENT YEAR", y="SEVERITY CODE")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig2, use_container_width=True) 
            
st.write('source: http://www.csp2.org/tsf-failures-from-1915')





            