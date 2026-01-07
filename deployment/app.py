import sys
import os
import streamlit as st

sys.path.append(os.path.abspath("."))

from src.resume_parser import extract_text_from_resume
from src.skill_extractor import extract_skills
from src.career_recommender import recommend_careers
from src.ats_scoring import calculate_ats_score
from src.ml.ats_similarity import ats_similarity

st.set_page_config(page_title="AI Career Coach", layout="wide")

st.title("🤖 AI Career Coach")
st.write("Upload your resume and get career insights")

resume_path = "data/raw/sample resume.pdf"

if st.button("Analyze Resume"):
    try:
        resume_text = extract_text_from_resume(resume_path)

        st.success("Resume parsed successfully!")

        skills = extract_skills(resume_text)
        st.subheader("🧠 Extracted Skills")
        st.write(skills)

        careers = recommend_careers(skills)
        st.subheader("🎯 Career Recommendations")
        for career, score in careers:
            st.write(f"- **{career}** (Match Score: {score})")

        ats_score, matched, missing = calculate_ats_score(resume_text)
        st.subheader("📊 ATS Resume Score")
        st.write(f"Score: **{ats_score:.2f}%**")

        st.write("✅ Matched Skills:", matched)
        st.write("❌ Missing Skills:", missing)

        jd = st.text_area("Paste Job Description")
        if jd:
            sim = ats_similarity(resume_text, jd)
            st.subheader("📈 Resume vs Job Match")
            st.write(f"Similarity: **{sim:.2f}%**")

    except Exception as e:
        st.error(str(e))
