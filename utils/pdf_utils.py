from PyPDF2 import PdfReader
from utils.ai_api import ask_ai

def extract_pdf_text(path):
    """Extract raw text from a PDF file"""
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def summarize(text):
    """Summarize extracted PDF text using AI"""
    prompt = "Summarize the following content:\n" + text[:4000]
    return ask_ai(prompt)
