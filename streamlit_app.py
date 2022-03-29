import streamlit as st
import pandas as pd

rad = st.radio('Title',('1','2'))
slide = st.slider('Taille du titre', 20, 150, 1)
st.balloons()

st.markdown(f"""
           <style>
           .big-font {{
              font-size:{slide}px !important;
           }}
           </style>
           """, unsafe_allow_html=True)
                
if  rad == '1':
  st.markdown('<p class="big-font">Hello Wilder 1 !!</p>', unsafe_allow_html=True )
if  rad == '2':
  st.markdown('<p class="big-font">Hello Wilder 2 !!</p>', unsafe_allow_html=True )



link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.write(df_cars)

