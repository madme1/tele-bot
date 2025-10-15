import os
from dotenv import load_dotenv
from config.logger import logger

def load_env_vars():
    load_dotenv()

    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    if not TELEGRAM_TOKEN or not CHAT_ID:
        logger.error("Missing TELEGRAM_TOKEN or CHAT_ID in .env")
        raise EnvironmentError("Missing TELEGRAM_TOKEN or CHAT_ID")

    return TELEGRAM_TOKEN, CHAT_ID
