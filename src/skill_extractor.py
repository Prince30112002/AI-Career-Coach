import re

# Common tech + non-tech skills (expandable)
SKILL_SET = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "data science", "data analysis", "nlp", "computer vision",
    "tensorflow", "keras", "pytorch", "scikit-learn",
    "power bi", "tableau", "excel",
    "html", "css", "javascript",
    "git", "github", "docker",
    "aws", "azure", "gcp",
    "communication", "leadership", "problem solving"
]


def extract_skills(resume_text: str) -> list:
    """
    Extract skills from resume text using keyword matching
    """
    resume_text = resume_text.lower()
    found_skills = set()

    for skill in SKILL_SET:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text):
            found_skills.add(skill.title())

    return sorted(found_skills)


if __name__ == "__main__":

    # Sample text (temporary testing)
    sample_resume_text = """
    Experienced Data Scientist with strong skills in Python, Machine Learning,
    SQL, NLP, and Deep Learning. Worked with TensorFlow and Power BI.
    """

    skills = extract_skills(sample_resume_text)

    print("✅ Extracted Skills:")
    for skill in skills:
        print("-", skill)
