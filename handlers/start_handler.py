async def start_command(update, context):
    await update.message.reply_text(
        "Hello! I'm your personal AI assistant bot.\n"
        "Commands:\n"
        "/weather <city>\n"
        "/ask <question>\n"
        "/remind <minutes> <task>\n"
        "/resume <upload resume PDF>\n"
        "/quiz <upload PDF to generate MCQs>\n"
        "Send a PDF for summary.\n"
        "Send an image for OCR."
    )
