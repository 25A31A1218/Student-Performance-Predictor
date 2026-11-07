import streamlit as st
import joblib


st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# Load trained model
model = joblib.load("student_performance_model.pkl")


st.title("🎓 Student Performance Predictor")

st.write(
    "Predict a student's expected final score using "
    "study habits, attendance, previous performance, "
    "and assignment completion."
)

st.divider()


# Inputs
study_hours = st.slider(
    "Daily Study Hours",
    min_value=0,
    max_value=12,
    value=4
)

attendance = st.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

previous_score = st.slider(
    "Previous Exam Score",
    min_value=0,
    max_value=100,
    value=65
)

assignments_completed = st.slider(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=7
)


if st.button("Predict Performance"):

    input_data = [[
        study_hours,
        attendance,
        previous_score,
        assignments_completed
    ]]

    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))

    st.subheader("📊 Prediction")

    st.metric(
        "Expected Final Score",
        f"{prediction:.1f}/100"
    )


    # Performance category
    if prediction >= 85:

        st.success(
            "Excellent performance predicted! 🌟"
        )

    elif prediction >= 70:

        st.info(
            "Good performance predicted. Keep improving! 👍"
        )

    elif prediction >= 50:

        st.warning(
            "Average performance predicted. "
            "More consistent preparation may help."
        )

    else:

        st.error(
            "Performance may need improvement. "
            "Focus on study consistency and attendance."
        )


    st.divider()

    st.subheader("💡 Suggestions")

    if study_hours < 4:
        st.write(
            "• Consider increasing daily study time gradually."
        )

    if attendance < 75:
        st.write(
            "• Try to improve attendance and attend classes regularly."
        )

    if previous_score < 60:
        st.write(
            "• Review previous topics and identify weak areas."
        )

    if assignments_completed < 7:
        st.write(
            "• Complete assignments consistently to strengthen learning."
        )
