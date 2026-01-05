from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_similarity(resume_text, job_description):
    """
    Calculate ATS similarity score between resume and job description
    using TF-IDF + Cosine Similarity.
    """

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity_score * 100, 2)


if __name__ == "__main__":
    resume_text = """
    Experienced Data Scientist skilled in Python, Machine Learning,
    SQL, NLP, TensorFlow, and Deep Learning.
    """

    job_description = """
    Looking for a Data Scientist with strong knowledge of Python,
    Machine Learning, SQL, NLP, Statistics, and Cloud technologies.
    """

    score = calculate_ats_similarity(resume_text, job_description)

    print("📊 ATS Similarity Score")
    print(f"Resume vs Job Description Match: {score}%")
