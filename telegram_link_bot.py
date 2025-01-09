from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup
from config import BOT_API_TOKEN
import os

# Function to collect links from the specified webpage
def collect_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Filter links that contain 'torrent' in the URL
        torrent_links = [link for link in links if 'torrent' in link.lower()]
        return torrent_links
    except Exception as e:
        return [f"Error: {e}"]

# Function to save links to a .txt file
def save_links_to_file(links, filename='links.txt'):
    try:
        with open(filename, 'w') as file:
            for link in links:
                file.write(link + "\n")
    except Exception as e:
        print(f"Error saving links to file: {e}")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me a URL, and I'll fetch the torrent links for you.")

# Link collector command handler
async def get_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a URL. Example: /links https://example.com")
        return

    url = context.args[0]
    await update.message.reply_text(f"Fetching torrent links from: {url}")
    
    links = collect_links(url)
    
    if links:
        # Save filtered torrent links to a .txt file
        save_links_to_file(links)
        
        # Send the file back to the user
        with open('links.txt', 'rb') as file:
            await update.message.reply_document(file, filename="torrent_links.txt")
    else:
        await update.message.reply_text("No torrent links found or an error occurred.")

# Main function to start the bot
def main():
    # Create the application object
    application = Application.builder().token(BOT_API_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("links", get_links))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
