
# TG Link Collector Bot

A Telegram bot that collects and filters links from a given URL. This guide explains how to deploy the bot on a VPS.

## Features

- Collects all links from a provided webpage.
- Filters links containing the word "torrent".
- Saves the filtered links to a `.txt` file.
- Sends the `.txt` file back to the user.

## Prerequisites

1. A VPS with Linux installed (e.g., Ubuntu 20.04 or later).
2. Python 3.8 or higher installed on the VPS.
3. A Telegram Bot API token. You can obtain this by creating a bot through [BotFather](https://core.telegram.org/bots#botfather).

---

## Deployment Steps

### 1. Clone the Repository

Log in to your VPS and clone the bot's repository:
```bash
sudo apt update
sudo apt install git -y
git clone https://github.com/your-username/telegram-link-collector.git
cd telegram-link-collector
```

---

### 2. Install Python and Virtual Environment

Ensure Python is installed:
```bash
sudo apt install python3 python3-pip python3-venv -y
```

Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

### 4. Set Up Your Bot Token

Create a `.env` file in the project directory to store your bot token securely:
```bash
nano .env
```
Add the following content to the file:
```
BOT_API_TOKEN=your_telegram_bot_token
```
Replace `your_telegram_bot_token` with your actual bot token.

**Important:** Add `.env` to `.gitignore` to prevent it from being pushed to the repository:
```bash
echo ".env" >> .gitignore
```

---

### 5. Test the Bot

Run the bot to ensure it works correctly:
```bash
python3 telegram_link_bot.py
```
If the bot starts successfully, press `Ctrl+C` to stop it and proceed with setting up the service.

---

### 6. Create a Systemd Service File

Create a `systemd` service file to run the bot continuously:
```bash
sudo nano /etc/systemd/system/tg_link_collector.service
```

Add the following content:
```ini
[Unit]
Description=TG Link Collector Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/telegram-link-collector/telegram_link_bot.py
WorkingDirectory=/path/to/telegram-link-collector
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
Replace `/path/to/telegram-link-collector` with the actual path to the bot directory (use `pwd` to find the path).

---

### 7. Reload and Enable the Service

Reload the `systemd` daemon and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl start tg_link_collector
```

Enable the service to start on boot:
```bash
sudo systemctl enable tg_link_collector
```

Check the service status:
```bash
sudo systemctl status tg_link_collector
```

---

### 8. Logs and Debugging

To view logs for the bot service:
```bash
sudo journalctl -u tg_link_collector.service
```

---

### 9. Stopping and Restarting the Bot

To stop the bot:
```bash
sudo systemctl stop tg_link_collector
```

To restart the bot:
```bash
sudo systemctl restart tg_link_collector
```

---

## Additional Notes

1. Always keep your `.env` file secure and avoid committing it to version control.
2. Use `screen` or `tmux` for manual testing if necessary.
3. To deploy multiple bots, create separate `systemd` service files with unique names.

---

Enjoy using the TG Link Collector Bot!

