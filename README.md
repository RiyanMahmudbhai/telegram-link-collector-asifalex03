
## Features

- Collects all links from a provided webpage.
- Filters links containing the word "torrent".
- Saves the filtered links to a `.txt` file.
- Sends the `.txt` file back to the user.

## Requirements

- Python 3.8+ (preferably)
- A Telegram Bot Token (from [BotFather](https://core.telegram.org/bots#botfather))
- Dependencies in `requirements.txt`

## Installation Guide

### 1. Clone the Repository

First, clone the repository to your local machine or VPS:

```bash
git clone https://github.com/telegram-link-collector-asifalex03
cd telegram-link-collector-asifalex03
```

### 2. Create a Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment to manage the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux or MacOS
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Your Bot Token

**Important**: Do **not** commit your bot token to GitHub for security reasons.

1. **Create a `.env` file** in the project directory with your bot token. Here's an example `.env` file content:

    ```plaintext
    BOT_API_TOKEN=your_telegram_bot_token
    ```

2. The bot will read the token from this `.env` file when it runs.

**Note**: Make sure you add the `.env` file to the `.gitignore` file to avoid pushing it to GitHub. You can do this by adding `.env` to your `.gitignore` file like this:

```plaintext
.env
```

### 5. Run the Bot

To start the bot, run the following command:

```bash
python3 telegram_link_bot.py
```

The bot will now be running and ready to receive commands.

### 6. Deploy on VPS

To deploy on a VPS, follow these steps:

1. **Clone the repository** to your VPS.
2. **Install Python** and **set up a virtual environment** (if not already set up).
3. **Set up the `.env` file** with your bot token on the VPS.
4. **Run the bot** using the command:
    
    ```bash
    python3 telegram_link_bot.py
    ```

If you need the bot to run continuously, you can use tools like **`screen`**, **`tmux`**, or **`systemd`** to keep it running in the background.

---

## Commands

### `/start`
Sends a welcome message and explains how to use the bot.

### `/links <URL>`
Fetches all links from the provided URL, filters links that contain "torrent", saves them to a `.txt` file, and sends it back to the user.

Example:

```plaintext
/links https://telegra.ph/WZ-ML-X-Torrent-Search-01-09-35
```

---

## Contributing

Feel free to fork this repository and contribute to it. If you find bugs or have ideas for improvements, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Important Notes:**  

1. **Sensitive Info**: The bot token should **never be pushed to GitHub**. Store it in a `.env` file, which you can ignore in Git using `.gitignore`.
2. **`.gitignore`**: Make sure `.env` is added to `.gitignore` so that you don’t accidentally share your bot token or other secrets.

Here’s an example of a `.gitignore` file that ignores sensitive files:

```plaintext
# Ignore the environment file where sensitive information is stored
.env
```

---
