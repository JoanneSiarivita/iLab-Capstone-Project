import streamlit as st

st.set_page_config(
    page_title="Eat Well Live Well",
    page_icon=":green_salad:",
)

st.title("Eat Well Live Well")
name = st.text_input("Please enter your name:")
gender = st.radio('Gender Preference', ['Male', 'Female', 'Other'])
submit_page1 = st.button("Submit")

if submit_page1:
    st.session_state["name"] = name
    st.session_state["page"] = 1  # Set page state to 1 after submission

# Page 1 content
if st.session_state.get("page") == 1:
    st.write(f"Hi {st.session_state['name']}!")
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

    # Button to proceed to next page
    if st.button("NEXT >>"):
        st.session_state["page"] = 2

# Page 2 content
elif st.session_state.get("page") == 2:
    st.write(f"{st.session_state['name']}, please enter your height and weight.")
    st.write("This helps us to assess if you have a higher risk of diabetes.")

    # Input for height
    height = st.text_input("Height (in cm)", key="height_input")

    # Input for weight
    weight = st.text_input("Weight (in kg)", key="weight_input")

    if st.button("Submit"):
        # Process the height and weight inputs
        if height and weight:
            try:
                height_cm = float(height)
                weight_kg = float(weight)

                # Convert height from cm to meters
                height_m = height_cm / 100.0

                # Calculate BMI
                bmi = weight_kg / (height_m ** 2)

                st.write(f"Your BMI is: {bmi:.2f}")

                # Interpret BMI categories
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
            
        # Button to proceed to next page (optional)
        if st.button("NEXT >>"):
            st.session_state["page"] = 3

# Additional pages can be added similarly by incrementing the page number in session_state and adding corresponding content blocks.
