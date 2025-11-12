## DUMROO — AI Natural‑Language Data Query (Role‑Based)

Concise, practical tool to let authorized admins ask natural‑language questions about student data.
It translates English queries into safe Pandas filters (using a generative model), then applies the organization's role scope to enforce data visibility.

---

## Quick start (Windows PowerShell)

1. Create a Python 3.10+ virtual environment and activate it.

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Provide your Google Generative AI / Gemini API key (do not hardcode):

```powershell
setx GOOGLE_API_KEY "your_gemini_api_key_here"
# then restart your terminal or reopen PowerShell
```

3. Run the Streamlit demo:

```powershell
streamlit run app.py
# open http://localhost:8501
```

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

- Swap `data.csv` for a database (Postgres, MySQL, MongoDB) and push filtering to the DB.
- Add authentication (JWT / sessions) and persist admin scopes per user.
- Improve prompt engineering to support follow-ups and clarifying questions.

---

## License & contact

Educational / assignment use. Modify freely for learning. For questions, open an issue in the repository.

---

Quick verification: after editing, run the PowerShell quick start steps above to confirm the demo starts and the UI loads at http://localhost:8501.