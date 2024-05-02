import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_calculation_page(height, weight):
    st.title('BMI Calculation')
    st.write('Your BMI and category:')
    
    bmi = calculate_bmi(height, weight)
    bmi_category = get_bmi_category(bmi)
    st.write(f'BMI: {bmi:.1f}')
    st.write(f'Category: {bmi_category}')

    # Plot BMI graph
    height_values = np.linspace(100, 250, 100)
    weight_values = np.linspace(0, 200, 100)
    H, W = np.meshgrid(height_values, weight_values)
    BMI = W / ((H / 100) ** 2)
    plt.imshow(BMI, extent=[100, 250, 0, 200], aspect='auto', origin='lower', cmap='viridis')
    plt.scatter(height, weight, color='red')
    plt.xlabel('Height (cm)')
    plt.ylabel
