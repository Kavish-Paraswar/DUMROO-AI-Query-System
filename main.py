import pandas as pd
import google.generativeai as genai
import os
from datetime import datetime, timedelta
import streamlit as st

# ---- CONFIG ----
os.environ["GOOGLE_API_KEY"] = "AIzaSyDvMpQ94onIH7JZ0SoDasKIFsKDoLdvti8"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# ---- Load dataset ----
data = pd.read_csv("data.csv")
data["quiz_date"] = pd.to_datetime(data["quiz_date"])

# ---- Helper Functions ----
def interpret_query(query):
    prompt = f"""
Convert this English question into a valid Pandas filter expression.
Columns: student_name, grade, class, homework_status, quiz_score, quiz_date, region.

If the query mentions "last week", use 'quiz_date >= DATE7'.
Return only the condition.

Example:
homework_status == 'not submitted'
or
grade == 8 and quiz_date >= DATE7

Question: {query}
Condition:
"""
    model = genai.GenerativeModel("gemini-2.0-flash")
    resp = model.generate_content(prompt)
    return resp.text.strip()

def sanitize_condition(cond: str):
    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    return cond.replace("DATE7", f"'{seven_days_ago}'")

def run_query(query, user_role, admin_scope, student_name=None):
    try:
        condition = interpret_query(query)
        condition_norm = sanitize_condition(condition)
        filtered = data.query(condition_norm)

        # ---- Role-Based Access ----
        if user_role == "Admin":
            filtered = filtered[
                (filtered["grade"] == admin_scope["grade"]) &
                (filtered["region"] == admin_scope["region"])
            ]
        elif user_role == "Student" and student_name:
            filtered = filtered[filtered["student_name"].str.lower() == student_name.lower()]

        return condition, condition_norm, filtered
    except Exception as e:
        return None, None, f"Error: {e}"

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Dumroo AI Query System", layout="centered")
st.title("🎓 Dumroo AI Data Query System")
st.caption("Ask natural questions about student data with role-based access control.")

# ---- Sidebar Role Selection ----
st.sidebar.header("User Role")
user_role = st.sidebar.radio("Login as:", ["Admin", "Student"])

if user_role == "Admin":
    st.sidebar.subheader("Admin Scope")
    grade = st.sidebar.selectbox("Select Grade", sorted(data["grade"].unique()))
    region = st.sidebar.selectbox("Select Region", sorted(data["region"].unique()))
    admin_scope = {"grade": grade, "region": region}
    student_name = None
else:
    st.sidebar.subheader("Student Access")
    student_name = st.sidebar.selectbox("Select Your Name", sorted(data["student_name"].unique()))
    admin_scope = None

# ---- Query Input ----
query = st.text_input("Enter your question:", placeholder="e.g., Show me performance data for grade 8 from last week")

if query:
    condition, sanitized, result = run_query(query, user_role, admin_scope, student_name)

    if isinstance(result, str):
        st.error(result)
    else:
        st.subheader("AI Generated Filter:")
        st.code(condition, language="python")
        st.subheader("Sanitized Filter:")
        st.code(sanitized, language="python")

        if result.empty:
            st.warning("No results found (or restricted by role).")
        else:
            st.success(f"Results for {user_role}:")
            st.dataframe(result)

st.markdown("---")
st.caption("Powered by Google Gemini • Built for Dumroo AI Developer Assignment")
