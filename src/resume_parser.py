import os
import PyPDF2

def extract_text_from_resume(resume_path):
    if not os.path.exists(resume_path):
        raise FileNotFoundError("Resume file not found")

    text = ""
    with open(resume_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    return text


if __name__ == "__main__":
    resume_path = "data/raw/sample resume.pdf"
    try:
        resume_text = extract_text_from_resume(resume_path)
        print("✅ Resume text extracted successfully!")
        print(resume_text[:500])
    except Exception as e:
        print("❌ Error:", e)
