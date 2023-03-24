import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo_2022-12-20_19-56-58.jpg')

with col2:
    st.title('Andrii Hula')
    st.info('Всім привіт. Вікторії особливий :-)')

st.info('Це довге речення під обома блоками - під фото і під текстом')