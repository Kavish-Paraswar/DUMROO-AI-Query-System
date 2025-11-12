AI-Powered Natural Language Data Query System with Role-Based Access Control

📋 Project Overview

This project demonstrates an AI system that allows admins to query structured student data using natural English questions.
It integrates Google Gemini API with Pandas for intelligent data filtering and Streamlit for an interactive web interface.

Admins can only view data relevant to their assigned scope (grade and region), ensuring role-based data security.

🚀 Features

🗣️ Natural-language to Pandas query translation via Gemini 2.0

🔐 Role-based access restriction (grade & region filter)

📊 Real-time data filtering and visualization using Streamlit

🧩 Clean, modular Python structure (easy to extend with databases)

⚡ Lightweight CSV backend for rapid testing

🏗️ Tech Stack
Component	Technology
AI Model	Google Gemini 2.0-Flash
Language	Python 3.10 +
Data	Pandas + CSV
Interface	Streamlit
Access Control	Custom Role-Scope Filter
📁 Project Structure
dumroo_assignment/
│
├── app.py              # Main Streamlit app
├── data.csv            # Sample dataset
└── requirements.txt    # Dependencies

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/<your-username>/dumroo-assignment.git
cd dumroo-assignment

2️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt is missing:

pip install pandas streamlit google-generativeai

3️⃣ Configure Gemini API Key

Never hardcode your API key.

Windows (PowerShell):

setx GOOGLE_API_KEY "your_gemini_api_key_here"


macOS / Linux (bash/zsh):

export GOOGLE_API_KEY="your_gemini_api_key_here"


Then restart the terminal.

▶️ Run the Application
streamlit run app.py


Access URL:
http://localhost:8501

🧪 Example Queries

Try typing these inside the web interface:

Which students haven’t submitted their homework yet?

Show me performance data for grade 8 from last week.

List all upcoming quizzes scheduled for next week.

Show students in grade 8 with scores above 70.

Display all homework submissions from the East region.

🔒 Role-Based Access Logic

Each admin can only view records matching:

(grade == admin_scope["grade"]) & (region == admin_scope["region"])


This ensures restricted visibility even if broader queries are made.

📊 Sample Output
[AI generated filter] grade == 8 and quiz_date >= '2025-11-05'
[Sanitized] grade == 8 and quiz_date >= '2025-11-05'

  student_name  grade class homework_status  quiz_score   quiz_date region
1        Arjun      8     A    not submitted           0  2025-11-09   East
3        Tanvi      8     B    not submitted           0  2025-11-11   East

💡 Future Improvements

🔁 Connect to live database (MySQL / MongoDB)

💬 Add multi-admin login with JWT or session auth

🤖 Extend Gemini prompts for follow-up contextual questions

📱 Deploy on Streamlit Cloud or Render for demo access

📜 License

This project is for educational use under the Dumroo AI Developer Assignment.
Feel free to modify or extend for learning purposes.