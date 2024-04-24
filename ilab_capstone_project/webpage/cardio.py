import streamlit as st

def calculate_cardiovascular_risk(age, gender, bmi, family_diabetes_history, physical_activity, smoking, alcohol):
    # Dummy implementation, replace with actual risk calculation algorithm
    risk_score = 0
    if age > 50:
        risk_score += 1
    if gender == 'Male':
        risk_score += 1
    if bmi >= 30:
        risk_score += 1
    if family_diabetes_history == 'Yes':
        risk_score += 1
    if physical_activity == 'Inactive':
        risk_score += 1
    if smoking == 'Yes':
        risk_score += 1
    if alcohol == 'Yes':
        risk_score += 1
    
    # Normalize risk score
    max_score = 7  # Maximum possible score
    risk_percentage = (risk_score / max_score) * 100
    
    # Determine risk level
    if risk_percentage < 30:
        risk_level = "Low"
    elif risk_percentage < 70:
        risk_level = "Medium"
    else:
        risk_level = "High"
        
    return risk_percentage, risk_level

def cardiovascular_risk_page(age, gender, bmi, family_diabetes_history, physical_activity, smoking, alcohol):
    st.title('Cardiovascular Disease Risk Assessment')
    st.write('Your risk of developing cardiovascular disease:')
    
    risk_percentage, risk_level = calculate_cardiovascular_risk(age, gender, bmi, family_diabetes_history, physical_activity, smoking, alcohol)
    st.write(f'Risk Percentage: {risk_percentage:.1f}%')
    st.write(f'Risk Level: {risk_level}')

    # Next button to navigate to the next page
    if st.button('Next'):
        # Navigate to the next page (risk summary page)
        st.write('Navigating to the next page...')

def main():
    # Dummy values for user information (replace with actual values from previous page)
    age = 30
    gender = 'Male'
    bmi = 25
    family_diabetes_history = 'No'
    physical_activity = 'Active'
    smoking = 'No'
    alcohol = 'No'
    cardiovascular_risk_page(age, gender, bmi, family_diabetes_history, physical_activity, smoking, alcohol)

if __name__ == "__main__":
    main()
