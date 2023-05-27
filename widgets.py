import streamlit as st

st.title("WIDGET")

if st.button("subscribe and save"):
    st.write('amruth')

name = st.text_input('Name')

st.write(name)

adress = st.text_area('enter the adress')

st.write(adress)

st.date_input("enter the date")

st.time_input("enter the time")

st.checkbox("pick one")

st.radio("colors", ['r','g','b'],index = 0 )

st.selectbox("colors", ['r','g','b'],index = 0 )

st.multiselect("colors", ['r','g','b'])

st.slider("age",min_value=18,max_value=60,value=20,step=2)

st.number_input("enter the number",min_value=1.0,max_value=100.0,value=20.0,step=2.0)

a= st.file_uploader('drop your file here')

st.write(a)