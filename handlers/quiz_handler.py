from utils.pdf_utils import extract_pdf_text
from utils.ai_api import ask_ai
import os

async def generate_quiz(update, context):
    if not update.message.reply_to_message or not update.message.reply_to_message.document:
        await update.message.reply_text("❗ Reply to a PDF with /quiz")
        return

    os.makedirs("data/uploads", exist_ok=True)

    file = await update.message.reply_to_message.document.get_file()
    path = "data/uploads/quiz.pdf"
    await file.download_to_drive(path)

    text = extract_pdf_text(path)
    prompt = f"Create 5 MCQs with answers from this content:\n{text[:3000]}"

    quiz = ask_ai(prompt)
    await update.message.reply_text("📝 Quiz:\n" + quiz)
