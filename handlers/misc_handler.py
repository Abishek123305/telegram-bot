async def unknown_message(update, context):
    await update.message.reply_text("I didn't understand. Try /ask, /quiz, /weather, or /resume.")
