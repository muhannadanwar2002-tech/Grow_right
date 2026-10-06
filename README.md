# Grow Right

Grow Right is a simple python project web application
its sole purpose is to check whether a plant is suitalble in a city's enviornment
while giving tips and guides to the user or filling the curiosity of the user on which are the top plants in the user defined city 


## Project Idea

Different plants prefer different temperatures, humidity levels, seasons, soil types, watering schedules, and sunlight conditions.
Grow Right compares the plant requirements with the selected city's climate data and gives the plant a suitability score.
although the comparisons aren't strict to mathematical fundamentals its closer to a agricultural wise.(which will be discussed below)

## Features

### 1. Grow a Plant
The user selects a city and a plant. And the application displays:
- Suitability Score
- Suitability Status
- Optimal Temperature
- Humidity
- Best Season
- Soil
- Watering
- Sun Exposure
- Growing Location
by calling a function in plant class called grow_right()

### 2. Best Plants for My City
The user selects a city, and the application displays the three plants with the highest suitability scores using the existing top_3_plants() function.

## Streamlit Pages

### page1.py
The first page lets the user choose between:
1-Grow a Plant

2-Best Plants for My City

It stores the user's selections using st.session_state and then opens the result page.

### pages/2_result.py
The second page reads the stored choices and displays the result.

It imports and uses:
1-Dictionary_Cities
2-Dictionary_Plants
and uses them for calling the functions stated below

## Main Files

### City.py
Contains the City class and the Saudi city database.

Main functions:
1-score_calculator()
2-suitability()
3-top_3_plants()


### Plants.py
Contains the Plants class and the plant database.
Main function:
1-grow_right():
    where Each plant returns:
      1-Temperature range
      2-Humidity
      3-Preferred season
      4-Soil
      5-Watering
      6-Sun exposure
      7-Location

### Usercml.py(naming should have been user_by_python) 
since it's the user interface interms of regular python outputs 

## Cities Included based on database collected:
- Riyadh
- Makkah
- Madinah
- Jazan
- Al Qassim
- Al Baha
- Abha
## Plants Included based on database collected:
- Rosemary
- Tomato
- Lettuce
- Cucumber
- Mint
- Basil
- Thyme
- Parsley

## Score Calculation

The score uses temperature and humidity.

### Temperature
- 60 points if the city temperature is inside the plant's preferred range.
- 30 points if it is within a 5°C margin outside the preferred range.
- 0 points otherwise.

### Humidity
Humidity is represented as:
1-Low = 1
2-Medium = 2
3-High = 3
which is then represented within the calculation by using numerical value
The humidity score is:
-40 points when the plant and city humidity levels match
-20 points when there is one level of difference.
- 0 points when the difference is larger.
and this is because that plants can thrive in somewhat extreme condition
that is why we stated in the beginning that the computation isnt strict when comparing since
the temperature and humidity are just preferable by the plant meaning it can thrive above or below its preferred range
which is what agriculture is all about.
### Final Score
Temperature Score + Humidity Score
Maximum score:
100%
## Suitability Status

80% or more  → Highly Suitable
60% or more  → Suitable
Below 60%    → Not Suitable

## Installation of streamlit

python3 -m pip install streamlit

## Run the Application via terminal

python3 -m streamlit run page1.py

### Grow a Plant
1. Open the application.
2. Select Grow a Plant.
3. Select a city.
4. Select a plant.
5. Press Continue.
6. View the suitability score and growing guide.

### Best Plants for My City
1. Open the application.
2. Select Best Plants for My City.
3. Select a city.
4. Press Continue.
5. View the top 3 plants.

## Design
streamlit uses:
- Light green background
- Dark green text
- Green buttons
- Simple input controls
- Two pages


## Notes

- we used css within Streamlit since most of us are more familiar with css and htmls (but we used it for background colors )
- Plant and city data are stored in dictionaries.
- The recommendations are based on the temperature and humidity data currently stored in the project.
- This is an educational planting advisor and is not a replacement for professional agricultural advice.
