from telebot import types
from config.settings import Config
import os
import uuid
from datetime import datetime
from bot.keyboards import get_main_menu, get_back_button, get_design_type_keyboard, get_confirm_keyboard

# Папки для хранения данных
UPLOAD_FOLDER = 'user_designs'
DESIGN_BRIEFS_FOLDER = 'design_briefs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DESIGN_BRIEFS_FOLDER, exist_ok=True)


class DesignState:
    AWAITING_TYPE = 1
    AWAITING_DESIGN = 2
    AWAITING_DESCRIPTION = 3
    AWAITING_QUANTITY = 4
    AWAITING_CONFIRMATION = 5


active_design_sessions = {}
design_requests = {}


class DesignRequest:
    def __init__(self, user_id):
        self.user_id = user_id
        self.design_type = None
        self.photo_path = None
        self.description = None
        self.quantity = 1
        self.urgency = 'standard'
        self.created_at = datetime.now()
        self.status = 'new'
        self.request_id = str(uuid.uuid4())[:8]


def register_design_handlers(bot):
    @bot.message_handler(func=lambda msg: msg.text == "🎨 Создать дизайн")
    def start_design_session(message):
        """Начало сессии создания дизайна"""
        chat_id = message.chat.id
        active_design_sessions[chat_id] = DesignState.AWAITING_TYPE
        design_requests[chat_id] = DesignRequest(message.from_user.id)

        bot.send_message(
            chat_id,
            "🖌️ Выберите тип дизайна:",
            reply_markup=get_design_type_keyboard()
        )

    @bot.message_handler(func=lambda msg: (
            active_design_sessions.get(msg.chat.id) == DesignState.AWAITING_TYPE and
            msg.text in ["Ваза", "Стакан", "Бокал", "Декоративное изделие", "Другое"]
    ))
    def handle_design_type(message):
        """Обработка выбора типа дизайна"""
        chat_id = message.chat.id
        design_requests[chat_id].design_type = message.text
        active_design_sessions[chat_id] = DesignState.AWAITING_DESIGN

        bot.send_message(
            chat_id,
            f"Вы выбрали: {message.text}\n\n"
            "Теперь пришлите фото эскиза или текстовое описание:",
            reply_markup=get_back_button()
        )

    @bot.message_handler(
        content_types=['photo'],
        func=lambda msg: active_design_sessions.get(msg.chat.id) == DesignState.AWAITING_DESIGN
    )
    def handle_design_photo(message):
        """Обработка загруженного фото"""
        chat_id = message.chat.id
        try:
            # Сохранение файла
            file_info = bot.get_file(message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            filename = f"design_{message.from_user.id}_{message.message_id}.jpg"
            save_path = os.path.join(UPLOAD_FOLDER, filename)

            with open(save_path, 'wb') as f:
                f.write(downloaded_file)

            design_requests[chat_id].photo_path = save_path
            active_design_sessions[chat_id] = DesignState.AWAITING_DESCRIPTION

            bot.send_message(
                chat_id,
                "📝 Теперь добавьте текстовое описание к вашему эскизу:",
                reply_markup=get_back_button()
            )

        except Exception as e:
            bot.send_message(
                chat_id,
                f"❌ Ошибка при обработке фото: {str(e)}",
                reply_markup=get_main_menu()
            )
            clean_up_session(chat_id)

    @bot.message_handler(
        func=lambda msg: (
                active_design_sessions.get(msg.chat.id) == DesignState.AWAITING_DESCRIPTION and
                msg.text and
                msg.text != "Отмена"
        )
    )
    def handle_design_description(message):
        """Обработка текстового описания"""
        chat_id = message.chat.id
        design_requests[chat_id].description = message.text
        active_design_sessions[chat_id] = DesignState.AWAITING_QUANTITY

        bot.send_message(
            chat_id,
            "🔢 Укажите количество изделий (1-100):",
            reply_markup=get_back_button()
        )

    @bot.message_handler(
        func=lambda msg: (
                active_design_sessions.get(msg.chat.id) == DesignState.AWAITING_QUANTITY and
                msg.text.isdigit() and
                1 <= int(msg.text) <= 100
        )
    )
    def handle_quantity(message):
        """Обработка количества изделий"""
        chat_id = message.chat.id
        design_requests[chat_id].quantity = int(message.text)
        active_design_sessions[chat_id] = DesignState.AWAITING_CONFIRMATION

        # Формируем сводку заказа
        request = design_requests[chat_id]
        summary = (
            f"📋 Сводка заказа:\n\n"
            f"Тип: {request.design_type}\n"
            f"Количество: {request.quantity}\n"
            f"Описание: {request.description}\n\n"
            f"Все верно?"
        )

        if request.photo_path:
            try:
                with open(request.photo_path, 'rb') as photo:
                    bot.send_photo(
                        chat_id,
                        photo,
                        caption=summary,
                        reply_markup=get_confirm_keyboard()
                    )
                    return
            except Exception as e:
                print(f"Ошибка отправки фото: {e}")

        bot.send_message(
            chat_id,
            summary,
            reply_markup=get_confirm_keyboard()
        )

    @bot.message_handler(
        func=lambda msg: (
                active_design_sessions.get(msg.chat.id) == DesignState.AWAITING_CONFIRMATION and
                msg.text in ["✅ Подтвердить", "❌ Изменить"]
        )
    )
    def handle_confirmation(message):
        """Обработка подтверждения заказа"""
        chat_id = message.chat.id
        if message.text == "✅ Подтвердить":
            request = design_requests[chat_id]

            # Сохраняем полное описание заказа
            save_design_brief(chat_id)

            # Уведомление пользователя
            bot.send_message(
                chat_id,
                "🎉 Ваш заказ принят! Наш дизайнер свяжется с вами в течение 24 часов.\n\n"
                f"Номер заказа: #{request.request_id}",
                reply_markup=get_main_menu()
            )

            # Уведомление админа
            notify_admin(bot, chat_id)

        else:
            bot.send_message(
                chat_id,
                "🔄 Начнем процесс заново. Выберите тип дизайна:",
                reply_markup=get_design_type_keyboard()
            )
            active_design_sessions[chat_id] = DesignState.AWAITING_TYPE

        clean_up_session(chat_id)

    @bot.message_handler(
        func=lambda msg: (
                active_design_sessions.get(msg.chat.id) is not None and
                msg.text == "Отмена"
        )
    )
    def cancel_design_session(message):
        """Отмена текущей сессии дизайна"""
        chat_id = message.chat.id
        bot.send_message(
            chat_id,
            "🚫 Создание дизайна отменено",
            reply_markup=get_main_menu()
        )
        clean_up_session(chat_id)

    @bot.message_handler(commands=['my_designs'])
    def show_user_designs(message):
        """Показ истории заказов пользователя"""
        # Здесь можно реализовать просмотр предыдущих заказов
        pass


def save_design_brief(chat_id):
    """Сохранение полного описания заказа в файл"""
    request = design_requests[chat_id]
    filename = f"brief_{request.request_id}.txt"
    filepath = os.path.join(DESIGN_BRIEFS_FOLDER, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Номер заказа: #{request.request_id}\n")
        f.write(f"Пользователь: {request.user_id}\n")
        f.write(f"Тип изделия: {request.design_type}\n")
        f.write(f"Количество: {request.quantity}\n")
        f.write(f"Дата создания: {request.created_at}\n")
        f.write(f"Описание:\n{request.description}\n")
        if request.photo_path:
            f.write(f"Файл эскиза: {request.photo_path}\n")


def notify_admin(bot, chat_id):
    """Уведомление администратора о новом заказе"""
    if not Config.ADMIN_ID:
        return

    request = design_requests[chat_id]
    admin_message = (
        f"🆕 Новый заказ на дизайн!\n\n"
        f"Номер: #{request.request_id}\n"
        f"Тип: {request.design_type}\n"
        f"Количество: {request.quantity}\n"
        f"Пользователь: @{bot.get_chat(chat_id).username}\n\n"
        f"Описание:\n{request.description}"
    )

    try:
        if request.photo_path:
            with open(request.photo_path, 'rb') as photo:
                bot.send_photo(
                    Config.ADMIN_ID,
                    photo,
                    caption=admin_message
                )
        else:
            bot.send_message(Config.ADMIN_ID, admin_message)
    except Exception as e:
        print(f"Ошибка уведомления админа: {e}")


def clean_up_session(chat_id):
    """Очистка данных сессии"""
    if chat_id in active_design_sessions:
        del active_design_sessions[chat_id]
    if chat_id in design_requests:
        del design_requests[chat_id]