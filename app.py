{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "740eea68-f399-4d2f-a8e9-0ec9b24071d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-28 00:20:14.080 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-28 00:20:14.081 Session state does not function when running a script without `streamlit run`\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# app.py\n",
    "\n",
    "import streamlit as st\n",
    "import pickle\n",
    "import pandas as pd\n",
    "\n",
    "# Load the trained regression model\n",
    "with open(\"salary2025_model.pkl\", \"rb\") as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "# Define the education mapping\n",
    "education_mapping = {'HS': 0, 'BS': 1, 'MS': 2, 'PHD': 3}\n",
    "\n",
    "# App title\n",
    "st.title(\"💼 Salary Predictor\")\n",
    "st.subheader(\"📈 Predict your salary based on skills, experience, and education\")\n",
    "\n",
    "# User input widgets\n",
    "education = st.selectbox(\"Education Level\", list(education_mapping.keys()))\n",
    "years_coding = st.slider(\"Years of Coding Experience\", 0, 40, 5)\n",
    "country = st.selectbox(\"Country\", [\"United States\", \"United Kingdom\", \"Germany\", \"Other\"])\n",
    "codes_java = st.checkbox(\"Codes in Java\")\n",
    "codes_python = st.checkbox(\"Codes in Python\")\n",
    "codes_sql = st.checkbox(\"Codes in SQL\")\n",
    "codes_go = st.checkbox(\"Codes in Go\")\n",
    "\n",
    "# Map the selected education level to its numeric value\n",
    "education_num = education_mapping[education]\n",
    "\n",
    "# Build the feature dictionary for prediction\n",
    "features = {\n",
    "    \"Education\": education_num,\n",
    "    \"YearsCoding\": years_coding,\n",
    "    \"Java\": int(codes_java),\n",
    "    \"Python\": int(codes_python),\n",
    "    \"SQL\": int(codes_sql),\n",
    "    \"Go\": int(codes_go),\n",
    "    \"Country_Germany\": 0,\n",
    "    \"Country_United Kingdom\": 0,\n",
    "    \"Country_United States\": 0,\n",
    "}\n",
    "\n",
    "# Set the correct country dummy variable\n",
    "if country == \"United States\":\n",
    "    features[\"Country_United States\"] = 1\n",
    "elif country == \"United Kingdom\":\n",
    "    features[\"Country_United Kingdom\"] = 1\n",
    "elif country == \"Germany\":\n",
    "    features[\"Country_Germany\"] = 1\n",
    "# If \"Other\", all three remain 0 (default)\n",
    "\n",
    "# Create a DataFrame from the features\n",
    "input_data = pd.DataFrame([features])\n",
    "\n",
    "# Section header\n",
    "st.markdown(\"### 📊 Salary Prediction\")\n",
    "\n",
    "# Predict button\n",
    "if st.button(\"💵 Predict Salary\"):\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    st.success(f\"💰 Estimated Salary: **${prediction:,.2f}**\")\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\n",
    "    \"<small>📘 Built with ❤️ using Streamlit</small>\",\n",
    "    unsafe_allow_html=True\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c46ed374-4065-43f7-896a-1bcf15439996",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
