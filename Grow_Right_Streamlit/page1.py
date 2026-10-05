import streamlit as st
from City import Dictionary_Cities
from Plants import Dictionary_Plants

# page settings
st.set_page_config(page_title="Grow Right", page_icon="🌱")

# simple colors
st.markdown("""
<style>
.stApp {
    background-color: #F4F8F2;
}
h1, h2, h3, p, label {
    color: #234D36 !important;
}
.stButton > button {
    background-color: #3E7B52;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# title
st.title("🌱 Grow Right")
st.write("Saudi Planting Advisor")

# choose what the user wants
choice = st.radio(
    "Choose an option:",
    ["Grow a Plant", "Best Plants for My City"]
)

# choose city from the City dictionary
city = st.selectbox(
    "Choose your city:",
    list(Dictionary_Cities.keys())
)

# plant is only needed in the first option
if choice == "Grow a Plant":
    plant = st.selectbox(
        "Choose your plant:",
        list(Dictionary_Plants.keys())
    )

# save choices and go to result page
if st.button("Continue"):
    st.session_state["choice"] = choice
    st.session_state["city"] = city

    if choice == "Grow a Plant":
        st.session_state["plant"] = plant

    st.switch_page("pages/2_result.py")
