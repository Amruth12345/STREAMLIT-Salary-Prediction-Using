import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

data = {
    'num':[x for x in range(1, 11)],
    "square":[x**2 for x in range (1, 11)],
    "twice":[x*2 for x in range(1, 11)],
    "thrice":[x*3 for x in range(1,11)]
}

a = pd.DataFrame(data)

st.write(a)

st.sidebar.selectbox("select",[1,2,3,4,5])