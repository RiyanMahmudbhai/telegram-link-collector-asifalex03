from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
from config import BOT_API_TOKEN

# Function to collect links from the specified webpage
def collect_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        return [f"Error: {e}"]

# Start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Send me a URL, and I'll fetch the links for you.")

# Link collector command handler
def get_links(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Please provide a URL. Example: /links https://example.com")
        return
    
    url = context.args[0]
    update.message.reply_text(f"Fetching links from: {url}")
    links = collect_links(url)
    
    if links:
        message = "\n".join(links[:10])  # Send up to 10 links
        update.message.reply_text(f"Here are the links:\n{message}")
    else:
        update.message.reply_text("No links found or an error occurred.")

# Main function to start the bot
def main():
    if not BOT_API_TOKEN:
        print("Error: Bot token not found.")
        return

    updater = Updater(BOT_API_TOKEN)

    # Add command handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("links", get_links))

    # Start the bot
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
