# utils/scheduler.py
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

def start_scheduler():
    """
    Start the AsyncIOScheduler — call this from inside the running event loop (e.g. post_init or
    right before/inside `await app.run_polling()`).
    """
    # don't call scheduler.start() if already running
    if not scheduler.running:
        scheduler.start()
    else:
        # already running
        pass

def add_reminder(bot, chat_id, minutes, task):
    # schedule a single notification after 'minutes' minutes
    scheduler.add_job(
        func=lambda: asyncio.create_task(bot.send_message(chat_id=chat_id, text=f"⏰ Reminder: {task}")),
        trigger="date",
        run_date= ( asyncio.get_event_loop().time() + minutes*60 ),
        id=f"reminder-{chat_id}-{task[:10]}",
        replace_existing=True,
        max_instances=1
    )
