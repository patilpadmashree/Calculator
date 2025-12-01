import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Linear Regression App", page_icon="📈")

st.title("📈 Linear Regression Trainer")

st.write("""
Enter X and Y values below and click **Train Model**.
""")

# -----------------------------
# Input section
# -----------------------------
st.subheader("Enter Data Points")

x_input = st.text_area("Enter X values (comma separated)", "1, 2, 3, 4, 5")
y_input = st.text_area("Enter Y values (comma separated)", "2, 4, 5, 4, 5")

def parse_input(text):
    try:
        return np.array([float(i.strip()) for i in text.split(",")])
    except:
        return None

X = parse_input(x_input)
Y = parse_input(y_input)

# Session state for model
if "model" not in st.session_state:
    st.session_state.model = None

# -----------------------------
# Train Model Button
# -----------------------------
if st.button("Train Model"):
    if X is None or Y is None:
        st.error("Please enter valid numbers separated by commas.")
    elif len(X) != len(Y):
        st.error("X and Y must have the same number of values.")
    else:
        X_reshaped = X.reshape(-1, 1)

        model = LinearRegression()
        model.fit(X_reshaped, Y)

        st.session_state.model = model
        st.success("Model trained successfully!")

# -----------------------------
# If model exists → enable prediction + graph
# -----------------------------
if st.session_state.model:

    model = st.session_state.model

    st.write(f"### Model Equation:  **y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}**")

    # Prediction
    st.subheader("Predict New Value")
    new_x = st.number_input("Enter X to predict Y:", value=1.0)
    predicted_y = model.predict(np.array([[new_x]]))[0]

    st.info(f"Predicted Y value: **{predicted_y:.2f}**")

    # Plot
    st.subheader("Regression Plot")

    fig, ax = plt.subplots()
    ax.scatter(X, Y, label="Data Points")

    x_line = np.linspace(min(X), max(X), 100)
    y_line = model.predict(x_line.reshape(-1, 1))
    ax.plot(x_line, y_line, label="Regression Line")

    ax.scatter([new_x], [predicted_y], s=100, label="Prediction Point")

    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.set_title("Linear Regression Fit")
    ax.legend()

    st.pyplot(fig)
else:
    st.warning("Model not trained yet. Enter values and click **Train Model**.")
