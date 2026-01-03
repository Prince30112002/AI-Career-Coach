from collections import Counter

# Skill → Career mapping
CAREER_MAP = {
    "data scientist": {"python", "machine learning", "deep learning", "tensorflow", "statistics"},
    "data analyst": {"sql", "power bi", "excel", "python"},
    "machine learning engineer": {"python", "machine learning", "tensorflow"},
    "nlp engineer": {"nlp", "deep learning", "python"},
    "ai engineer": {"python", "machine learning", "deep learning", "nlp"}
}

def recommend_careers(skills, top_n=3):
    skills = set(skill.lower() for skill in skills)
    scores = {}

    for career, required_skills in CAREER_MAP.items():
        match_score = len(skills.intersection(required_skills))
        if match_score > 0:
            scores[career] = match_score

    ranked = Counter(scores).most_common(top_n)
    return ranked


if __name__ == "__main__":
    # Sample extracted skills (from your skill_extractor output)
    extracted_skills = [
        "Python", "Machine Learning", "Deep Learning",
        "NLP", "SQL", "Power BI", "TensorFlow"
    ]

    recommendations = recommend_careers(extracted_skills)

    print("🎯 Career Recommendations:")
    for career, score in recommendations:
        print(f"- {career.title()} (Skill Match Score: {score})")
