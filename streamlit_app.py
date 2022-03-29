import streamlit as st
import pandas as pd

rad = st.radio('1','2')

if  rad == '1':
  st.title('Hello Wilders 1')
if  rad == '2':
  st.title('Hello Wilders 2')

slide = st.slider('Taille du titre', 0, 100, 50, 10)

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.write(df_cars)


