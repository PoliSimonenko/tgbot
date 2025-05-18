from telebot import types
from telebot.types import Message, CallbackQuery
from config.settings import settings
from config.settings import Config
import time
def register_handlers(bot):
    @bot.message_handler(func=lambda msg: msg.text in ["📞 Связаться с менеджером", "Менеджер"])
    def manager_start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("WhatsApp"),
            types.KeyboardButton("Телефон"),
            types.KeyboardButton("Email"),
            types.KeyboardButton("Назад")
        )
        bot.send_message(
            message.chat.id,
            "📞 Выберите способ связи:",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in ["WhatsApp", "Телефон", "Email"])
    def handle_contact_method(message):
        if message.text == "WhatsApp":
            bot.send_message(
                message.chat.id,
                "💬 Наш WhatsApp: +375 (XX) XXX-XX-XX\n"
                "Ссылка: https://wa.me/375XXXXXXXXX"
            )
        elif message.text == "Телефон":
            bot.send_message(
                message.chat.id,
                "☎️ Телефон менеджера: +375 (XX) XXX-XX-XX\n"
                "Часы работы: Пн-Пт 9:00-18:00"
            )
        else:
            msg = bot.send_message(
                message.chat.id,
                "Напишите ваш вопрос для email-обращения:",
                reply_markup=types.ForceReply()
            )
            bot.register_next_step_handler(msg, process_email_request)

    def process_email_request(message):
        bot.send_message(
            Config.ADMIN_ID,
            f"📧 Новый email-запрос от @{message.from_user.username}:\n\n"
            f"{message.text}\n\n"
            f"ID: {message.from_user.id}\n"
            f"Время: {time.strftime('%Y-%m-%d %H:%M')}"
        )
        bot.send_message(
            message.chat.id,
            "✅ Ваш запрос отправлен! Ответ придет в течение 24 часов.",
            reply_markup=types.ReplyKeyboardRemove()
        )