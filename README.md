## DUMROO — AI Natural‑Language Data Query (Role‑Based)

Concise, practical tool to let authorized admins ask natural‑language questions about student data.
It translates English queries into safe Pandas filters (using a generative model), then applies the organization's role scope to enforce data visibility.

---

## Quick start (Windows PowerShell)

1. Create a Python 3.10+ virtual environment and activate it.

<<<<<<< HEAD
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
=======
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
>>>>>>> 5b3f33b56418625dbbe52c2cfd83694f101b5ecb
pip install -r requirements.txt
```

<<<<<<< HEAD
2. Provide your Google Generative AI / Gemini API key (do not hardcode):

```powershell
=======
3️⃣ Configure Gemini API Key
Never hardcode your API key.

Windows (PowerShell):
>>>>>>> 5b3f33b56418625dbbe52c2cfd83694f101b5ecb
setx GOOGLE_API_KEY "your_gemini_api_key_here"
# then restart your terminal or reopen PowerShell
```

<<<<<<< HEAD
3. Run the Streamlit demo:

```powershell
=======
macOS / Linux (bash/zsh):
export GOOGLE_API_KEY="your_gemini_api_key_here"

Then restart the terminal.

▶️ Run the Application
>>>>>>> 5b3f33b56418625dbbe52c2cfd83694f101b5ecb
streamlit run app.py
# open http://localhost:8501
```

<<<<<<< HEAD
---

## What this repository contains

- `app.py` — Streamlit demo UI (query input, examples, results)
- `data.csv` — small CSV dataset used by the demo
- `requirements.txt` — Python dependency list

If you remove or rename any of these, update `app.py` accordingly.

---

## High-level behavior / contract

- Input: an English question about the CSV student data.
- Output: a Pandas DataFrame of rows matching the sanitized filter.
- Safety: the system always applies the admin's role-scope filter before returning results.

Role-scope (example): only return rows where both `grade == admin_scope['grade']` and `region == admin_scope['region']`.

---
=======
Access URL:
http://localhost:8501


🧪 Example Queries


Which students haven’t submitted their homework yet?
Show me performance data for grade 8 from last week.
List all upcoming quizzes scheduled for next week.
Show students in grade 8 with scores above 70.
Display all homework submissions from the East region.
>>>>>>> 5b3f33b56418625dbbe52c2cfd83694f101b5ecb

## Data schema (expected columns)

- `student_name` — string
- `grade` — integer
- `class` — string (class/section)
- `homework_status` — string (e.g. "submitted" / "not submitted")
- `quiz_score` — numeric
- `quiz_date` — ISO date (YYYY-MM-DD)
- `region` — string

Make sure `data.csv` uses these headers or adapt `app.py` to your schema.

---

## Example queries to try

<<<<<<< HEAD
- "Which students haven’t submitted their homework yet?"
- "Show students in grade 8 with quiz_score > 70"
- "List upcoming quizzes for the East region"

The model suggests a Pandas filter; the app sanitizes it and enforces the admin scope before running.

---

## Security notes

- Never commit API keys. Use environment variables or secure secrets management.
- The demo enforces a final programmatic filter (grade + region) to limit visibility.
- Treat the model output as untrusted text — always sanitize and validate before evaluation.

---

## Extending this project
=======
Working of Project 


<img width="1920" height="1080" alt="Screenshot 2025-11-12 235048" src="https://github.com/user-attachments/assets/d27e431b-b953-4906-80b6-c3a09ea274f3" />


<img width="1920" height="1080" alt="Screenshot 2025-11-12 235040" src="https://github.com/user-attachments/assets/987fd5cb-3746-424d-8e3b-e5813f370b42" />


>>>>>>> 5b3f33b56418625dbbe52c2cfd83694f101b5ecb

- Swap `data.csv` for a database (Postgres, MySQL, MongoDB) and push filtering to the DB.
- Add authentication (JWT / sessions) and persist admin scopes per user.
- Improve prompt engineering to support follow-ups and clarifying questions.

<<<<<<< HEAD
---

## License & contact

Educational / assignment use. Modify freely for learning. For questions, open an issue in the repository.

---

Quick verification: after editing, run the PowerShell quick start steps above to confirm the demo starts and the UI loads at http://localhost:8501.
=======
This project is for educational use under the Assignment.
Feel free to modify or extend for learning purposes.
>>>>>>> 5b3f33b56418625dbbe52c2cfd83694f101b5ecb
