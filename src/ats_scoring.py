# src/ats_scoring.py

from skill_extractor import extract_skills

def calculate_ats_score(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(job_description))

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills.difference(resume_skills)

    score = round((len(matched_skills) / len(jd_skills)) * 100, 2) if jd_skills else 0

    return {
        "ATS Score (%)": score,
        "Matched Skills": list(matched_skills),
        "Missing Skills": list(missing_skills)
    }


# ---------------- TEST RUN ----------------
if __name__ == "__main__":
    resume_text = """
    I have experience in Python, Machine Learning, Deep Learning,
    NLP, SQL, TensorFlow and Power BI.
    """

    job_description = """
    Looking for a Data Scientist with skills in Python, Machine Learning,
    SQL, Statistics, NLP and Cloud.
    """

    result = calculate_ats_score(resume_text, job_description)

    print("\n📊 ATS Resume Score")
    print(f"Score: {result['ATS Score (%)']}%")

    print("\n✅ Matched Skills:")
    for skill in result["Matched Skills"]:
        print("-", skill)

    print("\n❌ Missing Skills:")
    for skill in result["Missing Skills"]:
        print("-", skill)
