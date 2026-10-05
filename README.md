# 🌱 Grow Right

**Grow Right** is a simple Saudi planting advisor built with **Python** and **Streamlit**.

The project helps the user:
1. Check whether a selected plant is suitable for a selected Saudi city.
2. View a growing guide for the selected plant.
3. Find the top 3 plants for a selected city.

The Streamlit interface uses the existing `City` and `Plants` classes without changing the main project logic.

---

## Project Idea

Different plants prefer different temperatures, humidity levels, seasons, soil types, watering schedules, and sunlight conditions.

Grow Right compares the plant requirements with the selected city's climate data and gives the plant a suitability score.

---

## Features

### 1. Grow a Plant
The user selects a city and a plant. The application displays:
- Suitability Score
- Suitability Status
- Optimal Temperature
- Humidity
- Best Season
- Soil
- Watering
- Sun Exposure
- Growing Location

### 2. Best Plants for My City
The user selects a city, and the application displays the three plants with the highest suitability scores using the existing `top_3_plants()` function.

---

## Streamlit Pages

### `page1.py`
The first page lets the user choose between:
- **Grow a Plant**
- **Best Plants for My City**

It stores the user's selections using `st.session_state` and then opens the result page.

### `pages/2_result.py`
The second page reads the stored choices and displays the result.

It imports and uses:
```python
Dictionary_Cities
Dictionary_Plants
```

---

## Project Structure

```text
Grow_Right_Streamlit/
│
├── page1.py
├── City.py
├── Plants.py
├── Usercml.py
├── requirements.txt
│
└── pages/
    └── 2_result.py
```

---

## Main Files

### `City.py`
Contains the `City` class and the Saudi city database.

Main functions:
```python
score_calculator()
suitability()
top_3_plants()
```

### `Plants.py`
Contains the `Plants` class and the plant database.

Each plant stores:
- Temperature range
- Humidity
- Preferred season
- Soil
- Watering
- Sun exposure
- Location

### `Usercml.py`
The original command-line version of the project.

### `requirements.txt`
Contains the package needed to run the Streamlit interface.

---

## Cities Included

- Riyadh
- Makkah
- Madinah
- Jazan
- Al Qassim
- Al Baha
- Abha

---

## Plants Included

- Rosemary
- Tomato
- Lettuce
- Cucumber
- Mint
- Basil
- Thyme
- Parsley

---

## Suitability Score

The score uses temperature and humidity.

### Temperature
- **60 points** if the city temperature is inside the plant's preferred range.
- **30 points** if it is within a 5°C margin outside the preferred range.
- **0 points** otherwise.

### Humidity
Humidity is represented as:
```text
Low
Medium
High
```

The humidity score is:
- **40 points** when the plant and city humidity levels match.
- **20 points** when there is one level of difference.
- **0 points** when the difference is larger.

### Final Score
```text
Temperature Score + Humidity Score
```

Maximum score:
```text
100%
```

---

## Suitability Status

```text
80% or more  → Highly Suitable
60% or more  → Suitable
Below 60%    → Not Suitable
```

---

## Technologies Used

- Python
- Streamlit
- Object-Oriented Programming
- Dictionaries
- Lists
- Functions
- Classes and Objects

---

## Installation

Open Terminal inside the project folder.

Install the requirements:

```bash
python3 -m pip install -r requirements.txt
```

Or install Streamlit directly:

```bash
python3 -m pip install streamlit
```

---

## Run the Application

Run:

```bash
python3 -m streamlit run page1.py
```

Streamlit will show a local URL similar to:

```text
http://localhost:8501
```

Open it in your browser if it does not open automatically.

---

## How to Use

### Grow a Plant
1. Open the application.
2. Select **Grow a Plant**.
3. Select a city.
4. Select a plant.
5. Press **Continue**.
6. View the suitability score and growing guide.

### Best Plants for My City
1. Open the application.
2. Select **Best Plants for My City**.
3. Select a city.
4. Press **Continue**.
5. View the top 3 plants.

---

## Example

```text
Option: Grow a Plant
City: Riyadh
Plant: Tomato
```

The application gets the selected city object and calls:

```python
score = city.score_calculator(plant_name)
```

Then the result page displays the score and plant information.

---

## Design

The Streamlit interface is intentionally simple and suitable for a student project.

It uses:
- Light green background
- Dark green text
- Green buttons
- Simple input controls
- Two pages

---

## Notes

- Streamlit is used mainly for the user interface.
- The main calculations remain inside the existing project classes.
- Plant and city data are stored in dictionaries.
- The recommendations are based on the temperature and humidity data currently stored in the project.
- This is an educational planting advisor and is not a replacement for professional agricultural advice.

---

## Authors

Developed as a Python student project.

**Project Name:** Grow Right  
**Application:** Saudi Planting Advisor
