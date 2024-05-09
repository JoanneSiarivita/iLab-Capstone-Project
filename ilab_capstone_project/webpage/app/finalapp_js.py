# IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import base64

# Function to display content based on page state
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/png;base64,{bin_str}");
    background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

#def get_base64(bin_file):
#    with open(bin_file, 'rb') as f:
#        data = f.read()
#    return base64.b64encode(data).decode()


# Set Streamlit page config
st.set_page_config(page_title="Eat Well Live Well", page_icon=":green_salad:")

# Define click_button function to handle button click events
def click_button():
    st.session_state.clicked = True

# Initialise session state
if 'key' not in st.session_state:
    st.session_state.key = 'value'

# DEFINE PAGE 1 DISPLAY
def display_page_1():
    st.image('Header.png')
    st.markdown('<p class="big-font">This application will be used to assess if you have any dietary risk factors for diabetes. You will answer a series of questions regarding the types and amount of food you eat to provide a dietary risk assessment for type 2 diabetes.</p>', unsafe_allow_html=True)
    st.write("Getting treated for diabetes early can prevent the following life-altering diseases:")
    st.image('complications.png')
    st.write(":warning: The information provided by this application is not intended to be a substitute for professional medical advice, diagnosis, or treatment.")
    name_key = "name_input"  # Unique key for name input
    name = st.text_input("Please enter your name and select gender to begin:", key=name_key)
    st.session_state["name"] = name
    gender = st.radio('Gender Preference', ['Male', 'Female', 'Non-Binary'])
    st.write("Please enter your height and weight. This helps us to see if you have a higher risk for diabetes")
    height_key = "height_input"
    height = st.text_input("Height (in cm):",key=height_key)
    st.session_state["height"] = height
    weight_key = "weight_input"
    weight = st.text_input("Weight (in kg):",key=weight_key)
    st.session_state["weight"] = weight
    submit_page1 = st.button("Submit", on_click=click_button)
    if submit_page1:
        st.session_state["page"] = 2  # Move to page 2 after submission

# DEFINE PAGE 2 DISPLAY
def display_page_2():
    st.image('Header.png')
    st.write(f"Hi {st.session_state['name']}!")
    st.write("The early signs and symptoms of Type 2 Diabetes can include:")
    signs = ["Frequent urination :toilet:", "Increased thirst :potable_water:", "Fatigue :sleeping:", "Blurred vision :eyeglasses:", "Slow healing of cuts and wounds :adhesive_bandage:", "Tingling numbness or pain in hands or feet :wave:", "Patches of darker skin :black_medium_square:", "Itching and yeast infections :mushroom:"]
    st.markdown("\n".join([f"- {sign}" for sign in signs]))
    st.write(":large_red_square: If you have recently started experiencing these symptoms, it is recommended that you seek medical advice as soon as possible.")
    st.link_button("To find a GP (General Practitioner) please click here", "https://www.healthdirect.gov.au/australian-health-services")
    if st.button("NEXT"):
        st.session_state["page"] = 3

# DEFINE PAGE 3 DISPLAY
def display_page_3():
    st.image('Header.png')
    name = st.session_state["name"]
    st.write(f"{name}, what do you eat each day?")
    st.link_button("For more information on serving sizes please click here", "https://www.eatforhealth.gov.au/food-essentials/five-food-groups/grain-cereal-foods-mostly-wholegrain-and-or-high-cereal-fibre")

    # Define food options and their corresponding serving sizes
    food_options = {
        "Fruit": {"image": "fruitserve.png", "serving_size": 150},
        "Starchy Vegetables": {"image": "starchyvegserve.png", "serving_size": 180},
        "Dairy": {"image": "dairyserve.png", "serving_size": 250},
        "Refined Grains": {"image": "refgrainserve.png", "serving_size": 50},
        "Whole Grains": {"image": "whgrainserve.png", "serving_size": 50},
        "Processed Meats": {"image": "prmeatserve.png", "serving_size": 50},
        "Eggs": {"image": "eggserve.png", "serving_size": 55},
        "Unprocessed Meat": {"image": "unprmeatserve.png", "serving_size": 100},
        "Sweetened Beverage": {"image": "swdrinkserve.png", "serving_size": 248},
        "Fruit Juice": {"image": "fjuiceserve.png", "serving_size": 248}
    }

    # Create an empty list to store data for each food type
    food_data_list = []

    # Iterate through food options to collect user input
    for food_type, info in food_options.items():
        st.image(info["image"], caption=f"Serving Size {food_type}")
        serves = st.select_slider(f"How many serves of {food_type} per day?", options=["0","1","2","3","4","5 or more"], help="help")
        num_serves = float(serves.split()[0])
        total_serves_per_day = num_serves * info["serving_size"]

        # Append data tuple to the list
        food_data_list.append((food_type, info["serving_size"], total_serves_per_day))

    # Create a DataFrame from the collected data
    food_data = pd.DataFrame(food_data_list, columns=['Food Type', 'Serving Size (g)', 'Serves per Day'])

# Add a button to calculate and submit selection
    if st.button("Submit"):
        # Calculate total servings per day across all food types
        total_serves_per_day = sum(food_data['Serves per Day'])

        #Calculate BMI
        height_cm = float(st.session_state["height"])
        weight_kg = float(st.session_state["weight"])
        height_m = height_cm/100
        bmi = weight_kg/(height_m **2)

        # DEFINE FUNCTIONS FOR PREDICTION AND CALCULATIONS
        def predict_diabetes_risk(risk_factor, model):
            data = np.array([[risk_factor]])
            prediction = model.predict(data)[0]
            return prediction
        
        # Use a trained model to predict diabetes risk
        risk_prediction = predict_diabetes_risk(bmi, svm_model)
        
        st.session_state["result"] = risk_prediction
        st.success("Selections submitted successfully")
        st.session_state["page"] = 4  # Move to results page

# DEFINE PAGE 4 DISPLAY
def display_page_4():
    st.image('Header.png')
    st.write("Your predicted risk of developing Type 2 Diabetes:")
    st.write(st.session_state["results"])
    if st.button("Restart"):
        st.session_state["page"] = 1  # Restart to page 1

# Function to load SVM model from pickle file
def load_svm_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Path to the SVM model file
model_path = 'svm_model.pkl'

# Load the SVM model
svm_model = load_svm_model(model_path)

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = 1

# RUN APP
# Main Streamlit app
if st.session_state["page"] == 1:
    display_page_1()
elif st.session_state["page"] == 2:
    display_page_2()
elif st.session_state["page"] == 3:
    display_page_3()
elif st.session_state["page"] == 4:
    display_page_4()


