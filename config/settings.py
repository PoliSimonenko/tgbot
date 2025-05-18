import os
from dotenv import load_dotenv
from pathlib import Path

# Загрузка .env из корня проекта
BASE_DIR = Path(__file__).resolve().parent.parent  # Путь к корню проекта
load_dotenv(BASE_DIR / '.env')

class Settings:
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    ADMIN_ID = os.getenv('ADMIN_ID')

# Создаем экземпляр настроек
settings = Settings()  # Это критически важная строка!

class Config:
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    ADMIN_ID = os.getenv('ADMIN_ID')
    WEBHOOK_URL = os.getenv('WEBHOOK_URL', '')

class UserState:
    IDLE = 0
    AWAIT_DESIGN = 1
    AWAIT_TEST_ANSWER = 2

user_states = {}  # Хранение состояний: {user_id: state}