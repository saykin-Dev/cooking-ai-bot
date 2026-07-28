# Cooking AI Bot - config
# Version: 0.1.0
...

import os
from dotenv import load_dotenv

load_dotenv()

# Telegram bot token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Deepseek API
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"

# Bot Settings
MAX_MESSAGE_LENGTH = 4096
MAX_RECIPES = 6
REQUESTS_TIMEOUT = 30

# Launch Validation
def validate_config():
    """Check that all important variables are set"""
    errors = []
    if not TELEGRAM_TOKEN:
        errors.append("TELEGRAM_TOKEN not installed in .env file")
    elif TELEGRAM_TOKEN.startswith("your_"):
        errors.append("TELEGRAM_TOKEN not installed. You should go to @BotFather!")

    if not DEEPSEEK_API_KEY:
        errors.append("DEEPSEEK_API_KEY not installed in .env file")
    elif DEEPSEEK_API_KEY.startswith("your_"):
        errors.append("DEEPSEEK_API_KEY not installed. Go to api.deepseek.com!")

    if errors:
        print("\n Config Error!")
        for error in errors:
            print(f" - {error}")
        print()
        return False
    print("Config succesfully launched")
    return True