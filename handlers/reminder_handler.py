from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ContextTypes
from utils.scheduler import scheduler

async def set_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text(
            "Usage: /remind <minutes> <task>\nExample: /remind 10 Drink water"
        )
        return

    try:
        minutes = int(context.args[0])
        task = " ".join(context.args[1:])
    except ValueError:
        await update.message.reply_text("❌ Minutes must be a number")
        return

    run_time = datetime.now() + timedelta(minutes=minutes)

    scheduler.add_job(
        send_reminder,
        trigger="date",
        run_date=run_time,
        args=[update.effective_chat.id, task]
    )

    await update.message.reply_text(
        f"⏰ Reminder set! I’ll remind you in {minutes} minutes."
    )

async def send_reminder(chat_id, task):
    from utils.bot_instance import bot
    await bot.send_message(chat_id=chat_id, text=f"🔔 Reminder: {task}")
