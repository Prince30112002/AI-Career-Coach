# src/skill_extractor.py

import re

SKILLS_DB = [
    "python", "machine learning", "deep learning", "nlp",
    "sql", "power bi", "tensorflow", "statistics",
    "cloud", "data analysis", "ai"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill.title())

    return list(set(found_skills))


# TEST
if __name__ == "__main__":
    sample_text = "I know Python, SQL, Machine Learning and NLP"
    print("✅ Extracted Skills:")
    for s in extract_skills(sample_text):
        print("-", s)
