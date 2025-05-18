from telebot import types


def get_design_type_keyboard():
    """Клавиатура для выбора типа дизайна"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton("Ваза")
    btn2 = types.KeyboardButton("Стакан")
    btn3 = types.KeyboardButton("Бокал")
    btn4 = types.KeyboardButton("Декоративное изделие")
    btn5 = types.KeyboardButton("Другое")
    back_btn = types.KeyboardButton("Отмена")

    markup.add(btn1, btn2, btn3, btn4, btn5, back_btn)
    return markup


def get_confirm_keyboard():
    """Клавиатура для подтверждения заказа"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    confirm_btn = types.KeyboardButton("✅ Подтвердить")
    change_btn = types.KeyboardButton("❌ Изменить")
    back_btn = types.KeyboardButton("Отмена")

    markup.add(confirm_btn, change_btn, back_btn)
    return markup

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("🎨 Создать дизайн"),
        types.KeyboardButton("🧪 Тест 'Кто ты из продукции?'"),
        types.KeyboardButton("🎁 Подобрать подарок"),
        types.KeyboardButton("🏭 Гид по заводу"),
        types.KeyboardButton("📞 Связаться с менеджером")
    )
    return markup



def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "🎨 Создать дизайн",
        "🧪 Тест 'Кто ты из продукции?'",
        "🎁 Подобрать подарок",
        "🏭 Гид по заводу",
        "📞 Связаться с менеджером"
    ]
    markup.add(*buttons)
    return markup

def get_back_button():
    """Кнопка 'Назад' для возврата в предыдущее меню"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Назад"))
    markup.add(types.KeyboardButton("Отмена"))
    return markup

def get_tour_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton("🏭 Главный цех"),
        types.KeyboardButton("🏛️ Музей"),
        types.KeyboardButton("🚪 Склад"),
        types.KeyboardButton("⬅️ Назад")
    ]
    markup.add(*buttons)
    return markup