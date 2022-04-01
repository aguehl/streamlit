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
select = st.multiselect('Which region do you want?',options, default= options)
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

optionY = df_cars.columns
optionX = df_cars.columns


Ycol = st.selectbox('Choisir des données à visualiser:', optionY)
Xcol = st.selectbox('', optionX)

XArray= np.array(df_cars[Xcol])
YArray= np.array(df_cars[Ycol])


Cor=round(np.corrcoef(XArray,YArray)[0,1], 2)
 
fig = px.scatter(df_cars, y=Ycol, x=Xcol, trendline="ols",  color=Ycol, color_continuous_scale="turbo",
                labels={
                  Ycol:Ycol,
                  Xcol:Xcol},
                title=f'Correlation entre {Xcol} et {Ycol}')

fig.update_layout(title_font_size=26)

st.plotly_chart(fig, use_container_width=True)
st.subheader(f'Coef de correlation {Cor}')
