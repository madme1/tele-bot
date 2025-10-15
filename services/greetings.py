from config.logger import logger

async def send_greeting(bot, chat_id):
    try:
        await bot.send_message(chat_id=chat_id, text="Hello! 👋 This is your friendly greeting.")
        logger.info("Sent greeting message")
    except Exception as e:
        logger.error(f"Failed to send greeting message: {e}")
