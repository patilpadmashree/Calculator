import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="📏")

st.title("📏 BMI Calculator App")

st.write("Enter your details below:")

weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=60.0)
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=165.0)

if st.button("Calculate BMI"):
    height_m = height / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)
    st.subheader(f"Your BMI: {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal weight")
    elif 25 <= bmi < 29.9:
        st.info("Overweight")
    else:
        st.error("Obesity")
