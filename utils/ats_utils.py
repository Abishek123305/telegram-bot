# utils/ats_utils.py

ROLE_KEYWORDS = {
    "software developer": [
        "python", "java", "sql", "oops", "data structures",
        "algorithms", "git", "api", "problem solving"
    ],
    "data analyst": [
        "python", "sql", "excel", "power bi", "tableau",
        "pandas", "numpy", "data visualization", "statistics"
    ],
    "ml engineer": [
        "machine learning", "deep learning", "python",
        "tensorflow", "pytorch", "cnn", "nlp", "model training"
    ]
}

def ats_match(resume_text: str, role: str):
    resume_text = resume_text.lower()
    keywords = ROLE_KEYWORDS.get(role.lower())

    if not keywords:
        return None

    matched = [k for k in keywords if k in resume_text]
    missing = [k for k in keywords if k not in resume_text]

    score = (len(matched) / len(keywords)) * 100

    return {
        "score": round(score, 1),
        "matched": matched,
        "missing": missing
    }
