import streamlit as st
import functions

st.title('My Todo App')

st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')

todos = functions.get_todos()

for item in todos:
    st.checkbox(item)
