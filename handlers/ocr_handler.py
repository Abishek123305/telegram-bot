from utils.ocr_utils import extract_text_from_image

async def ocr_extract(update, context):
    file = await update.message.photo[-1].get_file()
    path = f"data/uploads/{file.file_id}.jpg"
    await file.download_to_drive(path)
    
    text = extract_text_from_image(path)
    await update.message.reply_text("📝 Extracted Text:\n" + text)
