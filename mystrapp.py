import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Hello  Wilder")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)

st.write(df_cars)

options = df_cars['continent'].unique().tolist()
select = st.sidebar.multiselect('Which region do you want?',options, default= options)
filtered_df = df_cars[df_cars['continent'].isin(select)]
st.write(filtered_df)


poids = df_cars['wheightlbs']
temps = df_cars['time-to-60']


st.write(poids)
st.write(temps)

#The plot
fig = go.Figure(
    go.Pie(
    labels = poids,
    values = temps,
    hoverinfo = "label+percent",
    textinfo = "value"
))

st.header("Time to 60mph by the wheight ")
st.plotly_chart(fig)
