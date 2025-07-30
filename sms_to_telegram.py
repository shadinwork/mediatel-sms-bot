import os
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# ========= CONFIGURATION ========= #
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MEDIATEL_USERNAME = os.getenv("MEDIATEL_USERNAME")
MEDIATEL_PASSWORD = os.getenv("MEDIATEL_PASSWORD")

LOGIN_URL = 'https://mediateluk.com/login'
INBOX_URL = 'https://mediateluk.com/sms'
session = requests.Session()
# ================================= #
# (rest of your code remains same)
