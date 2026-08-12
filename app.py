import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_performance_model.pkl")


# -----------------------------
# Recommendation Function
# -----------------------------

def generate_recommendations(student):

    recommendations = []

    if student["Study_Hours"] < 4:
        recommendations.append("📚 Increase your study hours.")

    if student["Attendance"] < 75:
        recommendations.append("🏫 Improve your class attendance.")

    if student["Practice_Tests"] < 3:
        recommendations.append("📝 Complete more practice tests.")

    if student["Sleep_Hours"] < 6:
        recommendations.append("😴 Try to get better sleep.")

    if len(recommendations) == 0:
        recommendations.append("✅ Your current study habits look good!")

    return recommendations


# -----------------------------
# Performance Level
# -----------------------------

def performance_level(score):

    if score >= 85:
        return "Excellent 🌟"

    elif score >= 70:
        return "Good 👍"

    elif score >= 50:
        return "Average 📖"

    else:
        return "Needs Improvement ⚠️"


# -----------------------------
# App Title
# -----------------------------

st.title("🎓 Student Performance Predictor")

st.write(
    "Enter student information to predict the final exam score "
    "and receive personalized recommendations."
)


# -----------------------------
# Student Inputs
# -----------------------------

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=15.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

practice_tests = st.number_input(
    "Practice Tests",
    min_value=0,
    max_value=20,
    value=3
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=15.0,
    value=7.0
)


# -----------------------------
# Prediction Button
# -----------------------------

if st.button("🔮 Predict Score"):

    # Create student DataFrame
    new_student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Score": [previous_score],
        "Practice_Tests": [practice_tests],
        "Sleep_Hours": [sleep_hours]
    })

    # Make prediction
    prediction = model.predict(new_student)[0]

    # Keep prediction between 0 and 100
    prediction = max(0, min(100, prediction))

    # Get performance level
    level = performance_level(prediction)

    # Student information
    student = {
        "Study_Hours": study_hours,
        "Attendance": attendance,
        "Previous_Score": previous_score,
        "Practice_Tests": practice_tests,
        "Sleep_Hours": sleep_hours
    }

    # Generate recommendations
    recommendations = generate_recommendations(student)


    # -----------------------------
    # Prediction Result
    # -----------------------------

    st.divider()

    st.subheader("🎯 Prediction Result")

    st.success(
        f"Predicted Final Score: {prediction:.2f} / 100"
    )

    st.info(
        f"📊 Performance Level: {level}"
    )


    # -----------------------------
    # Student Analytics
    # -----------------------------

    st.subheader("📊 Student Analytics")

    analytics_data = pd.DataFrame({
        "Metric": [
            "Study Hours",
            "Attendance",
            "Previous Score",
            "Practice Tests",
            "Sleep Hours"
        ],

        "Value": [
            study_hours,
            attendance,
            previous_score,
            practice_tests,
            sleep_hours
        ]
    })

    st.bar_chart(
        analytics_data.set_index("Metric")
    )


    # -----------------------------
    # Recommendations
    # -----------------------------

    st.subheader("💡 Personalized Recommendations")

    for recommendation in recommendations:
        st.write(recommendation)