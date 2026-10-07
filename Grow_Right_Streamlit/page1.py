import streamlit as st
from City import Dictionary_Cities
from Plants import Dictionary_Plants

                            # page title using the config
st.set_page_config(page_title="Grow Right")

                            # simple colors by using markdown (which is used to display string) to write and display the css/ html codde for the color background
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


st.title("Grow Right")        #displaying the Title
st.write("Saudi Planting Advisor")


choice = st.radio(            # creating a radio buttons of grow a plant or best plant  to allow user options 
    "Choose an option:",
    ["Grow a Plant", "Best Plants for My City"]
)

                                # creates a selectbox containing all avaialable cities imported from class city
city = st.selectbox(
    "Choose your city:",
    list(Dictionary_Cities.keys())
)

                                # show the select box of plants only when the radio button of grow  a plant
if choice == "Grow a Plant":    # which creates a list from the  dictionary of plants imported from class
    plant = st.selectbox(
        "Choose your plant:",    
        list(Dictionary_Plants.keys())
    )

                                # save choices and going to the result page
if st.button("Continue"):
    st.session_state["choice"] = choice
    st.session_state["city"] = city

    if choice == "Grow a Plant":
        st.session_state["plant"] = plant

    st.switch_page("pages/2_result.py")
