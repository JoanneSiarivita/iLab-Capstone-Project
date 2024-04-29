import streamlit as st

# Define the main title and page configuration
st.set_page_config(
    page_title="Eat Well Live Well",
    page_icon=":green_salad:"
)

# Initialize session state variables
if "name" not in st.session_state:
    st.session_state["name"] = ""
if "gender" not in st.session_state:
    st.session_state["gender"] = ""
if "height" not in st.session_state:
    st.session_state["height"] = ""
if "weight" not in st.session_state:
    st.session_state["weight"] = ""
if "selected_meals" not in st.session_state:
    st.session_state["selected_meals"] = []

# Page 1: Name and Gender Input
st.title("Eat Well Live Well")

name = st.text_input("Please enter your name")
gender = st.radio('Gender', ['Male', 'Female', 'Other'])

if st.button("Submit"):
    st.session_state["name"] = name
    st.session_state["gender"] = gender

# Page 2: Height and Weight Input
    st.write(f"Hi {name}!")
    st.write("Please enter your height and weight to assess your risk for diabetes.")

    height = st.number_input("Height (in centimeters)")
    weight = st.number_input("Weight (in kilograms)")

    if st.button("Next"):
        st.session_state["height"] = height
        st.session_state["weight"] = weight

        # Page 3: Meal Selection
        st.write("Now, please select 3 meal options from the list below.")

        meals = ["Grilled Chicken Salad", "Vegetable Stir-Fry", "Salmon with Quinoa", "Oatmeal with Berries"]
        selected_options = st.multiselect("Select 3 meals", meals, key="meals")

        if len(selected_options) == 3 and st.button("Next"):
            st.session_state["selected_meals"] = selected_options

            # Page 4: Servings Selection
            st.write("For each selected meal, how many servings do you typically consume per day?")
            servings = {}
            for meal in selected_options:
                servings[meal] = st.slider(f"{meal} servings per day", 1, 5, 1)

            if st.button("Next"):
                # Page 5: Calculation (with animation)
                st.write("Calculating...")

                # Placeholder for calculation (e.g., risk assessment)
                # Simulate loading animation (lottiefiles.com)
                # st_lottie_url = 'https://assets3.lottiefiles.com/packages/lf20_0nyz3h.json'
                # st_lottie(st_lottie_url, width=200, height=200)

                # Simulate result (low, medium, high risk)
                risk_factor = "Medium"  # Placeholder result
                st.session_state["risk_factor"] = risk_factor

                # Page 6: Result Display and Feedback
                st.write(f"Hi {name}, thank you for using the Eat Well Live Well app (Diabetes edition).")
                st.write(f"Based on the information you provided today, your dietary risk factor for type 2 diabetes is {risk_factor}.")

                feedback = st.radio("Was this application helpful?", ('Yes', 'No'))

                # Further actions based on feedback (e.g., logging responses)
