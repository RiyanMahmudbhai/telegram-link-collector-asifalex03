# Telegram Link Collector Bot

This is a Telegram bot that collects links from a given URL and filters the links that contain the word "torrent". The bot sends the filtered links back to the user in a `.txt` file.

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
git clone https://github.com/yourusername/telegram-link-collector.git
cd telegram-link-collector
