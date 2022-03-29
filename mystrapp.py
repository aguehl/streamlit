import streamlit as st
import pandas as pd
st.title("Hello  Wilder")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)



options = df_cars['continent'].unique().tolist()
select = st.sidebar.multiselect('Which region do you want?',options, default= options)
filtered_df = df_cars[df_cars['continent'].isin(select)]
st.write(filtered_df)
