import streamlit as st

# Function to display first page
def display_first_page():
    st.title("Eat Well Live Well")
    name = st.text_input("Please enter your name and then click on your gender to begin")
    gender = st.radio('Gender Preference', ['Male', 'Female', 'Other'])
    submit = st.button("Submit")

    if submit:
        st.session_state["name"] = name
        st.write(f"Hi {name}!")
        st.write("The early signs and symptoms of Type 2 Diabetes can include:")
    
        # List of signs
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
    
        # Display signs as bullet points
        st.markdown("\n".join([f"- {sign}" for sign in signs]))

        st.write("If you have recently started experiencing these symptoms, it is recommended that you seek medical advice as soon as possible.")
        
        # Add button to proceed to next page
        next_page = st.button("NEXT >>")

        # Simulate a click on a next page button
        st.session_state["next_page"] = True

# Function to display second page
def display_second_page():
    name = st.session_state["name"]
    st.write(f"{name}, please enter your height and weight.")
    st.write("This helps us to see if you have a higher risk of diabetes.")

    # Input for height
    height = st.text_input("Height (in cm)", key="height_input")

    # Input for weight
    weight = st.text_input("Weight (in kg)", key="weight_input")

    if st.button("Submit"):
        #Process the height and weight inputs
        if height and weight:
            try:
                height_cm=float(height)
                weight_kg = float(weight)

                # convert height from cm to mtr
                height_m = height_cm/100.0

                # calculate bmi
                bmi = weight_kg/ (height_m ** 2)

                st.write(f"Your BMI is :{bmi:.2f}")

                #intepret bmi categories
                if bmi < 18.5:
                    st.write("Your BMI indicates that you are underweight. Let's work towards achieving a healthier weight!")
                elif bmi < 24.9:
                    st.write("Congratulations! Your BMI falls within the normal weight range. Keep up the good work!")
                elif bmi < 29.9:
                    st.write("Your BMI suggests that you are overweight. With dedication and healthy choices, you can achieve your weight goals!")
                else:
                    st.write("Your BMI indicates obesity. It's never too late to start making positive changes for a healthier lifestyle!")
            except ValueError:
                st.write("Please enter valid numeric values for height and weight")
            
            # Add button to proceed to next page
       # next_page = st.button("NEXT >>")

        # Simulate a click on a next page button
        #st.session_state["next_page"] = True

# Function to display third page
def display_third_page():
    name = st.session_state["name"]
    st.write(f"{name}, what do you eat each day?")

    # Define the list of food options
    food_options = [
        "Fruit","Non-starchy vegetable","Starchy vegetable","Refined grains",
        "Whole grains","Processed meats","Unprocessed meats","Eggs","Sweetened beverages",
        "Fruit juice","Saturated fats","Unsaturated fats","Added sugars","Added salts","Dairy"
    ]

    # Display checkboxes for food options
    selected_options=st.multiselect("Select options:", food_options,default=[])

    if len(selected_options) < 3:
        st.warning("Please select up to 3 options.")

    # Dictionary to store serves per day for each selected option
    serves_per_day = {}

    # For each selected option, prompt user to input serves per day
    for index, option in enumerate(selected_options):
        serves_per_day = st.select_slider(f"How many serves of {option} per day?", options=["0-1","2-3","4 or more"])

    # Add a button to submit selection
    if st.button("Submit", key="submit button"):
        # Calculate risk factor based on servings per day
        result=calculate_risk_factor(serves_per_day)
        st.session_state["results"]=result
        st.success("Selections submitted successfully")
        st.session_state["page"] = "results"

    def calculate_risk_factor(serves_per_day):
        risk_factor=0
        for food, serves in serves_per_day.items():
            if food in ["Refined grains","Processed meat","Sweetened beverages","Added sugars","Added salts"]:
                risk_factor += serves_per_day[food]
        return risk_factor    
            
    
    # Add button to proceed to next page
    next_page = st.button("NEXT >>")

    # Simulate a click on a next page button
    st.session_state["next_page"] = True

#Function to display results
def display_results_page():
    name = st.session_state["name"]
    st.write(f"{name}, Thank you for using the Eat Well Live Well App (Diabetes Edition).")
    st.write("Based on the information you provided today, your dietary risk factor for Type 2 Diabetes is {result}.")

         

# Main application logic
def main():
    st.set_page_config(
        page_title="Eat Well Live Well",
        page_icon=":green_salad:"
    )

    if "name" not in st.session_state:
        st.session_state["name"] = ""

    if "page" not in st.session_state:
        st.session_state["page"] = "first"

    if not st.session_state["page"] == "first":
        display_first_page()
    elif st.session_state["page"] == "second":
        display_second_page()
    elif st.session_state["page"] == "third":
        display_third_page()
    elif st.session_state["page"] == "results":
        display_results_page()

if __name__ == "__main__":
    main()

