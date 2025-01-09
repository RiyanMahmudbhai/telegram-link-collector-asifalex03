import os
from dotenv import load_dotenv

load_dotenv()
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

if not BOT_API_TOKEN:
    raise ValueError("Bot token not found. Please set BOT_API_TOKEN.")
