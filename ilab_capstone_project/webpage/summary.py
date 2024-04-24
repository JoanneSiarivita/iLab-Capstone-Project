import streamlit as st

def risk_summary_page(age, gender, bmi, family_diabetes_history, physical_activity, smoking, alcohol):
    st.title('Risk Summary')
    st.write('Based on the information provided and assessments conducted, your overall risk of developing a lifestyle disease is:')

    # Dummy implementation, replace with actual risk assessment algorithm
    overall_risk = "Low"  # Dummy value, replace with actual assessment
    
    st.write(f'Overall Risk Level: {overall_risk}')

    # Feedback section at the bottom
    st.write('')
    feedback = st.radio('Was this assessment helpful?', ['Yes', 'No'])

def main():
    # Dummy values for user information (replace with actual values from previous pages)
    age = 30
    gender = 'Male'
    bmi = 25
    family_diabetes_history = 'No'
    physical_activity = 'Active'
    smoking = 'No'
    alcohol = 'No'
    risk_summary_page(age, gender, bmi, family_diabetes_history, physical_activity, smoking, alcohol)

if __name__ == "__main__":
    main()
