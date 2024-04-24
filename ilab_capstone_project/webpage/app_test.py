import streamlit as st

st.title('Eat Well Live Well')

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.placeholder = "Type here"

col1, col2 = st.columns([3, 1])  # Adjust column width ratio as needed

with col1:
    st.header("Provide information")
    text_input = st.text_input(
        "Please enter your first name",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    gender_preference = st.radio(
        "Indicate your gender preference",
        key="visibility",
        options=["Female", "Male", "Transgender"],
    )

    # Next button to proceed to the next step
    if st.button("Next"):
        st.session_state.step = "display_info"

with col2:
    st.header("Information provided")
    if "step" in st.session_state and st.session_state.step == "display_info":
        if text_input:
            st.write("Hi", text_input + ",")
            #st.write("Your gender preference is:", gender_preference)
            st.write("If you have experienced any of these symptoms:")
            symptoms = [
                "Blurry vision",
                "Fatigue",
                "Frequent urination",
                "Frequent hunger",
                "Increased thirst",
                "Itching",
                "Patches of darker skin",
                "Slow healing of cuts and wounds",
                "Tingling, numbness, pain in hands and feet",
                "Yeast infection"
            ]
            st.write(symptoms)
            st.write("It is recommended that you seek medical advice.")

            # Let's continue button and end session button
            if st.button("Let's Continue"):
                # Reset session state for next step
                st.session_state.step = None
            if st.button("End Session"):
                # Clear session state and end session
                st.session_state.clear()
