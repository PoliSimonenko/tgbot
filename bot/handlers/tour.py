from telebot import types
import os
import time
from bot.keyboards import get_back_button, get_main_menu

# Конфигурация путей
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOUR_IMAGES_DIR = os.path.join(BASE_DIR, 'static', 'tour')

# Состояния пользователей
user_tour_status = {}

TOUR_DATA = {
    "🏭 Главный цех": {
        "description": "Сердце производства с 15 печами до 1500°C",
        "photo": "workshop_main.jpg",
        "rooms": {
            "🔨 Формовка": "Ручная выдувка стекла. Познакомьтесь с первым этапом создания стеклянных изделий - формовкой. Здесь вы узнаете, как из раскалённой стекломассы под руками мастера рождаются будущие вазы, графины и бокалы. Этот процесс требует особого мастерства, точности и творческого подхода.\n\n 💡 За смену мастера создают несколько видов изделий, каждый из которых требует точного расчёта количества стекломассы и идеальной техники. После формовки изделия отправляются в печь для отжига, где медленно остывают и приобретают прочность.",
            "🎨 Декорирование": "Ручная роспись. В этом разделе вы увидите, как мастера превращают обычные заготовки в настоящие произведения искусства с помощью гравировки, росписи и других техник. Каждый штрих и узор - это результат кропотливой работы и вдохновения художников.\n\n✂️ Резчики и шлифовальщики используют алмазные инструменты и сложные техники гравировки, чтобы создать изысканный декор. Например, нанесение узора на небольшое пасхальное яйцо занимает всего несколько минут, однако требует большого опыта и внимания к деталям.\n\n✨ После декорирования изделия полируют в специальных кислотных смесях, что придаёт им характерный блеск и прозрачность - именно так рождается настоящее произведение искусства.",
            "🔥 Печи": "12 промышленных печей. Загляните в самое сердце стеклозавода - горячие печи, где рождается стекло. Здесь вы узнаете, как поддерживается нужная температура, как плавится стекломасса и как важно соблюдать технологические тонкости для получения идеального материала.\n\n ⏳ После формовки изделия попадают в печь для отжига (называемую лере), где проводят от полутора до двух часов. Медленное охлаждение предотвращает внутренние напряжения и трещины, обеспечивая прочность и долговечность изделий.\n\n💪 Работа с печами требует особых знаний и точности - от правильного поддержания температуры зависит качество всего выпускаемого стекла."
        }
    },
    "🏛️ Музей": {
        "description": "Музей стекла с уникальной коллекцией",
        "photo": "museum.jpg",
        "halls": {
            "🕰️ Исторический зал": {
                "description": "Экспонаты XIX-XX веков. Погрузитесь в атмосферу ушедших эпох и откройте для себя уникальные изделия, созданные мастерами 'Немана' более века назад.",
                "exhibits": {
                    "🍷 Ваза 'Рубин' (1890)": "Первая продукция завода. Один из старейших экспонатов музея, созданный в конце XIX века.",
                    "🏺 Графин 'Неман' (1925)": "Классика стиля. Исторический графин, выполненный в лаконичном стиле 1920-х годов."
                }
            },
            "✨ Современный зал": {
                "description": "Современные авторские работы. Откройте для себя современные шедевры стеклозавода 'Неман'.",
                "exhibits": {
                    "💎 Скульптура 'Лед'": "Работа 2020 года. Эта изысканная скульптура выполнена из прозрачного стекла.",
                    "🌌 Композиция 'Галактика'": "Инновационные технологии. Оригинальная композиция, вдохновлённая загадками космоса."
                }
            }
        }
    }
}


def register_handlers(bot):
    @bot.message_handler(func=lambda msg: msg.text == "🏭 Гид по заводу")
    def start_tour(message):
        user_tour_status[message.chat.id] = {
            "current_location": "main",
            "current_zone": None,
            "current_hall": None
        }
        show_zones_menu(message.chat.id, bot)

    def show_zones_menu(chat_id, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [types.KeyboardButton(name) for name in TOUR_DATA.keys()]
        markup.add(*buttons)
        markup.add(types.KeyboardButton("⬅️ Назад"))

        bot.send_message(
            chat_id,
            "*👋 Добро пожаловать в виртуальный музей стеклозавода 'Неман'!* - уникальное пространство, где оживает история и современность белорусского стеклоделия! ✨\n\n"
            "Здесь вы сможете совершить увлекательное путешествие по залам, посвящённым разным эпохам и этапам производства, узнать о легендарных изделиях и увидеть редкие экспонаты в мельчайших деталях. 🔍\n\n"
            "🏭 *В музее представлены:*\n"
            "• *Главный цех* - интерактивная экскурсия по этапам производства: формовка, декорирование, работа печей. 🔥\n"
            "• *Музей* - два зала: исторический и современный, где вы увидите как шедевры прошлого, так и актуальные работы мастеров. 🖼️\n\n"
            "🔎 *Выберите зону для посещения:*",
            reply_markup=markup,
            parse_mode="Markdown"
        )
        user_tour_status[chat_id]["current_location"] = "zones"

    @bot.message_handler(func=lambda msg:
    user_tour_status.get(msg.chat.id) and
    msg.text in TOUR_DATA
                         )
    def show_zone(message):
        chat_id = message.chat.id
        zone_name = message.text
        user_tour_status[chat_id] = {
            "current_location": "zone",
            "current_zone": zone_name,
            "current_hall": None
        }

        zone = TOUR_DATA[zone_name]

        # Специальная обработка для главного цеха
        if zone_name == "🏭 Главный цех":
            send_workshop_messages(chat_id, bot)
        else:
            send_zone_info(chat_id, bot, zone_name, zone)

        if 'rooms' in zone:
            show_rooms_menu(chat_id, bot, zone)
        elif 'halls' in zone:
            show_halls_menu(chat_id, bot, zone)

    def send_zone_info(chat_id, bot, zone_name, zone):
        """Отправка информации о зоне (кроме главного цеха)"""
        photo_path = os.path.join(TOUR_IMAGES_DIR, zone['photo'])
        try:
            with open(photo_path, 'rb') as photo_file:
                bot.send_photo(
                    chat_id,
                    photo_file,
                    caption=f"{zone_name}\n\n{zone['description']}"
                )
        except Exception as e:
            print(f"Ошибка загрузки фото: {e}")
            bot.send_message(
                chat_id,
                f"{zone_name}\n\n{zone['description']}"
            )

    def send_workshop_messages(chat_id, bot):
        """Последовательная отправка сообщений о главном цехе"""
        messages = [
            {
                "text": "🔥 *Главный цех стеклозавода «Неман»* (1/5)\n\nЭто сердце производства, где рождаются уникальные стеклянные изделия. Здесь проходят ключевые этапы: формовка, декорирование и работа печей. Современное оборудование и традиции мастеров создают продукцию, известную во всем мире.",
                "photo": "workshop_main.jpg",
                "delay": 5
            },
            {
                "text": "📜 *История главного цеха* (2/5)\n\nВ начале 1960-х годов на заводе началась масштабная реконструкция: построены просторные корпуса с современной вентиляцией, а стекловарение переведено на природный газ. Именно здесь впервые в стране было внедрено автоматизированное производство изделий на ножке - до 6 миллионов штук в год!",
                "photo": "workshop_history.jpg",
                "delay": 5
            },
            {
                "text": "🎨 *Работа мастеров* (3/5)\n\nРабота у печей - священное место для стеклодувов. Извлечённое из печи стекло быстро остывает, и мастера за считанные минуты придают ему форму. Высокая точность и концентрация - залог качества и красоты каждого изделия.",
                "photo": "masters_work.jpg",
                "delay": 5
            },
            {
                "text": "⚙️ *Технологии и инновации* (4/5)\n\nСегодня главный цех сочетает вековые традиции ручного производства с современными технологиями. Это позволяет выпускать как массовую посуду, так и эксклюзивные художественные изделия, которые ценят коллекционеры и любители стекла.",
                "photo": "technologies.jpg",
                "delay": 5
            },
            {
                "text": "📸 *Фото из главного цеха* (5/5)\n\nВот как выглядит главный цех сегодня - просторные светлые помещения, современное оборудование и мастера за работой.",
                "photo": "workshop_now.jpg",
                "delay": 0
            }
        ]

        for msg in messages:
            try:
                photo_path = os.path.join(TOUR_IMAGES_DIR, msg["photo"])
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(
                        chat_id,
                        photo,
                        caption=msg["text"],
                        parse_mode="Markdown"
                    )
            except Exception as e:
                print(f"Ошибка загрузки фото {msg['photo']}: {e}")
                bot.send_message(
                    chat_id,
                    msg["text"],
                    parse_mode="Markdown"
                )

            if msg["delay"] > 0:
                time.sleep(msg["delay"])

    def show_rooms_menu(chat_id, bot, zone):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for room in zone['rooms']:
            markup.add(types.KeyboardButton(room))
        markup.add(types.KeyboardButton("⬅️ Назад"))

        bot.send_message(
            chat_id,
            "Выберите подраздел:",
            reply_markup=markup
        )
        user_tour_status[chat_id]["current_location"] = "rooms"

    def show_halls_menu(chat_id, bot, zone):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for hall in zone['halls']:
            markup.add(types.KeyboardButton(hall))
        markup.add(types.KeyboardButton("⬅️ Назад"))

        bot.send_message(
            chat_id,
            "Выберите зал музея:",
            reply_markup=markup
        )
        user_tour_status[chat_id]["current_location"] = "halls"

    @bot.message_handler(func=lambda msg:
    user_tour_status.get(msg.chat.id) and
    msg.text in get_current_rooms_or_halls(msg.chat.id)
                         )
    def show_room_or_hall(message):
        chat_id = message.chat.id
        zone_name = user_tour_status[chat_id]["current_zone"]
        zone = TOUR_DATA[zone_name]

        if user_tour_status[chat_id]["current_location"] == "rooms":
            room_name = message.text
            room_desc = zone['rooms'][room_name]

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("⬅️ Назад"))

            bot.send_message(
                chat_id,
                f"🔍 *{room_name}*\n\n{room_desc}",
                parse_mode="Markdown",
                reply_markup=markup
            )
            user_tour_status[chat_id]["current_location"] = "room_detail"

        elif user_tour_status[chat_id]["current_location"] == "halls":
            hall_name = message.text
            hall = zone['halls'][hall_name]

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for exhibit in hall['exhibits']:
                markup.add(types.KeyboardButton(exhibit))
            markup.add(types.KeyboardButton("⬅️ Назад"))

            bot.send_message(
                chat_id,
                f"🏛️ *{hall_name}*\n\n{hall['description']}",
                parse_mode="Markdown",
                reply_markup=markup
            )
            user_tour_status[chat_id].update({
                "current_location": "hall_detail",
                "current_hall": hall_name
            })

    @bot.message_handler(func=lambda msg:
    user_tour_status.get(msg.chat.id) and
    msg.text in get_current_exhibits(msg.chat.id)
                         )
    def show_exhibit(message):
        chat_id = message.chat.id
        zone_name = user_tour_status[chat_id]["current_zone"]
        hall_name = user_tour_status[chat_id]["current_hall"]
        exhibit_name = message.text

        exhibit_desc = TOUR_DATA[zone_name]['halls'][hall_name]['exhibits'][exhibit_name]

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("⬅️ Назад"))

        bot.send_message(
            chat_id,
            f"🖼️ *{exhibit_name}*\n\n{exhibit_desc}",
            parse_mode="Markdown",
            reply_markup=markup
        )
        user_tour_status[chat_id]["current_location"] = "exhibit_detail"

    @bot.message_handler(func=lambda msg:
    user_tour_status.get(msg.chat.id) and
    msg.text == "⬅️ Назад"
                         )
    def handle_back(message):
        chat_id = message.chat.id
        current_location = user_tour_status[chat_id]["current_location"]

        if current_location == "room_detail":
            zone_name = user_tour_status[chat_id]["current_zone"]
            show_rooms_menu(chat_id, bot, TOUR_DATA[zone_name])
        elif current_location == "rooms":
            show_zones_menu(chat_id, bot)
        elif current_location == "hall_detail":
            zone_name = user_tour_status[chat_id]["current_zone"]
            show_halls_menu(chat_id, bot, TOUR_DATA[zone_name])
        elif current_location == "halls":
            show_zones_menu(chat_id, bot)
        elif current_location == "exhibit_detail":
            zone_name = user_tour_status[chat_id]["current_zone"]
            hall_name = user_tour_status[chat_id]["current_hall"]
            show_hall_details(chat_id, bot, TOUR_DATA[zone_name]['halls'][hall_name], hall_name)
        else:
            exit_tour(chat_id, bot)

    def show_hall_details(chat_id, bot, hall, hall_name):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for exhibit in hall['exhibits']:
            markup.add(types.KeyboardButton(exhibit))
        markup.add(types.KeyboardButton("⬅️ Назад"))

        bot.send_message(
            chat_id,
            f"🏛️ *{hall_name}*\n\n{hall['description']}",
            parse_mode="Markdown",
            reply_markup=markup
        )
        user_tour_status[chat_id]["current_location"] = "hall_detail"

    def exit_tour(chat_id, bot):
        user_tour_status.pop(chat_id)
        bot.send_message(
            chat_id,
            "Экскурсия завершена. Что вас интересует?",
            reply_markup=get_main_menu()
        )

    def get_current_rooms_or_halls(chat_id):
        zone_name = user_tour_status.get(chat_id, {}).get("current_zone")
        if not zone_name or zone_name not in TOUR_DATA:
            return []

        zone = TOUR_DATA[zone_name]
        if user_tour_status[chat_id]["current_location"] == "rooms":
            return list(zone.get('rooms', {}).keys())
        elif user_tour_status[chat_id]["current_location"] == "halls":
            return list(zone.get('halls', {}).keys())
        return []

    def get_current_exhibits(chat_id):
        zone_name = user_tour_status.get(chat_id, {}).get("current_zone")
        hall_name = user_tour_status.get(chat_id, {}).get("current_hall")

        if not zone_name or zone_name not in TOUR_DATA:
            return []
        if not hall_name or 'halls' not in TOUR_DATA[zone_name]:
            return []
        if hall_name not in TOUR_DATA[zone_name]['halls']:
            return []

        return list(TOUR_DATA[zone_name]['halls'][hall_name].get('exhibits', {}).keys())

    @bot.message_handler(func=lambda msg: user_tour_status.get(msg.chat.id))
    def handle_other_commands(message):
        bot.send_message(
            message.chat.id,
            "Используйте кнопки навигации или '⬅️ Назад'",
            reply_markup=get_back_button()
        )