import streamlit as st
import pandas as pd
st.title("Hello")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)


options = df_cars['continent'].unique().tolist()
select = st.sidebar.multiselect('Which region do you want?',options)

st.write(df_cars, select)
