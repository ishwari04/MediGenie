import streamlit as st

# ✅ Add background image
def add_bg_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://t3.ftcdn.net/jpg/02/38/08/42/360_F_238084232_5XhGUddDZezzJxybvVXzfPp8cOKAuqRp.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_messages_white():
    st.markdown(
        """
        <style>
        .stAlert {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_image()
style_messages_white()



import streamlit as st
import pandas as pd
import pyttsx3
import numpy as np
import csv
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# File paths
TRAINING_PATH = "Data/Training.csv"
TESTING_PATH = "Data/Testing.csv"
DESCRIPTION_PATH = "MasterData/symptom_Description.csv"
PRECAUTION_PATH = "MasterData/symptom_precaution.csv"
SEVERITY_PATH = "MasterData/Symptom_severity.csv"

# Load datasets
training = pd.read_csv(TRAINING_PATH)
testing = pd.read_csv(TESTING_PATH)
cols = training.columns[:-1]
X = training[cols]
y = training['prognosis']
le = preprocessing.LabelEncoder()
y_encoded = le.fit_transform(y)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
reduced_data = training.groupby(training['prognosis']).max()

# Safely load master data
severity_dict = {}
with open(SEVERITY_PATH) as file:
    for row in csv.reader(file):
        if len(row) >= 2:
            severity_dict[row[0]] = int(row[1])

description_dict = {}
with open(DESCRIPTION_PATH) as file:
    for row in csv.reader(file):
        if len(row) >= 2:
            description_dict[row[0]] = row[1]

precaution_dict = {}
with open(PRECAUTION_PATH) as file:
    for row in csv.reader(file):
        if len(row) >= 5:
            precaution_dict[row[0]] = row[1:5]

# Get symptom list
symptom_list = list(cols)

# Streamlit UI
st.title("🧠 MediGenie - AI Healthcare Chatbot")
st.markdown("Select your symptoms and get a diagnosis with suggested precautions.")

selected_symptoms = st.multiselect("Choose your symptoms:", options=symptom_list)
days = st.slider("How many days have you had symptoms?", 1, 30, 3)

if st.button("Diagnose"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        input_vector = [1 if symptom in selected_symptoms else 0 for symptom in cols]
        prediction_encoded = clf.predict([input_vector])[0]
        primary_disease = le.inverse_transform([prediction_encoded])[0]

        # Secondary prediction
        secondary_model = DecisionTreeClassifier()
        secondary_model.fit(X, y)
        test_vector = np.zeros(len(cols))
        for symptom in selected_symptoms:
            if symptom in cols:
                test_vector[cols.get_loc(symptom)] = 1
        secondary_prediction = secondary_model.predict([test_vector])[0]

        # Severity calculation
        severity_score = sum(severity_dict.get(s, 0) for s in selected_symptoms)
        severity_level = (severity_score * days) / (len(selected_symptoms) + 1)

        st.success(f"🩺 Predicted Disease: **{primary_disease}**")
        if primary_disease != secondary_prediction:
            st.info(f"Other possibility: **{secondary_prediction}**")

        st.write("📝 Description:")
        st.write(description_dict.get(primary_disease, "No description available."))

        st.write("💊 Suggested Precautions:")
        for i, item in enumerate(precaution_dict.get(primary_disease, []), 1):
            st.write(f"{i}. {item}")

        if severity_level > 13:
            st.error("⚠️ Severity is high. You should consult a doctor.")
        else:
            st.success("🙂 Severity seems manageable. Follow the precautions.")

        # Voice Output
        engine = pyttsx3.init()
        engine.say(f"You may have {primary_disease}")
        engine.runAndWait()
