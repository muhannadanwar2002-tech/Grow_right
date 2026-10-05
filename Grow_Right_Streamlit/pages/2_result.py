import streamlit as st
from City import Dictionary_Cities
from Plants import Dictionary_Plants

# page settings
st.set_page_config(page_title="Result", page_icon="🌿")

# same simple design
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

st.title("🌿 Result")

# make sure the user came from the first page
if "choice" not in st.session_state:
    st.warning("Please go back and choose an option first.")

else:
    choice = st.session_state["choice"]
    city_name = st.session_state["city"]

    # get the city object from the existing dictionary
    city = Dictionary_Cities[city_name]

    # option 1: check one plant
    if choice == "Grow a Plant":
        plant_name = st.session_state["plant"]

        # use the existing class and dictionary
        plant = Dictionary_Plants[plant_name]
        score = city.score_calculator(plant_name)

        st.subheader(plant_name.title() + " in " + city.name)
        st.write("Suitability Score:", score, "%")
        st.write("Status:", city.suitability(plant_name))

        st.subheader("Growing Guide")

        # plant information comes from the existing Plants object
        st.write(plant.grow_right())

    # option 2: show the top 3 plants
    elif choice == "Best Plants for My City":
        st.subheader("Top 3 Plants in " + city.name)

        # use the existing function from City class
        top_plants = city.top_3_plants()

        for plant in top_plants:
            st.write(plant[0].title(), ":", plant[1], "%")

# return to first page
if st.button("Back"):
    st.switch_page("page1.py")
    
