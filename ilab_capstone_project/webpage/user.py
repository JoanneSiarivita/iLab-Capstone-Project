import streamlit as st

def user_information_page():
    st.title('Wellbeing Watcher')
    st.write('Please provide the following information:')
    
    # Input fields for user information
    name = st.text_input('Your Name')
    gender = st.radio('Gender Preference', ['Male', 'Female', 'Other'])
    age = st.number_input('Age', min_value=0, max_value=150, value=30)
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
