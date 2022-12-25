import pandas
import streamlit as st

st.set_page_config(layout='wide')

st.title('The Best Company')
st.write('Blablabla about our company..')

st.subheader('Our team')

col1, col2, col3 = st.columns(3)

data = pandas.read_csv('data.csv')

with col1:
    for index, row in data[0:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in data[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in data[8:12].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")