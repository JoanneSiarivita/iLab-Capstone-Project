import streamlit as st

def diet_page():
    st.title('What do you eat each day?')
    st.write('Please select the number of servings per day for each food group:')

    # Define food groups and their recommendations
    food_groups = {
        'Fruits': '2-4 servings',
        'Vegetables': '3-5 servings',
        'Grains': '6-8 servings',
        'Proteins': '2-3 servings',
        'Dairy': '2-3 servings',
        'Fats and Oils': 'Use sparingly'
    }

    # Input fields for servings per day
    servings = {}
    for group, recommendation in food_groups.items():
        servings[group] = st.slider(f'{group} ({recommendation})', 0, 10, 0)

    # Next button to navigate to the next page
    if st.button('Next'):
        # Save servings information to session state or database
        # Navigate to the next page (BMI calculation page)
        st.write('Navigating to the next page...')

def main():
    diet_page()

if __name__ == "__main__":
    main()
