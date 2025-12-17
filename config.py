# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env from project root

# tolerate either BOT_TOKEN or TELEGRAM_BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")
# tolerate either OPENAI_KEY or OPENAI_API_KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

DB_URL = os.getenv("DB_URL", "sqlite:///data/bot.db")

# quick sanity check (optional)
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in .env — add BOT_TOKEN or TELEGRAM_BOT_TOKEN")
