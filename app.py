import streamlit as st
import pickle
import pandas as pd

# Load the trained regression model
with open("salary2025_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the education mapping
education_mapping = {'HS': 0, 'BS': 1, 'MS': 2, 'PHD': 3}

# App title
st.title("💼 Salary Predictor")
st.subheader("📈 Predict your salary based on skills, experience, and education")

# User input widgets
education = st.selectbox("Education Level", list(education_mapping.keys()))
years_coding = st.slider("Years of Coding Experience", 0, 40, 5)
country = st.selectbox("Country", ["United States", "United Kingdom", "Germany", "Other"])
codes_java = st.checkbox("Codes in Java")
codes_python = st.checkbox("Codes in Python")
codes_sql = st.checkbox("Codes in SQL")
codes_go = st.checkbox("Codes in Go")

# Map the selected education level to its numeric value
education_num = education_mapping[education]

# Build the feature dictionary for prediction
features = {
    "Education": education_num,
    "YearsCoding": years_coding,
    "Java": int(codes_java),
    "Python": int(codes_python),
    "SQL": int(codes_sql),
    "Go": int(codes_go),
    "Country_Germany": 0,
    "Country_United Kingdom": 0,
    "Country_United States": 0
}

# Set the correct country dummy variable
if country == "United States":
    features["Country_United States"] = 1
elif country == "United Kingdom":
    features["Country_United Kingdom"] = 1
elif country == "Germany":
    features["Country_Germany"] = 1

# Create a DataFrame
input_data = pd.DataFrame([features])

# Section header
st.markdown("### 📊 Salary Prediction")

# Predict button
if st.button("💵 Predict Salary"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Salary: **${prediction:,.2f}**")

st.markdown("---")
st.markdown(
    "<small>📘 Built with ❤️ using Streamlit</small>",
    unsafe_allow_html=True
)
