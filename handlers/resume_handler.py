from utils.resume_utils import extract_text
from utils.ats_utils import ats_match

async def analyze_resume(update, context):
    if not update.message.reply_to_message or not update.message.reply_to_message.document:
        await update.message.reply_text(
            "❗ Reply to your resume PDF/DOCX with:\n/resume software developer"
        )
        return

    # role input
    role = " ".join(context.args)
    if not role:
        await update.message.reply_text("❗ Usage: /resume <job role>")
        return

    file = await update.message.reply_to_message.document.get_file()
    path = f"data/uploads/resume.pdf"
    await file.download_to_drive(path)

    text = extract_text(path)

    result = ats_match(text, role)

    if not result:
        await update.message.reply_text("❌ Unknown job role")
        return

    response = (
        f"📊 ATS Match Score: {result['score']}%\n\n"
        f"✅ Matched Skills:\n{', '.join(result['matched'])}\n\n"
        f"❌ Missing Skills:\n{', '.join(result['missing'])}"
    )

    await update.message.reply_text(response)
