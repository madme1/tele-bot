import asyncio
from config.logger import logger
from .latestNewsScarp import fetch_latest_indianexpress_news

sent_news = set()

async def send_latest_news(bot, chat_id):
    news_items = fetch_latest_indianexpress_news()
    
    new_news = [item for item in news_items if item not in sent_news]

    if not new_news:
        await bot.send_message(chat_id=chat_id, text="No New Updates On AI.")
        logger.info("No new Indian Express news to send.")
        return

    for item in new_news:
        try:
            await bot.send_message(chat_id=chat_id, text=item)
            logger.info("Sent news item to Telegram")
            sent_news.add(item)
            await asyncio.sleep(2)
        except Exception as e:
            logger.error(f"Failed to send news message: {e}")
