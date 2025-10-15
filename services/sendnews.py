import asyncio
from config.logger import logger
from .scraper import fetch_top_ai_news

# This will keep track of already sent news titles (or any unique identifier)
sent_news = set()

async def send_news(bot, chat_id):
    news_items = fetch_top_ai_news()
    
    # Filter news that hasn't been sent yet
    new_news = [item for item in news_items if item not in sent_news]
    
    if not new_news:
        await bot.send_message(chat_id=chat_id, text="No New Updates On AI.")
        logger.info("No new AI news to send.")
        return

    for item in new_news:
        try:
            await bot.send_message(chat_id=chat_id, text=item)
            logger.info("Sent news item to Telegram")
            sent_news.add(item)  # Mark this news as sent
            await asyncio.sleep(2)
        except Exception as e:
            logger.error(f"Failed to send news message: {e}")
