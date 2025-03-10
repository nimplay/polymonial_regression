# Project: Polynomial Regression App for Sales Prediction

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

This is a **Streamlit-based web application** that uses **Polynomial Regression** to predict sales based on advertising spend, discount offered, and the number of stores. It is designed to be user-friendly, interactive, and visually appealing.

---

## **Features**

- **Upload CSV Data**: Users can upload their own dataset in CSV format.
- **Interactive Inputs**: Users can input values for advertising spend, discount, and the number of stores to get sales predictions.
- **Visualizations**: Displays interactive plots showing the relationship between each feature and sales.
- **Modern Design**: Professional and responsive design with a custom footer.

---
## **How It Works**

The application uses **Polynomial Regression** to model the relationship between the independent variables (advertising spend, discount, and number of stores) and the dependent variable (sales). It includes:
- **Polynomial Features**: Captures non-linear relationships.
- **Interactive Plots**: Visualizes the regression line for each feature.
- **Prediction**: Predicts sales based on user inputs.

---

## Project Structure
- dataGenerator.py: Generate a synthetic dataset (`complex_sales_data.csv`).
- app.py`: Calculates Polynomial Regression, graphs the results and nteractive web application to visualise the data and model results.

## Install features

- python -m venv myenv
- pip install Flask
- myenv\Scripts\activate
- pip install pandas
- pip install numpy
- pip install matplotlib
- pip install scikit-learn
- pip install streamlit


## How to Run the Project
1. Generate the synthetic dataset:
   ````bash
   python dataGenerator.py

2. Deploy App.
   ````bash
   streamlit run app.py

3. You can add your own complex_sales_data.csv, generate a new cvs file using python generate_sales_data.py or use the example file

# Live


# polymonial_regression

https://polymonialregression-bdsdrcympu4nwrg4fn3awh.streamlit.app/
