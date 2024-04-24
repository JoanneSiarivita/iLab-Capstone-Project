import streamlit as st

# CSS for background image and text box colors
background = """
<style>
body {
    background-image: url('images/background.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-color: white;
}
</style>
"""
st.markdown(background, unsafe_allow_html=True)

# Import pages
from user import user_information_page
from diet import diet_page
from bmi import bmi_calculation_page
from cardio import cardiovascular_risk_page
from summary import risk_summary_page

# Define page titles
PAGE_TITLE_MAP = {
    "User Information": user_information_page,
    "Diet Recommendations": diet_page,
    "BMI Calculation": bmi_calculation_page,
    "Cardiovascular Disease Risk": cardiovascular_risk_page,
    "Risk Summary": risk_summary_page
}

# Function to display selected page
def display_page(page_title):
    page_function = PAGE_TITLE_MAP[page_title]
    page_function()

# Main function
def main():
    st.sidebar.title("Navigation")

    # Create a sidebar menu for page navigation
    selected_page = st.sidebar.radio("Go to", list(PAGE_TITLE_MAP.keys()))

    # Display the selected page
    display_page(selected_page)

if __name__ == "__main__":
    main()
