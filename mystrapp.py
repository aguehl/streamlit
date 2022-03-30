import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels
import seaborn as sns


st.title("Hello  Wilder")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)


options = df_cars['continent'].unique().tolist()
select = st.sidebar.multiselect('Which region do you want?',options, default= options)
filtered_df = df_cars[df_cars['continent'].isin(select)]
st.write(filtered_df)

viz_correlation = sns.heatmap(df_cars.corr(), 
			center=0,
			annot= True,
			cmap = sns.color_palette("vlag", as_cmap=True)
			)
st.title('Correlation entre les éléments')
st.pyplot(viz_correlation.figure)

st.balloons()
 

horse_power = df_cars['hp']
temps = df_cars['time-to-60']

Cor= np.corcoef(horse_power,temps)

	 
fig = px.scatter(df_cars, y='time-to-60', x='hp', trendline="ols",  color="time-to-60", color_continuous_scale="turbo",
                labels={
                  'time-to-60':'Temps de 0 à 60mph',
                  'hp':'Horse Power'},
                title='Correlation entre la puissance et le temps pour arriver à 60mph')


st.plotly_chart(fig, use_container_width=True)
st.subheader('Coef de correlation', Cor)


