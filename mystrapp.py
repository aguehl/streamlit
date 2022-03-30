import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory  as ff
st.title("Hello  Wilder")

link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df_cars = pd.read_csv(link)

st.write(df_cars)

options = df_cars['continent'].unique().tolist()
select = st.sidebar.multiselect('Which region do you want?',options, default= options)
filtered_df = df_cars[df_cars['continent'].isin(select)]
st.write(filtered_df)


poids = df_cars['weightlbs'].tolist()
temps = df_cars['time-to-60'].tolist()

graph_data = [poids, temps]
graph_labels = ['Wheight', 'Time to 60mph']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         graph_data, graph_labels, bin_size=[.1, .25, .5])



st.header("Time to 60mph by the wheight ")
st.plotly_chart(fig, use_container_width=True)


