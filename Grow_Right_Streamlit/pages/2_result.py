import streamlit as st
from City import Dictionary_Cities
from Plants import Dictionary_Plants

# page title using the config
st.set_page_config(page_title="Result")

# using css in markdown (is a function used for displaying text ) functions to change the background colors
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

st.title("Result")


if "choice" not in st.session_state:        # to make sure the user came from the first page we used an which is based on the session_state choice we saved in the first page 
    st.warning("Please go back and choose an option first.")

else:
    choice = st.session_state["choice"]
    city_name = st.session_state["city"]

    city = Dictionary_Cities[city_name]         # get the city from the existing city dictionary


    if choice == "Grow a Plant":                # the first option is it checks if the choice is plant
        
        plant_name = st.session_state["plant"] #takes the name that was saved in session state

        plant = Dictionary_Plants[plant_name]  #using the plant dictionary we can derive and assign the plant to plant
        
        score = city.score_calculator(plant_name) #returns the score of the plant in that city
        
        status=city.suitability(plant_name) #returns the suitability of the plant in that city
      
        st.subheader(plant_name.title() + " in " + city.name) #displays the plant in city
        
        st.write(status)                                      #displays the suitability

        st.subheader("Growing Guide") 
        
        st.markdown(plant.grow_right().replace("\n","  \n"))# plant information comes from the existing Plants object

    
    elif choice == "Best Plants for My City":               # option 2: show the top 3 plants
        st.subheader("Top 3 Plants in " + city.name)

        top_plants = city.top_3_plants()                    # use the existing function from City class

        for plant in top_plants:
            st.write(plant[0].title(), ":", plant[1], "%")

# return to first page
if st.button("Back"):
    st.switch_page("page1.py")
    
