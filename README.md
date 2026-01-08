
# 🤖 AI Career Coach & ATS Resume Analyzer

An **end-to-end AI-powered Career Guidance System** that analyzes resumes, extracts skills, calculates ATS scores, matches resumes with job descriptions, and recommends suitable career paths.

Built with **Python, NLP, and Machine Learning**, designed for real-world **recruitment & career coaching use cases**.

---

## 🚀 Key Features

- 📄 Resume parsing (PDF)
- 🧠 Skill extraction using NLP
- 📊 ATS (Applicant Tracking System) scoring
- 🎯 Career recommendations based on skill match
- 📈 Resume vs Job Description similarity score
- 🌐 Streamlit-ready deployment *(in progress)*

---

## 🧩 Problem Statement

Many candidates get rejected by **ATS systems** despite having strong skills.

This project helps:
- Job seekers improve their resumes
- Measure ATS compatibility
- Identify missing skills
- Get AI-based career recommendations

---

## 🛠️ Tech Stack

- **Programming:** Python  
- **NLP:** Regex, Text Cleaning  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Deployment:** Streamlit  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```

AI_Career_Coach/
│
├── assets/                  # Images & screenshots
│
├── data/
│   ├── raw/
│   │   └── sample resume.pdf
│   └── processed/
│
├── deployment/
│   └── app.py               # Streamlit app (WIP)
│
├── models/                  # Saved ML models
│
├── notebooks/
│   └── 01_exploration.ipynb
│
├── src/
│   ├── resume_parser.py     # Extract text from resume
│   ├── skill_extractor.py   # Skill extraction logic
│   ├── ats_scoring.py       # ATS score calculation
│   ├── career_recommender.py# Career suggestions
│   │
│   ├── ml/
│   │   ├── ats_similarity.py
│   │   ├── model_training.py
│   │   └── predictor.py
│   │
│   ├── nlp/
│   │   └── text_cleaning.py
│   │
│   └── utils/
│       └── helpers.py
│
├── requirements.txt
└── README.md

```

---

## 🧠 Modules Overview

### 🔹 Resume Parser
Extracts clean text from PDF resumes.

### 🔹 Skill Extractor
Identifies technical skills such as:
- Python
- SQL
- Machine Learning
- NLP
- Power BI
- Deep Learning

### 🔹 ATS Scoring
Calculates:
- ATS compatibility score (%)
- Matched vs missing skills

### 🔹 Career Recommendation Engine
Suggests roles like:
- Data Scientist
- Data Analyst
- AI Engineer  

Based on skill match score.

### 🔹 ATS Similarity
Measures resume vs job description similarity using ML techniques.

---

## 📊 Sample Output

```

📊 ATS Resume Score
Score: 66.67%

✅ Matched Skills:

* Python
* SQL
* Machine Learning
* NLP

❌ Missing Skills:

* Cloud
* Statistics

````

---

## ▶️ How to Run Locally

```bash
# Clone repository
git clone https://github.com/Prince30112002/AI-Career-Coach.git
cd AI_Career_Coach

# Install dependencies
pip install -r requirements.txt

# Run individual modules
python src/resume_parser.py
python src/skill_extractor.py
python src/ats_scoring.py
python src/career_recommender.py
````

---

## 🌐 Streamlit App (Coming Soon)

```bash
streamlit run deployment/app.py
```

---

## 🔮 Future Enhancements

* Resume upload via UI
* Job Description upload & comparison
* AI-powered resume improvement suggestions
* OpenAI-based career roadmap
* Cloud deployment

---

## 👤 Author

**Prince Rajak**
📧 Email: [rajakprince30112002@gmail.com](mailto:rajakprince30112002@gmail.com)
🔗 GitHub: [https://github.com/Prince30112002](https://github.com/Prince30112002)

---

⭐ If you find this project useful, consider giving it a **star**!

```


