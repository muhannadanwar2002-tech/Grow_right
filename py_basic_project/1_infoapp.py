import streamlit as st
from City import Dictionary_Cities
from Plants import Dictionary_Plants
st.title("Grow Right")
c1,c2=st.columns(2)
if c1.button("Click"):
    
    plant = st.text_input("Enter plant: ").lower()
    city = st.text_input("Enter city: ").lower()
    st.write("Plant you choose is :" , plant )
    st.write("city you choose is :" , city )
    try:
        Dictionary_Cities[city].suitability(plant)
        st.write()
        st.write("Growing Guide:")
        Dictionary_Plants[plant].GROW_RIGHT()
    except(Exception):
        print("Not in DataBase or Syntax error")  
    
if c2.button("Click2"):
    pass

