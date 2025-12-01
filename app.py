import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Linear Regression App", page_icon="📈")

st.title("📈 Linear Regression Trainer")

st.write("""
Upload or enter **X and Y values** to train a Linear Regression model.
""")

st.subheader("Enter Data Points")

# Input for X values
x_input = st.text_area("Enter X values (comma separated)", "1, 2, 3, 4, 5")

# Input for Y values
y_input = st.text_area("Enter Y values (comma separated)", "2, 4, 5, 4, 5")

# Convert inputs to arrays
def parse_input(text):
    try:
        return np.array([float(i.strip()) for i in text.split(",")])
    except:
        return None

X = parse_input(x_input)
Y = parse_input(y_input)

model_trained = False

if X is None or Y is None:
    st.error("Please enter valid numbers separated by commas.")
elif len(X) != len(Y):
    st.error("X and Y must have the same number of values.")
else:
    # Prepare training data
    X_reshaped = X.reshape(-1, 1)

    # Train model
    model = LinearRegression()
    model.fit(X_reshaped, Y)
    model_trained = True

    st.success("Model trained successfully!")

    # Show coefficients
    st.write(f"### Model Equation:  **y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}**")

    # Prediction section
    st.subheader("Predict New Value")
    new_x = st.number_input("Enter X to predict Y:", value=1.0)
    predicted_y = model.predict(np.array([[new_x]]))[0]

    st.info(f"Predicted Y value: **{predicted_y:.2f}**")

    # Plotting section
    st.subheader("Regression Plot")

    fig, ax = plt.subplots()
    ax.scatter(X, Y)               # original data
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.set_title("Linear Regression Fit")

    # Regression line
    x_line = np.linspace(min(X), max(X), 100)
    y_line = model.predict(x_line.reshape(-1, 1))
    ax.plot(x_line, y_line)

    # Highlight prediction
    ax.scatter([new_x], [predicted_y], s=100)

    st.pyplot(fig)
