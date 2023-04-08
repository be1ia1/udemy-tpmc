import streamlit as st
import plotly.express as px
import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM items")
data = cursor.fetchall()

dates = [i[0] for i in data]
temperatures = [i[1] for i in data]

figure = px.line(x = dates,
                 y = temperatures,
                 labels = {'x':"Date", 'y':"Temperature (C)"},
                 title='Student Project #10')
st.plotly_chart(figure)