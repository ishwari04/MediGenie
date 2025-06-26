# 🧠 MediGenie - AI-Powered Healthcare Chatbot

MediGenie is an AI-driven healthcare assistant built using **Machine Learning** and **Streamlit**, designed to predict possible diseases based on user-reported symptoms and recommend appropriate precautions.

🔗 **Live Demo:**
👉 [Access MediGenie App](https://medigenie-limwfsg2wjqpk7dtudstqw.streamlit.app/)

---

## 🚀 Features

* ✅ Diagnose diseases based on selected symptoms
* 📊 Uses Decision Tree Classifier for prediction
* 🔎 Provides description of predicted disease
* 💊 Lists recommended health precautions
* 🌟 Calculates condition severity based on symptom duration
* 🔊 Voice output for better accessibility (via `pyttsx3`)
* 🎨 Beautiful UI with background image support

---

## 🧠 How It Works

1. User selects one or more symptoms.
2. Duration of symptoms is entered (slider).
3. The ML model predicts:

   * Primary possible disease
   * Secondary possibility (for cross-verification)
4. Severity is calculated based on:

   * Number of days
   * Symptom severity scores
5. Displays:

   * Predicted disease(s)
   * Description
   * Precautionary measures
   * Severity advice (Doctor consult or manageable)

---

## 📁 Folder Structure

```
healthcare-chatbot/
│
├── Data/
│   ├── Training.csv
│   └── Testing.csv
│
├── MasterData/
│   ├── symptom_Description.csv
│   ├── symptom_precaution.csv
│   └── Symptom_severity.csv
│
├── streamlit_app.py
├── requirements.txt
└── .gitignore
```

---

## 💪 Technologies Used

* **Python**
* **Streamlit**
* **Pandas, NumPy**
* **Scikit-learn**
* **Pyttsx3** (Text-to-Speech)
* **DecisionTreeClassifier**

---

## 🛆 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/ishwari04/MediGenie.git
cd MediGenie

# 2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate    # For Windows

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the app
streamlit run streamlit_app.py
```

---

## 📸 Preview

![App Preview](https://user-images.githubusercontent.com/your-image-link.png)

---

## 🙌 Acknowledgements

* Medical dataset sourced for academic/demo use
* Inspired by AI use cases in healthcare

---

## ✨ Live Now

📍 [https://medigenie-limwfsg2wjqpk7dtudstqw.streamlit.app/](https://medigenie-limwfsg2wjqpk7dtudstqw.streamlit.app/)

---

## 📬 Contact

Developed with ❤️ by **Ishwari Kakade**
📧 [LinkedIn](https://www.linkedin.com/in/ishwari04/) | 🌐 [GitHub](https://github.com/ishwari04)
