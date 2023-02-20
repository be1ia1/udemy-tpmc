import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('happy.csv')

st.title('In search for Happiness')

x_select = st.selectbox(
    'Select the data for the X-axis',
    ('GDP', 'Happiness', 'Generosity')
)

y_select = st.selectbox(
    'Select the data for the Y-axis',
    ('GDP', 'Happiness', 'Generosity')
)

st.subheader(f'{x_select} and {y_select}')

# fake data
# x, y= [1, 4, 7], [2, 8, 14]
x, y = df[x_select.lower()], df[y_select.lower()]
figure = px.scatter(x = x, y = y)
st.plotly_chart(figure_or_data=figure)