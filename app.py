import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Function to train the model
def train_model(X, y):
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    return model, poly

# Function to predict sales
def predict_sales(model, poly, advertising, discount, stores):
    input_data = np.array([[advertising, discount, stores]])
    input_poly = poly.transform(input_data)
    return model.predict(input_poly)[0]

# Function to plot results
def plot_results(X, y, model, poly):
    X_poly = poly.transform(X)
    y_pred = model.predict(X_poly)

    # Create larger plots
    fig, ax = plt.subplots(1, 3, figsize=(20, 6))

    # Plot 1: Advertising vs Sales
    ax[0].scatter(X['Advertising'], y, color='blue', label='Actual Data')
    ax[0].plot(np.sort(X['Advertising']), np.sort(y_pred), color='red', label='Regression Line')
    ax[0].set_xlabel('Advertising Spend (in dollars)')
    ax[0].set_ylabel('Sales (in units)')
    ax[0].set_title('Advertising vs Sales')
    ax[0].legend()

    # Plot 2: Discount vs Sales
    ax[1].scatter(X['Discount'], y, color='green', label='Actual Data')
    ax[1].plot(np.sort(X['Discount']), np.sort(y_pred), color='orange', label='Regression Line')
    ax[1].set_xlabel('Discount (in percentage)')
    ax[1].set_ylabel('Sales (in units)')
    ax[1].set_title('Discount vs Sales')
    ax[1].legend()

    # Plot 3: Stores vs Sales
    ax[2].scatter(X['Stores'], y, color='purple', label='Actual Data')
    ax[2].plot(np.sort(X['Stores']), np.sort(y_pred), color='brown', label='Regression Line')
    ax[2].set_xlabel('Number of Stores')
    ax[2].set_ylabel('Sales (in units)')
    ax[2].set_title('Stores vs Sales')
    ax[2].legend()

    st.pyplot(fig)

# Custom footer with HTML and CSS
def add_footer():
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117;
        color: white;
        text-align: center;
        padding: 10px;
        font-family: Arial, sans-serif;
        font-size: 14px;
        z-index: 1000;
    }
    .footer a {
        color: #1E90FF;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        <p>Developed by <a href="https://www.linkedin.com/in/nimrod-acosta/" target="_blank">Nimrod Acosta</a> | © 2025 All rights reserved</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

# Streamlit app configuration
def main():
    # Custom styles
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #F0F2F6;
        }
        .stHeader {
            color: #1E90FF;
            font-size: 36px;
            font-weight: bold;
        }
        .stButton button {
            background-color: #1E90FF;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #0C7BDC;
        }
        .stSuccess {
            color: #28a745;
            font-size: 18px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Polynomial Regression App for Sales Prediction")
    st.write("This app predicts sales based on advertising spend, discount offered, and the number of stores.")

    # Upload CSV file
    st.sidebar.header("Upload CSV File")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("### Preview of the uploaded data:")
        st.write(data.head())

        # Train the model
        X = data[['Advertising', 'Discount', 'Stores']]
        y = data['Sales']
        model, poly = train_model(X, y)

        # Sidebar for input data
        st.sidebar.header("Enter data to predict sales")
        advertising = st.sidebar.number_input("Advertising spend (in dollars):", min_value=1000, max_value=10000, value=5000)
        discount = st.sidebar.number_input("Discount offered (in percentage):", min_value=5, max_value=50, value=20)
        stores = st.sidebar.number_input("Number of stores:", min_value=1, max_value=20, value=10)

        # Predict sales
        if st.sidebar.button("Predict Sales"):
            predicted_sales = predict_sales(model, poly, advertising, discount, stores)
            st.success(f"Predicted sales are: **{predicted_sales:.2f} units**")

        # Show plots
        st.header("Polynomial Regression Plots")
        plot_results(X, y, model, poly)
    else:
        st.warning("Please upload a CSV file to continue.")

    # Add footer
    add_footer()

if __name__ == "__main__":
    main()
