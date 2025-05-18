from telebot import types
import os
from bot.keyboards import get_main_menu

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUIZ_IMAGES_DIR = os.path.join(BASE_DIR, 'static', 'quiz_images')

# Обновлённые вопросы теста (10 вопросов)
QUESTIONS = [
    {
        "question": "Какой цвет вам больше нравится?",
        "options": [
            {"text": "Насыщенный синий", "traits": {"classic": 2, "modern": 1}},
            {"text": "Прозрачный хрусталь", "traits": {"elegant": 3}},
            {"text": "Яркий многоцветный", "traits": {"creative": 2, "bohemian": 1}},
            {"text": "Тёплый янтарный", "traits": {"vintage": 2, "cozy": 1}}
        ]
    },
    {
        "question": "Какой стиль вам ближе?",
        "options": [
            {"text": "Классика", "traits": {"classic": 3}},
            {"text": "Современный минимализм", "traits": {"modern": 3}},
            {"text": "Авангард", "traits": {"creative": 3, "bohemian": 1}},
            {"text": "Винтаж", "traits": {"vintage": 3, "cozy": 1}}
        ]
    },
    {
        "question": "Какой формы изделие вам нравится?",
        "options": [
            {"text": "Строгие геометрические", "traits": {"modern": 2, "classic": 1}},
            {"text": "Плавные изгибы", "traits": {"elegant": 2, "animal": 1}},
            {"text": "Необычные асимметричные", "traits": {"creative": 2, "bohemian": 1}},
            {"text": "Традиционные формы", "traits": {"classic": 2, "vintage": 1}}
        ]
    },
    {
        "question": "Какой материал вам приятнее?",
        "options": [
            {"text": "Тяжёлое стекло", "traits": {"classic": 2, "modern": 1}},
            {"text": "Хрусталь", "traits": {"elegant": 3, "animal": 1}},
            {"text": "Цветное стекло", "traits": {"creative": 2, "bohemian": 1}},
            {"text": "Матовое стекло", "traits": {"vintage": 2, "cozy": 1}}
        ]
    },
    {
        "question": "Какое изделие вы бы выбрали для подарка?",
        "options": [
            {"text": "Вазу", "traits": {"classic": 2, "elegant": 1}},
            {"text": "Декоративную фигуру", "traits": {"animal": 3, "creative": 1}},
            {"text": "Набор посуды", "traits": {"modern": 2, "cozy": 1}},
            {"text": "Ретро изделие", "traits": {"vintage": 3}}
        ]
    },
    {
        "question": "Какое время суток вам милее?",
        "options": [
            {"text": "Утро", "traits": {"classic": 2, "modern": 1}},
            {"text": "День", "traits": {"elegant": 2, "animal": 1}},
            {"text": "Вечер", "traits": {"creative": 2, "bohemian": 1}},
            {"text": "Ночь", "traits": {"vintage": 2, "cozy": 1}}
        ]
    },
    {
        "question": "Какой элемент декора вам ближе?",
        "options": [
            {"text": "Строгие линии", "traits": {"modern": 3}},
            {"text": "Природные мотивы", "traits": {"animal": 3, "elegant": 1}},
            {"text": "Абстракция", "traits": {"creative": 3}},
            {"text": "Ретро элементы", "traits": {"vintage": 3}}
        ]
    },
    {
        "question": "Какой праздник вам нравится больше?",
        "options": [
            {"text": "Официальное мероприятие", "traits": {"classic": 3}},
            {"text": "Творческий вечер", "traits": {"creative": 2, "bohemian": 1}},
            {"text": "Домашние посиделки", "traits": {"cozy": 3}},
            {"text": "Тематическая вечеринка", "traits": {"animal": 2, "modern": 1}}
        ]
    },
    {
        "question": "Какое животное вам симпатичнее?",
        "options": [
            {"text": "Лебедь", "traits": {"elegant": 3}},
            {"text": "Змея", "traits": {"animal": 3}},
            {"text": "Кабан", "traits": {"cozy": 2, "vintage": 1}},
            {"text": "Павлин", "traits": {"creative": 2, "bohemian": 1}}
        ]
    },
    {
        "question": "Какой аксессуар вы бы выбрали?",
        "options": [
            {"text": "Классические часы", "traits": {"classic": 3}},
            {"text": "Стильный шарф", "traits": {"modern": 2, "elegant": 1}},
            {"text": "Яркий браслет", "traits": {"creative": 2, "bohemian": 1}},
            {"text": "Винтажный кулон", "traits": {"vintage": 3}}
        ]
    }
]

# Обновлённая база изделий с новыми вариантами
PRODUCTS = [
    {
        "id": "vase_nemanka",
        "name": "Ваза 'Неманка'",
        "description": "Вы - воплощение элегантности и гармонии. Как эта ваза, вы умеете украшать собой любое пространство, создавая вокруг атмосферу уюта и красоты. В вас сочетаются классика и современность, а ваша внутренняя сила и спокойствие вдохновляют окружающих. Вы цените традиции, но всегда открыты новым впечатлениям и переменам.",
        "image": "vase_nemanka.jpg",
        "traits": {"classic": 4, "elegant": 3}
    },
    {
        "id": "grafine_volna",
        "name": "Графин 'Волна'",
        "description": "Вы - человек с необычным взглядом на мир и яркой индивидуальностью. Как этот графин с волнообразными формами, вы не боитесь выделяться и вносить в жизнь других свежесть и движение. Ваша энергия заряжает, а нестандартный подход помогает находить решения там, где другие видят только преграды. Вы легко адаптируетесь к переменам и умеете удивлять.",
        "image": "grafine_volna.jpg",
        "traits": {"modern": 4, "creative": 3}
    },
    {
        "id": "bokal_crystal",
        "name": "Бокал 'Кристалл'",
        "description": "Вы - воплощение утончённости, честности и внутреннего света. Как кристальный бокал, вы притягиваете внимание своей прозрачностью и искренностью. Вас ценят за чистоту помыслов, умение слушать и поддерживать. Вы любите красивые моменты жизни и умеете находить радость в деталях. Ваша душа - как огранённый кристалл, отражающий свет в самых разных оттенках.",
        "image": "bokal_crystal.jpg",
        "traits": {"elegant": 4, "classic": 2}
    },
    {
        "id": "stakan_retro",
        "name": "Стакан 'Ретро'",
        "description": "Вы - хранитель воспоминаний и семейных традиций. Как этот стакан, вы надёжны, просты и любимы многими поколениями. В вас чувствуется тепло домашнего очага, а ваша доброта и искренность делают вас незаменимым другом. Вы цените простые радости и умеете создавать атмосферу уюта и доверия вокруг себя.",
        "image": "stakan_retro.jpg",
        "traits": {"vintage": 4, "classic": 2}
    },
    {
        "id": "crystal_snake",
        "name": "Хрустальная змея",
        "description": "Вы - загадочная и мудрая личность, обладающая особым шармом. Как хрустальная змея, вы умеете быть разными: то спокойными и созерцательными, то стремительными и решительными. В вас сочетаются интуиция и аналитический ум, вы легко находите выход из сложных ситуаций и умеете вдохновлять других на перемены.",
        "image": "crystal_snake.jpg",
        "traits": {"animal": 4, "elegant": 3, "creative": 2}
    },
    {
        "id": "meshochek",
        "name": "Декоративное изделие 'Мешочек'",
        "description": "Вы - человек-сюрприз, в вас всегда есть что-то необычное и ценное. Как этот декоративный мешочек, вы храните в себе множество талантов и идей, которыми щедро делитесь с близкими. Вы умеете радовать неожиданными поступками и поддерживать атмосферу праздника даже в обычные дни.",
        "image": "meshochek.jpg",
        "traits": {"creative": 4, "bohemian": 3, "modern": 2}
    },
    {
        "id": "kabank_mugs",
        "name": "Набор кружек 'Кабан'",
        "description": "Вы - душа компании, настоящий друг и весёлый собеседник. Как этот набор кружек, вы всегда готовы к встречам и совместным приключениям. Вас ценят за открытость, чувство юмора и умение находить общий язык с разными людьми. Вы любите собирать друзей за одним столом и создавать незабываемые моменты радости и тепла.",
        "image": "kabank_mugs.jpg",
        "traits": {"cozy": 4, "animal": 3, "vintage": 2}
    }
]


def register_handlers(bot):
    user_profiles = {}

    @bot.message_handler(func=lambda msg: msg.text == "🧪 Тест 'Кто ты из продукции?'")
    def start_test(message):
        chat_id = message.chat.id
        user_profiles[chat_id] = {
            "current_question": 0,
            "traits": {
                "classic": 0,
                "modern": 0,
                "elegant": 0,
                "creative": 0,
                "vintage": 0,
                "animal": 0,
                "bohemian": 0,
                "cozy": 0
            }
        }
        ask_question(bot, chat_id)

    def ask_question(bot, chat_id):
        profile = user_profiles[chat_id]
        question = QUESTIONS[profile["current_question"]]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = [types.KeyboardButton(opt["text"]) for opt in question["options"]]
        markup.add(*buttons)
        markup.add(types.KeyboardButton("❌ Отменить тест"))

        bot.send_message(
            chat_id,
            f"Вопрос {profile['current_question'] + 1}/{len(QUESTIONS)}:\n{question['question']}",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: user_profiles.get(msg.chat.id) and
                                    msg.text in [opt["text"] for q in QUESTIONS for opt in q["options"]])
    def handle_answer(message):
        chat_id = message.chat.id
        profile = user_profiles[chat_id]
        current_question = QUESTIONS[profile["current_question"]]

        # Находим выбранный вариант
        selected = next(opt for opt in current_question["options"] if opt["text"] == message.text)

        # Обновляем профиль
        for trait, value in selected["traits"].items():
            profile["traits"][trait] += value

        # Переход к следующему вопросу или результат
        profile["current_question"] += 1
        if profile["current_question"] < len(QUESTIONS):
            ask_question(bot, chat_id)
        else:
            show_result(bot, chat_id)

    def show_result(bot, chat_id):
        profile = user_profiles[chat_id]

        # Находим наиболее подходящее изделие
        best_product = None
        best_score = -1

        for product in PRODUCTS:
            score = 0
            for trait, value in product["traits"].items():
                score += profile["traits"].get(trait, 0) * value

            if score > best_score:
                best_score = score
                best_product = product

        # Отправляем результат
        try:
            image_path = os.path.join(QUIZ_IMAGES_DIR, best_product["image"])
            with open(image_path, 'rb') as photo:
                bot.send_photo(
                    chat_id,
                    photo,
                    caption=f"🎉 Вы - <b>{best_product['name']}</b>!\n\n{best_product['description']}",
                    parse_mode="HTML",
                    reply_markup=get_main_menu()
                )
        except Exception as e:
            print(f"Ошибка загрузки фото: {e}")
            bot.send_message(
                chat_id,
                f"🎉 Вы - <b>{best_product['name']}</b>!\n\n{best_product['description']}",
                parse_mode="HTML",
                reply_markup=get_main_menu()
            )

        del user_profiles[chat_id]

    @bot.message_handler(func=lambda msg: user_profiles.get(msg.chat.id) and msg.text == "❌ Отменить тест")
    def cancel_test(message):
        chat_id = message.chat.id
        bot.send_message(
            chat_id,
            "Тест отменён. Когда будете готовы, попробуйте снова!",
            reply_markup=get_main_menu()
        )
        del user_profiles[chat_id]