import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Wellbeing Watcher", page_icon=":green salad:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# Use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style/style.css")
# Import pages
from streamlit_option_menu import option_menu
from user import user_information_page
from diet import diet_page
from bmi import bmi_calculation_page
from cardio import cardiovascular_risk_page
from summary import risk_summary_page


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
    st.sidebar.title("MENU")
    # Create a sidebar menu for page navigation
    selected_page = st.sidebar.radio(" ", list(PAGE_TITLE_MAP.keys()))
    # Display the selected page
    display_page(selected_page)

if __name__ == "__main__":
    main()
