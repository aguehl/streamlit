import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels


st.title("Hello  Wilder")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)

st.write(df_cars)

options = df_cars['continent'].unique().tolist()
select = st.sidebar.multiselect('Which region do you want?',options, default= options)
filtered_df = df_cars[df_cars['continent'].isin(select)]
st.write(filtered_df)


horse_power = df_cars['hp']
temps = df_cars['time-to-60']

fig = px.scatter(df_cars, y='time-to-60', x='hp', trendline="ols")


st.plotly_chart(fig, use_container_width=True)

