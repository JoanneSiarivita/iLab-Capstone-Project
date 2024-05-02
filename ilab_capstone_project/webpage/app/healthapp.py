import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Function to display content based on page state
def display_page(page_num):
    if page_num == 1:
        st.title("Eat Well Live Well - Welcome")
        name = st.text_input("Please enter your name and select gender to begin")
        gender = st.radio('Gender Preference', ['Male', 'Female', 'Other'])
        submit_page1 = st.button("Submit", key="first_page")

        if submit_page1:
            st.session_state["name"] = name
            st.session_state["page"] = 2  # Move to page 2 after submission

    elif page_num == 2:
        st.title("Eat Well Live Well")
        st.write(f"Hi {st.session_state['name']}!")
        st.write("The early signs and symptoms of Type 2 Diabetes can include:")

        signs = [
            "Frequent urination",
            "Increased thirst",
            "Fatigue",
            "Blurred vision",
            "Slow healing of cuts and wounds",
            "Tingling numbness or pain in hands or feet",
            "Patches of darker skin",
            "Itching and yeast infections"
        ]

        st.markdown("\n".join([f"- {sign}" for sign in signs]))

        st.write("If you have recently started experiencing these symptoms, it is recommended that you seek medical advice as soon as possible.")

        if st.button("NEXT"):
            st.session_state["page"] = 3

    elif page_num == 3:
        st.title("Eat Well Live Well")
        name = st.session_state["name"]
        st.write(f"{name}, what do you eat each day?")

        # Define the list of food options
        food_options = [
            "Eggs", "Fruit", "Non-starchy vegetable", "Starchy vegetable", "Refined grains",
            "Whole grains", "Processed meats", "Unprocessed meats", "Sweetened beverages",
            "Fruit juice", "Saturated fats", "Unsaturated fats", "Added sugars", "Added salts", "Dairy"
        ]

        # Display checkboxes for food options
        selected_options = st.multiselect("Select options:", food_options, default=[])

        if len(selected_options) < 3:
            st.warning("Please select up to 3 options.")

        # Dictionary to store serves per day for each selected option
        serves_per_day = {}

        # For each selected option, prompt user to input serves per day
        for option in selected_options:
            serves = st.select_slider(f"How many serves of {option} per day?", options=["0-1", "2-3", "4 or more"])
            serves_per_day[option] = serves

        # Add a button to submit selection
        if st.button("Submit", key="submit_button"):
            # Calculate risk factor based on servings per day
            result = calculate_risk_factor(serves_per_day)
            
            # Use a trained model to predict diabetes risk
            risk_prediction = predict_diabetes_risk(result)
            
            st.session_state["results"] = risk_prediction
            st.success("Selections submitted successfully")
            st.session_state["page"] = 4  # Move to results page

    elif page_num == 4:
        st.title("Eat Well Live Well")
        st.write("Your predicted risk of developing Type 2 Diabetes:")
        st.write(st.session_state["results"])
        st.button("Restart", key="restart_button")
        if st.session_state["restart_button"]:
            st.session_state["page"] = 1  # Restart to page 1

def calculate_risk_factor(serves_per_day):
    risk_factor = 0
    for food, serves in serves_per_day.items():
        if serves:
            try:
                serves = float(serves.split()[0])  # Extract numeric part from slider label
                if food in ["Refined grains", "Processed meats", "Sweetened beverages", "Added sugars", "Added salts"]:
                    risk_factor += serves
            except ValueError:
                st.warning(f"Invalid input for serves of {food}. Please enter a valid number.")
    return risk_factor

def predict_diabetes_risk(risk_factor):
    # Load your trained model (replace with your actual model loading code)
    model = RandomForestClassifier()  # Example - replace with your model loading code
    model.load('path_to_your_model')  # Load your trained model
    
    # Create a DataFrame for prediction
    data = pd.DataFrame({'Risk Factor': [risk_factor]})
    
    # Make prediction
    prediction = model.predict_proba(data)[:, 1][0]  # Assuming predicting probability of class 1
    
    return prediction

# Set Streamlit page config
st.set_page_config( 
    page_title="Eat Well Live Well",
    page_icon=":green_salad:",
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = 1

# Display content based on the current page
display_page(st.session_state["page"])
