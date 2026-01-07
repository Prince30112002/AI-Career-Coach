from src.skill_extractor import extract_skills

REQUIRED_SKILLS = [
    "Python",
    "SQL",
    "Machine Learning",
    "NLP",
    "Statistics",
    "Cloud"
]

def calculate_ats_score(resume_text: str):
    extracted_skills = extract_skills(resume_text)

    matched = [s for s in REQUIRED_SKILLS if s in extracted_skills]
    missing = [s for s in REQUIRED_SKILLS if s not in extracted_skills]

    score = (len(matched) / len(REQUIRED_SKILLS)) * 100

    return score, matched, missing


# 🔍 Test run
if __name__ == "__main__":
    sample_resume = """
    Data Analyst with experience in Python, SQL, NLP and Machine Learning.
    """

    score, matched, missing = calculate_ats_score(sample_resume)

    print("\n📊 ATS Resume Score")
    print(f"Score: {score:.2f}%")

    print("\n✅ Matched Skills:")
    for s in matched:
        print("-", s)

    print("\n❌ Missing Skills:")
    for s in missing:
        print("-", s)
