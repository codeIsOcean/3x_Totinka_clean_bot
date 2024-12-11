from dotenv import load_dotenv
import os

#Загружаем переменные окружения из файла .env
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# Проверяем что бот загрузился
if BOT_TOKEN is None:
    raise ValueError('BOT_TOKEN is not defined. Please check your .env file or environment variables.')
