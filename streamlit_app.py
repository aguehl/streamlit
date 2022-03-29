import streamlit as st
import pandas as pd

rad = st.radio('Title',('1','2'))
slide = st.slider('Taille du titre', 1, 3, 1)

if slide == 1:
  st.markdown("""
             <style>
             .big-font {
                font-size:100px !important;
             }
             </style>
             """, unsafe_allow_html=True)
elif slide == 2:
    st.markdown("""
             <style>
             .big-font {
                font-size:200px !important;
             }
             </style>
             """, unsafe_allow_html=True)
elif slide == 2:
    st.markdown("""
             <style>
             .big-font {
                font-size:300px !important;
             }
             </style>
             """, unsafe_allow_html=True)

                
if  rad == '1':
  st.markdown(''<p class="big-font">Hello Wilder 1 !!</p>', unsafe_allow_html=True )
if  rad == '2':
  st.markdown(''<p class="big-font">Hello Wilder 2 !!</p>', unsafe_allow_html=True )



link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

st.write(df_cars)


