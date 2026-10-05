import streamlit as st
st.title("Grow Right")
c1,c2=st.columns(2)
if c1.button("Click"):
    st.switch_page("1_infoapp.py")