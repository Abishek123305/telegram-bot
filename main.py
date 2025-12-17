# main.py
import logging
import config
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from handlers.start_handler import start_command
from handlers.weather_handler import weather_command
from handlers.ai_handler import ai_reply
from handlers.pdf_handler import pdf_analyze
from handlers.ocr_handler import ocr_extract
from handlers.reminder_handler import set_reminder
from handlers.resume_handler import analyze_resume
from handlers.quiz_handler import generate_quiz
from handlers.misc_handler import unknown_message

from utils.scheduler import start_scheduler

logging.basicConfig(level=logging.INFO)

async def post_init(application):
    logging.info("Post init: starting scheduler")
    start_scheduler()
    logging.info("Scheduler started")

def build_app():
    app = (
        ApplicationBuilder()
        .token(config.BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(CommandHandler("ask", ai_reply))
    app.add_handler(CommandHandler("remind", set_reminder))
    app.add_handler(CommandHandler("resume", analyze_resume))
    app.add_handler(CommandHandler("quiz", generate_quiz))

    # Document handler (PDF + DOCX)
    app.add_handler(
        MessageHandler(
            filters.Document.MimeType("application/pdf") |
            filters.Document.MimeType(
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            ),
            pdf_analyze
        )
    )

    # OCR
    app.add_handler(MessageHandler(filters.PHOTO, ocr_extract))

    # Fallback
    app.add_handler(MessageHandler(filters.TEXT, unknown_message))

    return app

def main():
    app = build_app()
    logging.info("Starting bot — run_polling()")
    app.run_polling()

if __name__ == "__main__":
    main()
