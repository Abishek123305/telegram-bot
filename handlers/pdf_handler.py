from utils.pdf_utils import extract_pdf_text, summarize
from utils.docx_utils import extract_docx_text

async def pdf_analyze(update, context):
    file = await update.message.document.get_file()
    filename = update.message.document.file_name.lower()
    path = f"data/uploads/{filename}"

    await file.download_to_drive(path)

    if filename.endswith(".pdf"):
        text = extract_pdf_text(path)
    elif filename.endswith(".docx"):
        text = extract_docx_text(path)
    else:
        await update.message.reply_text("❌ Unsupported file type")
        return

    if not text.strip():
        await update.message.reply_text("❌ Could not read document text.")
        return

    summary = summarize(text)
    await update.message.reply_text("📄 Document Summary:\n" + summary)
