# handlers/ai_handler.py
from telegram import Update
from telegram.ext import ContextTypes
from utils.ai_api import ask_ai   # <-- FIXED IMPORT

async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("Usage: /ask <your question>")
        return

    # Ask OpenAI
    answer = ask_ai(query)

    # Reply to user
    await update.message.reply_text(answer)
