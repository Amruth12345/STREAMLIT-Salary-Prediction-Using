import streamlit as st
st.title("Registration Form")

first, last=st.columns(2)

first.text_input("First Name")
last.text_input("last Name")

email,mob=st.columns([3,1])

email.text_input("Email ID")
mob.text_input("MOBILE")

user,pw,pw2=st.columns(3)

user.text_input("username")
pw.text_input("password",type = "password")
pw2.text_input("retype your password",type = "password")

ch,bl,sub = st.columns(3)
ch.checkbox("i agree")
sub.button("submit")