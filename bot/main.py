import types

from bot.keyboards import get_main_menu
from telebot import TeleBot
from config.settings import Config
from bot.handlers import (
    commands,
    design,
    quiz,
    tour,
    manager,
    gift
)

bot = TeleBot(Config.BOT_TOKEN)

# Регистрация всех обработчиков
commands.register_handlers(bot)
design.register_design_handlers(bot)
quiz.register_handlers(bot)
tour.register_handlers(bot)
manager.register_handlers(bot)
gift.register_handlers(bot)  # Регистрируем обработчики подарков


if __name__ == '__main__':
    print("Бот запущен!")
    bot.infinity_polling()