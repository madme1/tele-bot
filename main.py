import asyncio
from telegram import Bot
from utils.env_loader import load_env_vars
from config.logger import logger
from services.sendnews import send_news
from services.greetings import send_greeting
from services.sendlatestnews import send_latest_news
async def periodic_news(bot, chat_id, interval):
    while True:
        logger.info("Sending AI news")
        await send_news(bot, chat_id)
        logger.info(f"News sent. Sleeping for {interval} seconds.")
        await asyncio.sleep(interval)

async def periodic_greet(bot, chat_id, interval):
    while True:
        logger.info("Sending greeting")
        await send_greeting(bot, chat_id)
        logger.info(f"Greeting sent. Sleeping for {interval} seconds.")
        await asyncio.sleep(interval)
        
async def periodic_latest_news(bot, chat_id, interval):
    while True:
        logger.info("Sending greeting")
        await send_latest_news(bot, chat_id)
        logger.info(f"Greeting sent. Sleeping for {interval} seconds.")
        await asyncio.sleep(interval)

async def main():
    TELEGRAM_TOKEN, CHAT_ID = load_env_vars()
    bot = Bot(token=TELEGRAM_TOKEN)

    news_interval = 60*60*6  # 30 minutes
    greet_interval = 60   # 1 minute
    lastest_news_interval=60*60*3  # 1 minute
    
    news_task = asyncio.create_task(periodic_news(bot, CHAT_ID, news_interval))
    lastest_news_task= asyncio.create_task(periodic_latest_news(bot, CHAT_ID, lastest_news_interval))
    # greet_task = asyncio.create_task(periodic_greet(bot, CHAT_ID, greet_interval))

    # await asyncio.gather(news_task, greet_task)
    await asyncio.gather(news_task,lastest_news_task)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped manually")

