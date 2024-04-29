import streamlit as st

def user_information_page():
    # CSS for page background and text input area
    custom_css = """
    <style>
    body {
        background-image: url('images/background.jpg'); /* Change 'images/background.jpg' to your image path */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stTextInput>div>div>div>input {
        background-color: white !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.title('Eat Well Live Well')
    st.write('Please enter your first name and then click on your gender to begin:')
    
    # Input fields for user information
    name = st.text_input('Your Name')
    gender = st.radio('Gender Preference', ['Male', 'Female', 'Other'])
    
    height = st.number_input('Height (cm)', min_value=0.0, max_value=300.0, value=170.0)
    weight = st.number_input('Weight (kg)', min_value=0.0, max_value=500.0, value=70.0)
    family_diabetes_history = st.radio('Family history of type 2 diabetes', ['Yes', 'No', 'Not sure'])
    physical_activity = st.radio('Physical activity level', ['Active', 'Inactive'])
    smoking = st.radio('Smoker', ['Yes', 'No'])
    alcohol = st.radio('Alcohol consumption', ['Yes', 'No'])

    # Next button to navigate to the next page
    if st.button('Next'):
        # Save user information to session state or database
        # Navigate to the next page (diet page)
        st.write('Navigating to the next page...')

def main():
    user_information_page()

if __name__ == "__main__":
    main()
