import os
from dotenv import load_dotenv

load_dotenv()
BOT_API_TOKEN = os.getenv("7771432745:AAFjwPNf-1iwFjyKLb8Z1uJtUpSoQOL87PY")

if not BOT_API_TOKEN:
    raise ValueError("Bot token not found. Please set BOT_API_TOKEN.")
