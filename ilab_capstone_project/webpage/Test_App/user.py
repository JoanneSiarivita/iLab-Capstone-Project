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
        page = st.button("NEXT >>")

        # Simulate a click on a next page button
        st.session_state["page"] = True


def main():
    user_information_page()

if __name__ == "__main__":
    main()
