from src.skill_extractor import extract_skills

JOB_REQUIRED_SKILLS = [
    "Python", "Sql", "Machine Learning",
    "Statistics", "Cloud", "Nlp"
]

def calculate_ats_score(resume_text):
    resume_skills = extract_skills(resume_text)

    matched = list(set(resume_skills) & set(JOB_REQUIRED_SKILLS))
    missing = list(set(JOB_REQUIRED_SKILLS) - set(resume_skills))

    score = (len(matched) / len(JOB_REQUIRED_SKILLS)) * 100

    return score, matched, missing


if __name__ == "__main__":
    sample_text = """
    Skilled in Python, SQL, Machine Learning and NLP.
    """
    score, matched, missing = calculate_ats_score(sample_text)

    print("📊 ATS Resume Score")
    print(f"Score: {score:.2f}%")

    print("\n✅ Matched Skills:")
    for m in matched:
        print("-", m)

    print("\n❌ Missing Skills:")
    for m in missing:
        print("-", m)
