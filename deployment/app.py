import sys
import os

# 🔧 Fix path so that src/ modules are accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from pathlib import Path

# 📦 Import project modules
from src.resume_parser import extract_text_from_resume
from src.skill_extractor import extract_skills_from_text
from src.career_recommender import recommend_careers
from src.ats_scoring import calculate_ats_score
from src.ml.ats_similarity import calculate_similarity_score


# -------------------- UI CONFIG --------------------
st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Career Coach & ATS Analyzer")
st.write("Upload your resume and get **skills, ATS score, career recommendations, and JD similarity**")

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF or TXT)",
    type=["pdf", "txt"]
)

job_description = st.text_area(
    "🧾 Paste Job Description",
    placeholder="Paste the job description here..."
)

required_skills_input = st.text_input(
    "🛠️ Required Skills (comma separated)",
    placeholder="Python, SQL, Machine Learning, NLP"
)

# -------------------- PROCESS --------------------
if uploaded_file and job_description and required_skills_input:

    with st.spinner("🔍 Analyzing resume..."):

        # Save uploaded file temporarily
        temp_path = Path("temp_resume.pdf")
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        # Extract resume text
        resume_text = extract_text_from_resume(str(temp_path))

        # Extract skills
        extracted_skills = extract_skills_from_text(resume_text)

        # Required skills list
        required_skills = [s.strip() for s in required_skills_input.split(",")]

        # ATS Score
        ats_score, matched, missing = calculate_ats_score(
            extracted_skills,
            required_skills
        )

        # Career recommendations
        career_results = recommend_careers(extracted_skills)

        # Similarity score
        similarity_score = calculate_similarity_score(
            resume_text,
            job_description
        )

        # Remove temp file
        os.remove(temp_path)

    # -------------------- RESULTS --------------------
    st.success("✅ Analysis Complete!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Extracted Skills")
        st.write(", ".join(extracted_skills))

        st.subheader("📊 ATS Resume Score")
        st.metric("ATS Score", f"{ats_score:.2f}%")

        st.subheader("✅ Matched Skills")
        st.write(", ".join(matched) if matched else "None")

        st.subheader("❌ Missing Skills")
        st.write(", ".join(missing) if missing else "None")

    with col2:
        st.subheader("🎯 Career Recommendations")
        for role, score in career_results:
            st.write(f"**{role}** — Skill Match: {score}")

        st.subheader("📈 Resume vs Job Description Similarity")
        st.metric("Similarity Score", f"{similarity_score:.2f}%")

else:
    st.info("⬆️ Upload resume, add job description & required skills to start.")
