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

st.balloons()


# horse_power = df_cars['hp']
# temps = df_cars['time-to-60']

fig = px.scatter(df_cars, y='time-to-60', x='hp', trendline="ols",  color="time-to-60", color_continuous_scale="turbo",
                labels={
                  'time-to-60':'Temps de 0 à 60mph',
                  'hp':'Horse Power'},
                title='Correlation entre la puissance et le temps pour arriver à 60mph')


st.plotly_chart(fig, use_container_width=True)

