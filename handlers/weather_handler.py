from telegram import Update
from telegram.ext import ContextTypes
from utils.weather_api import get_weather

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Usage: /weather <city>")
        return
    
    city = " ".join(context.args)
    weather = get_weather(city)

    await update.message.reply_text(weather)
