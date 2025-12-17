from PyPDF2 import PdfReader

def extract_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume_file(path):
    text = extract_text(path).lower()
    keywords = ["python", "java", "sql", "ml", "ai", "dsa", "projects", "internship"]
    found = [k for k in keywords if k in text]
    score = len(found) / len(keywords) * 100
    return f"Skills detected: {', '.join(found)}\nScore: {score:.1f}%"
