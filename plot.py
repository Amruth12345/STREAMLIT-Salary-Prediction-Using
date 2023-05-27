import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

# st.image()
# st.audio("")
# st.video()


st.map()

chart = alt.Chart(data).mark_circle().encode(
    x = 'a',y = 'b'
)
st.altair_chart(chart,use_container_width=True)



st.graphviz_chart("""
digraph{ 
data->sub,
sub->do
data->do
}""")

plt.scatter(data['a'],data['b'])
plt.title('scatter')
st.pyplot()

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

