🎓 Student Performance Predictor

A machine learning-based application that predicts a student's expected academic performance using factors such as study hours, attendance, previous exam scores, and assignment completion.

📌 Overview

The Student Performance Predictor uses machine learning to analyze academic and behavioral factors that may influence student performance. Users can enter student information through an interactive interface and receive an estimated final score along with basic improvement suggestions.

This project demonstrates the practical use of Python, machine learning, data analysis, and Streamlit to build an interactive predictive application.

✨ Features

- 📚 Study hours analysis
- 📊 Attendance-based analysis
- 📝 Previous score consideration
- ✅ Assignment completion tracking
- 🤖 Machine learning-based score prediction
- 📈 Interactive prediction interface
- 💡 Personalized improvement suggestions
- 🎯 Performance classification

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- CSV Dataset

🧠 Machine Learning Model

The project uses Linear Regression to estimate the student's expected final score.

Input Features

- Daily study hours
- Attendance percentage
- Previous examination score
- Number of completed assignments

Output

The model predicts an estimated final score between 0 and 100.

📂 Project Structure

Student-Performance-Predictor/
│
├── app.py
├── train_model.py
├── student_data.csv
├── student_performance_model.pkl
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/Student-Performance-Predictor.git

Move into the project directory:

cd Student-Performance-Predictor

Install the required dependencies:

pip install -r requirements.txt

▶️ Run the Project

First, train the machine learning model:

python train_model.py

Then start the Streamlit application:

streamlit run app.py

The application will open in your browser.

📊 How It Works

1. The user enters academic information.
2. The trained machine learning model processes the inputs.
3. The system predicts the expected final score.
4. The prediction is classified into a performance category.
5. The application provides basic suggestions for improvement.

🚀 Future Improvements

- Use a larger real-world educational dataset
- Compare multiple machine learning algorithms
- Add data visualization dashboards
- Predict performance categories using classification models
- Add subject-wise performance prediction
- Add historical performance tracking
- Add student progress reports
- Deploy the application online

⚠️ Disclaimer

This project is an educational prototype. The prediction is based on a small demonstration dataset and should not be considered an accurate assessment of real-world student performance.

👩‍💻 Project Status

🚧 Work in Progress
