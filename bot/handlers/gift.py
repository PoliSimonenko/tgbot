from telebot import types
from bot.keyboards import get_main_menu, get_back_button
import random
import os

# Правильное определение BASE_DIR с закрытыми скобками
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GIFT_IMAGES_DIR = os.path.join(BASE_DIR, 'static', 'gift_images')

# База данных подарков с фото
GIFT_ITEMS = [
    {
        "name": "Набор шампанок 'France'",
        "description": "Идеальный подарок для ценителей изысканных вечеров и тех, кто любит создавать атмосферу праздника в кругу близких.",
        "price": "90.60 руб.",
        "link": "https://shopneman.by/catalog/shampanki/n-r-shampanok-france-2-sht-up-dr-s-1000-206-khr/",
        "gender": "female",
        "material": "crystal",
        "category": "наборы",
        "image": "france_shampagne.jpg"
    },
    {
        "name": "Змея декоративная",
        "description": "Прекрасный выбор для человека, который ценит оригинальные и символичные подарки, а также любит украшать дом необычными деталями.",
        "price": "24.60 руб.",
        "link": "https://shopneman.by/catalog/dekorativnye-izdeliya/dekor-izdelie-zmeya-600-14-khr/",
        "gender": "unisex",
        "material": "crystal",
        "category": "декоративные изделия",
        "image": "crystal_snake.jpg"
    },
    {
        "name": "Набор хрустальных шахмат",
        "description": "Подарок для стратегов и интеллектуалов, который подчеркнёт статус и станет украшением любого кабинета или гостиной.",
        "price": "839.70 руб.",
        "link": "https://shopneman.by/catalog/dekorativnye-izdeliya/nabor-dekor-izdeliy-sh-d-bestsv-chern-p-u-t-600-14-khr_1/",
        "gender": "male",
        "material": "crystal",
        "category": "наборы",
        "image": "chess_set.jpg"
    },
    {
        "name": "Декор.ваза 'Амелия'",
        "description": "Отличный вариант для тех, кто любит наполнять дом красотой и гармонией, ценит стильные интерьерные детали.",
        "price": "161.10 руб.",
        "link": "https://shopneman.by/catalog/floristika/dekor-vaza-ameliya-tsvetnaya-pudra-1-velbs/",
        "gender": "female",
        "material": "glass",
        "category": "декоративные изделия",
        "image": "amelia_vase.jpg"
    },
    {
        "name": "Ваза-цилиндр",
        "description": "Универсальный подарок для практичных людей, которые ценят лаконичность, надёжность и функциональность.",
        "price": "286.00 руб.",
        "link": "https://shopneman.by/catalog/floristika/vaza-tsilindr-v-170-s-kr-1000-221-khr/",
        "gender": "female",
        "material": "crystal",
        "category": "декоративные изделия",
        "image": "cylinder_vase.jpg"
    },
    {
        "name": "Ваза для сервировки",
        "description": "Подойдёт тем, кто любит принимать гостей и создавать уютную атмосферу за столом.",
        "price": "75.00 руб.",
        "link": "https://shopneman.by/catalog/servirovka/vaza-d-servirovki-stola-900-196-1-velkhr/",
        "gender": "unisex",
        "material": "crystal",
        "category": "декоративные изделия",
        "image": "serving_vase.jpg"
    },
    {
        "name": "Ваза для фруктов",
        "description": "Замечательный подарок для щедрых и гостеприимных людей, которые любят радовать близких вкусными угощениями.",
        "price": "398.90 руб.",
        "link": "https://shopneman.by/catalog/servirovka/vaza-d-fruktov-sinyaya-pudra-pod-up-tk-vne-gruppy-1-velkhr/",
        "gender": "unisex",
        "material": "crystal",
        "category": "посуда",
        "image": "fruit_vase.jpg"
    },
    {
        "name": "Ваза 'Оттепель'",
        "description": "Идея для подарка тем, кто ценит перемены, вдохновение и умеет видеть красоту в каждом дне.",
        "price": "176.10 руб.",
        "link": "https://shopneman.by/catalog/floristika/vaza-d-tsvetov-ottepel-chern-nalepy-krakle-bs/",
        "gender": "female",
        "material": "glass",
        "category": "декоративные изделия",
        "image": "ottepel_vase.jpg"
    },
    {
        "name": "Менажница 'Трио'",
        "description": "Прекрасный выбор для дружелюбных хозяев, которые любят собирать компанию за столом.",
        "price": "50.90 руб.",
        "link": "https://shopneman.by/catalog/servirovka/menazhnitsa-trio-100-8-ris-ot-formy-bs/",
        "gender": "unisex",
        "material": "glass",
        "category": "посуда",
        "image": "trio_tray.jpg"
    },
    {
        "name": "Набор бокалов для шампанского 'France'",
        "description": "Подарок для ценителей стиля и торжественных моментов, который добавит элегантности любому празднику.",
        "price": "231.10 руб.",
        "link": "https://shopneman.by/catalog/bokaly/n-r-bokalov-sh-france-6-sht-120-g-up-dr-s-1000-206-khr/",
        "gender": "unisex",
        "material": "crystal",
        "category": "наборы",
        "image": "france_glasses.jpg"
    },
    {
        "name": "Декор.яйцо (желтое) 'Возрождение'",
        "description": "Символичный подарок для тех, кто ценит обновление, новые начинания и любит необычные украшения для дома.",
        "price": "175.30 руб.",
        "link": "https://shopneman.by/catalog/dekorativnye-izdeliya/dekor-yaytso-zheltoe-met-podst-vozrozhdenie-p-u-vne-gruppy-stskh/",
        "gender": "unisex",
        "material": "crystal",
        "category": "декоративные изделия",
        "image": "egg_decor.jpg"
    },
    {
        "name": "Декоративное изделие 'Мешочек'",
        "description": "Идеально подойдёт для творческих и непредсказуемых людей, которые любят сюрпризы и оригинальные детали в интерьере.",
        "price": "48.20 руб.",
        "link": "https://shopneman.by/catalog/dekorativnye-izdeliya/dekor-izdelie-meshochek-zelenyy-tsvetnaya-pudra-2-velbs/",
        "gender": "unisex",
        "material": "glass",
        "category": "декоративные изделия",
        "image": "glass_pouch.jpg"
    }
]


def filter_gifts(criteria):
    """Фильтрация подарков по заданным критериям"""
    filtered = GIFT_ITEMS.copy()

    if 'price' in criteria:
        price = criteria['price']
        if price == "150":
            filtered = [item for item in filtered if float(item["price"].split()[0]) <= 150]
        elif price == "150-300":
            filtered = [item for item in filtered if 150 < float(item["price"].split()[0]) <= 300]
        elif price == "300-500":
            filtered = [item for item in filtered if 300 < float(item["price"].split()[0]) <= 500]
        elif price == "500":
            filtered = [item for item in filtered if float(item["price"].split()[0]) > 500]

    if 'gender' in criteria:
        gender = criteria['gender']
        filtered = [item for item in filtered if item["gender"] == gender or item["gender"] == "unisex"]

    if 'material' in criteria:
        material = criteria['material']
        filtered = [item for item in filtered if item["material"] == material]

    if 'category' in criteria:
        category = criteria['category']
        filtered = [item for item in filtered if category.lower() in item["category"].lower()]

    return filtered


def send_gifts(chat_id, bot, items, title="🎁 Результаты подбора:"):
    """Отправка списка подарков пользователю с фото"""
    if not items:
        bot.send_message(
            chat_id,
            "😕 По вашим критериям ничего не найдено. Попробуйте изменить параметры поиска.",
            reply_markup=get_back_button()
        )
        return

    bot.send_message(chat_id, title)

    for item in items[:3]:  # Отправляем первые 3 подарка
        try:
            image_path = os.path.join(GIFT_IMAGES_DIR, item["image"])
            with open(image_path, 'rb') as photo:
                bot.send_photo(
                    chat_id,
                    photo,
                    caption=(
                        f"🎁 <b>{item['name']}</b>\n\n"
                        f"{item['description']}\n"
                        f"💵 Цена: {item['price']}\n"
                        f"🔗 <a href='{item['link']}'>Подробнее</a>"
                    ),
                    parse_mode="HTML"
                )
        except Exception as e:
            print(f"Ошибка загрузки фото: {e}")
            bot.send_message(
                chat_id,
                (
                    f"🎁 <b>{item['name']}</b>\n\n"
                    f"{item['description']}\n"
                    f"💵 Цена: {item['price']}\n"
                    f"🔗 <a href='{item['link']}'>Подробнее</a>"
                ),
                parse_mode="HTML"
            )

    if len(items) > 3:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Показать еще"), types.KeyboardButton("⬅️ Назад"))
        bot.send_message(chat_id, f"Найдено {len(items)} вариантов. Хотите увидеть больше?", reply_markup=markup)
    else:
        bot.send_message(chat_id, "Это все варианты по вашему запросу.", reply_markup=get_back_button())


# ... (остальные функции остаются без изменений, как в предыдущем коде)

def register_handlers(bot):
    user_gift_state = {}

    @bot.message_handler(func=lambda msg: msg.text == "🎁 Подобрать подарок")
    def start_gift_selection(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [
            types.KeyboardButton("💰 По бюджету"),
            types.KeyboardButton("👫 По полу"),
            types.KeyboardButton("💎 Стекло или хрусталь"),
            types.KeyboardButton("📦 По категории"),
            types.KeyboardButton("🏆 Лучшие подарки"),
            types.KeyboardButton("⬅️ Назад")
        ]
        markup.add(*buttons)

        bot.send_message(
            message.chat.id,
            "🎁 ПОДОБРАТЬ ПОДАРОК ПО:\n\n"
            "💰 - БЮДЖЕТУ\n"
            "👫 - ПОЛУ ПОЛУЧАТЕЛЯ\n"
            "💎 - МАТЕРИАЛУ (СТЕКЛО/ХРУСТАЛЬ)\n"
            "📦 - КАТЕГОРИИ ИЗДЕЛИЯ\n"
            "🏆 - ПОПУЛЯРНЫЕ ВАРИАНТЫ",
            reply_markup=markup
        )

    # Остальные обработчики остаются без изменений, как в предыдущем коде
    # ...
    # Обработка выбора по бюджету
    @bot.message_handler(func=lambda msg: msg.text == "💰 По бюджету")
    def select_by_budget(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [
            types.KeyboardButton("150"),
            types.KeyboardButton("150-300"),
            types.KeyboardButton("300-500"),
            types.KeyboardButton("500"),
            types.KeyboardButton("⬅️ Назад")
        ]
        markup.add(*buttons)

        bot.send_message(
            message.chat.id,
            "💰 ВЫБЕРИТЕ БЮДЖЕТ:\n\n"
            "150 - до 150 руб.\n"
            "150-300 - от 150 до 300 руб.\n"
            "300-500 - от 300 до 500 руб.\n"
            "500 - от 500 руб. и выше",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in ["150", "150-300", "300-500", "500"])
    def show_gifts_by_budget(message):
        chat_id = message.chat.id
        price = message.text
        user_gift_state[chat_id] = {"criteria": {"price": price}}

        filtered_gifts = filter_gifts({"price": price})
        send_gifts(chat_id, bot, filtered_gifts, f"🎁 Подарки в категории {price} руб.:")

    # Обработка выбора по полу
    @bot.message_handler(func=lambda msg: msg.text == "👫 По полу")
    def select_by_gender(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [
            types.KeyboardButton("👨 Мужчине"),
            types.KeyboardButton("👩 Женщине"),
            types.KeyboardButton("👫 Унисекс"),
            types.KeyboardButton("⬅️ Назад")
        ]
        markup.add(*buttons)

        bot.send_message(
            message.chat.id,
            "👫 ДЛЯ КОГО ПОДБИРАЕМ ПОДАРОК?\n\n"
            "👨 - Мужчине\n"
            "👩 - Женщине\n"
            "👫 - Универсальный вариант",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in ["👨 Мужчине", "👩 Женщине", "👫 Унисекс"])
    def show_gifts_by_gender(message):
        chat_id = message.chat.id
        gender_map = {
            "👨 Мужчине": "male",
            "👩 Женщине": "female",
            "👫 Унисекс": "unisex"
        }
        gender = gender_map[message.text]
        user_gift_state[chat_id] = {"criteria": {"gender": gender}}

        filtered_gifts = filter_gifts({"gender": gender})
        send_gifts(chat_id, bot, filtered_gifts, f"🎁 Подарки для {message.text}:")

    # Обработка выбора по материалу
    @bot.message_handler(func=lambda msg: msg.text == "💎 Стекло или хрусталь")
    def select_by_material(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [
            types.KeyboardButton("🪔 Стекло"),
            types.KeyboardButton("💎 Хрусталь"),
            types.KeyboardButton("⬅️ Назад")
        ]
        markup.add(*buttons)

        bot.send_message(
            message.chat.id,
            "💎 ВЫБЕРИТЕ МАТЕРИАЛ:\n\n"
            "🪔 - Стеклянные изделия\n"
            "💎 - Хрустальные изделия",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in ["🪔 Стекло", "💎 Хрусталь"])
    def show_gifts_by_material(message):
        chat_id = message.chat.id
        material_map = {
            "🪔 Стекло": "glass",
            "💎 Хрусталь": "crystal"
        }
        material = material_map[message.text]
        user_gift_state[chat_id] = {"criteria": {"material": material}}

        filtered_gifts = filter_gifts({"material": material})
        send_gifts(chat_id, bot, filtered_gifts, f"🎁 {message.text} подарки:")

    # Обработка выбора по категории
    @bot.message_handler(func=lambda msg: msg.text == "📦 По категории")
    def select_by_category(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [
            types.KeyboardButton("🍽️ Посуда"),
            types.KeyboardButton("🖼️ Декоративные"),
            types.KeyboardButton("🎁 Наборы"),
            types.KeyboardButton("⬅️ Назад")
        ]
        markup.add(*buttons)

        bot.send_message(
            message.chat.id,
            "📦 ВЫБЕРИТЕ КАТЕГОРИЮ:\n\n"
            "🍽️ - Посуда (вазы, бокалы, графины)\n"
            "🖼️ - Декоративные изделия\n"
            "🎁 - Подарочные наборы",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in ["🍽️ Посуда", "🖼️ Декоративные", "🎁 Наборы"])
    def show_gifts_by_category(message):
        chat_id = message.chat.id
        category_map = {
            "🍽️ Посуда": "Посуда",
            "🖼️ Декоративные": "Декоративные изделия",
            "🎁 Наборы": "Наборы"
        }
        category = category_map[message.text]
        user_gift_state[chat_id] = {"criteria": {"category": category}}

        filtered_gifts = filter_gifts({"category": category})
        send_gifts(chat_id, bot, filtered_gifts, f"🎁 Подарки: {message.text}")

    # Обработка показа лучших подарков
    @bot.message_handler(func=lambda msg: msg.text == "🏆 Лучшие подарки")
    def show_best_gifts(message):
        chat_id = message.chat.id

        def price_to_float(price_str):
            try:
                # Обрабатываем разные форматы цен
                if '-' in price_str:
                    # Берем среднее значение для диапазона (например, "150-300" -> 225)
                    parts = [float(p.strip(' руб.')) for p in price_str.split('-')]
                    return sum(parts) / 2
                elif '+' in price_str:
                    # Для цен типа "500+" берем нижнюю границу
                    return float(price_str.strip('+ руб.'))
                else:
                    return float(price_str.strip(' руб.'))
            except:
                return 0.0  # В случае ошибки возвращаем 0

        # Сортируем по убыванию цены
        best_gifts = sorted(
            GIFT_ITEMS,
            key=lambda x: price_to_float(x["price"]),
            reverse=True
        )[:5]  # Берем топ-5

        for item in best_gifts:
            gift_text = (
                f"🏆 <b>{item['name']}</b>\n\n"
                f"{item['description']}\n"
                f"💵 Цена: {item['price']}\n"
                f"🔗 Ссылка: {item['link']}"
            )
            bot.send_message(
                chat_id,
                gift_text,
                parse_mode="HTML",
                reply_markup=get_back_button()
            )

        # Обработка кнопки "Показать еще"
    @ bot.message_handler(func=lambda msg: msg.text == "Показать еще")

    def show_more_gifts(message):
        chat_id = message.chat.id
        if chat_id not in user_gift_state:
            bot.send_message(chat_id, "Пожалуйста, начните подбор заново.", reply_markup=get_main_menu())
            return

        criteria = user_gift_state[chat_id].get("criteria", {})
        filtered_gifts = filter_gifts(criteria)

        # Отправляем следующие 3 подарка
        already_shown = user_gift_state[chat_id].get("shown_count", 0)
        next_gifts = filtered_gifts[already_shown:already_shown + 3]

        if not next_gifts:
            bot.send_message(chat_id, "Это все варианты по вашему запросу.", reply_markup=get_back_button())
            return

        for item in next_gifts:
            gift_text = (
                f"🎁 <b>{item['name']}</b>\n\n"
                f"{item['description']}\n"
                f"💵 Цена: {item['price']}\n"
                f"🔗 Ссылка: {item['link']}"
            )
            bot.send_message(
                chat_id,
                gift_text,
                parse_mode="HTML",
                reply_markup=get_back_button()
            )

        user_gift_state[chat_id]["shown_count"] = already_shown + len(next_gifts)

        # Проверяем, есть ли еще подарки для показа
        if len(filtered_gifts) > already_shown + len(next_gifts):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("Показать еще"), types.KeyboardButton("⬅️ Назад"))

            bot.send_message(
                chat_id,
                f"Показано {already_shown + len(next_gifts)} из {len(filtered_gifts)}. Хотите увидеть больше?",
                reply_markup=markup
            )
        else:
            bot.send_message(
                chat_id,
                "Это все варианты по вашему запросу.",
                reply_markup=get_back_button()
            )

    @bot.message_handler(func=lambda msg: msg.text == "⬅️ Назад")
    def handle_back(message):
        chat_id = message.chat.id

        # Если нет сохраненного состояния, возвращаем в главное меню
        if chat_id not in user_gift_state:
            bot.send_message(chat_id, "Возвращаемся в главное меню", reply_markup=get_main_menu())
            return

        # Получаем текущее состояние
        current_state = user_gift_state[chat_id].get('navigation', [])

        # Если история навигации пуста, возвращаем в главное меню
        if not current_state:
            bot.send_message(chat_id, "Возвращаемся в главное меню", reply_markup=get_main_menu())
            del user_gift_state[chat_id]
            return

        # Удаляем текущее состояние из истории
        previous_state = current_state.pop()

        # Определяем, куда возвращаться
        if previous_state == "main_menu":
            bot.send_message(chat_id, "Возвращаемся в главное меню", reply_markup=get_main_menu())
            del user_gift_state[chat_id]
        elif previous_state == "gift_selection":
            start_gift_selection(message)
        elif previous_state == "by_budget":
            select_by_budget(message)
        elif previous_state == "by_gender":
            select_by_gender(message)
        elif previous_state == "by_material":
            select_by_material(message)
        elif previous_state == "by_category":
            select_by_category(message)
        else:
            bot.send_message(chat_id, "Возвращаемся в главное меню", reply_markup=get_main_menu())
            del user_gift_state[chat_id]

        # Обновляем состояние
        user_gift_state[chat_id]['navigation'] = current_state