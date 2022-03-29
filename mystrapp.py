import streamlit as st
import pandas as pd
st.title("Hello  Wilder")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)

st.dataframe(df_cars)

options = df_cars['continent'].unique().tolist()
select = st.sidebar.multiselect('Which region do you want?',options)
filtered_df = df_cars[df_cars['continent'].isin(Select)]
st.write(filtered_df)
