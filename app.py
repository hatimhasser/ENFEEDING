import streamlit as st

st.title("Enteral Feeding Calculator")

# Input fields
weight = st.number_input("Patient Weight (kg)", min_value=1.0, value=70.0, step=0.1)
kcal_per_kg = st.number_input("Caloric Needs (kcal/kg)", min_value=10, value=25, step=1)
protein_per_kg = st.number_input("Protein Needs (g/kg)", min_value=0.5, value=1.25, step=0.1)
kcal_per_ml = st.number_input("Formula kcal per mL", min_value=0.5, value=1.0, step=0.1)
propofol_rate = st.number_input("Propofol Infusion Rate (mL/hr)", min_value=0.0, value=0.0, step=0.1)

# Calculations
total_calories = weight * kcal_per_kg
propofol_kcal = propofol_rate * 1.1 * 24  # 1.1 kcal/mL for 24 hours
adjusted_calories = max(0, total_calories - propofol_kcal)  # Ensure non-negative kcal

total_protein = weight * protein_per_kg
total_volume = adjusted_calories / kcal_per_ml
feeding_rate = total_volume / 24  # Continuous feeding rate

# Display results
st.subheader("Results")
st.write(f"Total Daily Calories: {adjusted_calories:.1f} kcal")
st.write(f"Total Protein: {total_protein:.1f} g")
st.write(f"Total Daily Volume: {total_volume:.1f} mL")
st.write(f"Feeding Rate: {feeding_rate:.1f} mL/hr")
