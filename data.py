import streamlit as st
import pandas as pd
import numpy as np

import time

a = np.arange(1,10).reshape(3,3)

dis = {
    "name":"amruth",
    "age" : "19",
    "city" : "karnataka"
}

st.dataframe(dis, width= 500,height=500)
st.table(dis)
st.json(dis)

@st.cache
def rest_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(rest_time())

if st.checkbox("2"):
    st.write(rest_time())