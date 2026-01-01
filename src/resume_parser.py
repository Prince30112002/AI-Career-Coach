import os
import PyPDF2


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF resume
    """
    text = ""

    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                text += page.extract_text() or ""

    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Resume file not found at path: {pdf_path}")

    except Exception as e:
        raise Exception(f"❌ Error while reading PDF: {str(e)}")

    return text.strip()


if __name__ == "__main__":

    # ✅ EXACT PATH (space-safe)
    resume_path = os.path.join(
        "data", "raw", "sample resume.pdf"
    )

    print("📄 Looking for resume at:", resume_path)

    resume_text = extract_text_from_pdf(resume_path)

    print("\n✅ Resume text extracted successfully!\n")
    print(resume_text[:1500])   # preview first 1500 characters
