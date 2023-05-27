import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np




st.title('Salary Predictor')

data = pd.read_csv("Salary_Data.csv")


x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))

nav=st.sidebar.radio("navigation",["Home","Prediction","Contribute"])
if nav == "Home":
    st.image("img.png",width=500)
    if st.checkbox("show Table"):
        st.table(data)

    graph = st.selectbox("graph",["interactive graph","non interactive"])

    val = st.slider("filter data using years",0,20)
    data= data.loc[data["YearsExperience"]>=val]

    if graph=="non interactive":
        plt.figure(figsize=(10,15))
        plt.scatter(x=data["YearsExperience"],y= data["Salary"])
        plt.ylim(0)
        plt.xlabel("years of experience")
        plt.ylabel('Salary')
        plt.tight_layout()
        st.pyplot()

    if graph == "interactive graph":
        layout = go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range=[0,210000])
        )
        fig = go.Figure(data=go.Scatter(x=data['YearsExperience'],y=data["Salary"],mode="markers"),layout=layout)
        st.plotly_chart(fig)


if nav == "Prediction":
    st.header("know your Salary")
    val = st.number_input("Enter your exp",0.00,20.00,step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"your predicted salary is {round(pred)}")

if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("enter your Experience",0.0,20.0)
    sal = st.number_input("Enter your Salary",0.0,10000000.0,step = 1000.0)
    if st.button("Submit"):
        to_add = [{"YearsExperience":ex,"Salary":sal}]
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Salary_Data.csv",mode ='a',header = False,index=False)
        st.success("Submitted")


