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
            "🔨 Формовка": {
                "description": "Ручная выдувка стекла. Познакомьтесь с первым этапом создания стеклянных изделий - формовкой. Здесь вы узнаете, как из раскалённой стекломассы под руками мастера рождаются будущие вазы, графины и бокалы. Этот процесс требует особого мастерства, точности и творческого подхода.\n\n 💡 За смену мастера создают несколько видов изделий, каждый из которых требует точного расчёта количества стекломассы и идеальной техники. После формовки изделия отправляются в печь для отжига, где медленно остывают и приобретают прочность.",
                "photo": "forming.jpg"
            },
            "🎨 Декорирование": {
                "description": "Ручная роспись. В этом разделе вы увидите, как мастера превращают обычные заготовки в настоящие произведения искусства с помощью гравировки, росписи и других техник. Каждый штрих и узор - это результат кропотливой работы и вдохновения художников.\n\n✂️ Резчики и шлифовальщики используют алмазные инструменты и сложные техники гравировки, чтобы создать изысканный декор. Например, нанесение узора на небольшое пасхальное яйцо занимает всего несколько минут, однако требует большого опыта и внимания к деталям.\n\n✨ После декорирования изделия полируют в специальных кислотных смесях, что придаёт им характерный блеск и прозрачность - именно так рождается настоящее произведение искусства.",
                "photo": "decorating.jpg"
            },
            "🔥 Печи": {
                "description": "12 промышленных печей. Загляните в самое сердце стеклозавода - горячие печи, где рождается стекло. Здесь вы узнаете, как поддерживается нужная температура, как плавится стекломасса и как важно соблюдать технологические тонкости для получения идеального материала.\n\n ⏳ После формовки изделия попадают в печь для отжига (называемую лере), где проводят от полутора до двух часов. Медленное охлаждение предотвращает внутренние напряжения и трещины, обеспечивая прочность и долговечность изделий.\n\n💪 Работа с печами требует особых знаний и точности - от правильного поддержания температуры зависит качество всего выпускаемого стекла.",
                "photo": "furnaces.jpg"
            }
        }
    },
    "🏛️ Музей": {
        "description":(
            "🎨 *Добро пожаловать в музей стеклозавода «Неман»* - уникальное пространство, где собраны экспонаты, датируемые 1910 годом, "
            "а также авторские композиции современных художников и ветеранов предприятия.\n\n"
            "Здесь вы познакомитесь с богатой историей стеклоделия, увидите фирменное молочно-дымчатое стекло с тончайшей «неманской нитью», "
            "благородный хрусталь и множество изделий, отмеченных премиями и дипломами международных выставок. 🏆\n\n"
            "Во время экскурсии вы увидите полный цикл производства стекла - от раскалённой массы до изящных изделий, созданных вручную мастерами. "
            "Этот процесс завораживает и оставляет неизгладимое впечатление! 🔥\n\n"
            "Музей открыт для всех посетителей, а экскурсии проводятся с опытным гидом, который расскажет о каждом экспонате и ответит на ваши вопросы. "
            "После посещения музея вы сможете приобрести уникальные изделия в фирменном магазине - настоящем музее-магазине с лучшими работами завода. 🎁"
        ),
        "photo": "museum.jpg",
        "halls": {
            "🕰️ Исторический зал": {
                "description": ("🕰 *Экспонаты XIX-XX веков* - погрузитесь в атмосферу ушедших эпох и откройте для себя уникальные изделия, созданные мастерами «Немана» более века назад.\n\n"
            "Здесь представлены редкие образцы стеклянных изделий, отражающие богатую историю и художественные традиции завода, основанного в 1883 году. "
            "Вы увидите, как менялись стили и технологии, от первых форм модерна до изящных классических решений начала XX века.\n\n"
            "В музее собраны изделия, которые когда-то украшали дома и дворцы, а также служили важными элементами быта и культуры."
        ),
                "photo": "historical_hall.jpg",
                "exhibits": {
                    "🍷 Ваза 'Рубин' (1890)": {
                        "description":  (
                    "✨ *Первая продукция завода.* Один из старейших экспонатов музея, созданный в конце XIX века. "
                    "Эта ваза поражает насыщенным рубиновым цветом и изящной формой, символизируя мастерство первых стеклодувов «Немана»."
                ),
                        "photo": "ruby_vase.jpg"
                    },
                    "🏺 Графин 'Неман' (1925)": {
                        "description": (
                    "🎩 *Классика стиля.* Исторический графин, выполненный в лаконичном стиле 1920-х годов. "
                    "Его строгие линии и утончённый декор отражают дух эпохи межвоенного периода и высокое качество производства."
                ),
                        "photo": "neman_decanter.jpg"
                    }
                }
            },
            "✨ Современный зал": {
                "description": (
            "👋 *Добро пожаловать в современный зал*, где традиции стеклоделия встречаются с *инновациями* и *авторским творчеством*! ✨\n\n"
            "Здесь собраны лучшие работы последних лет - уникальные изделия, созданные мастерами завода «Неман» с использованием новейших технологий и смелых художественных идей.\n\n"
            "Вы увидите не просто предметы, а настоящие *произведения искусства*, отражающие дух времени и стремление к совершенству. "
            "Каждая работа - результат экспериментов с формой, светом и фактурой, воплощение креативности и мастерства. 🎨"
            ),
                "photo": "modern_hall.jpg",
                "exhibits": {
                    "💎 Скульптура 'Лед'": {
                        "description": (
                    "❄️ *Погрузитесь в мир чистоты и прозрачности!* Эта изысканная скульптура, созданная в 2020 году, поражает своим *кристальным блеском* и утончёнными линиями. "
                    "Она словно запечатлела мгновение зимней свежести, передавая хрупкость и красоту льда в каждом изгибе."
                ),
                        "photo": "ice_sculpture.jpg"
                    },
                    "🌌 Композиция 'Галактика'": {
                        "description": (
                    "🚀 *Откройте для себя космическое вдохновение!* Оригинальная композиция, навеянная загадками Вселенной, выполнена с применением инновационных технологий и авторских приёмов. "
                    "Внутри стеклянной сферы словно застыли звёзды и туманности, создавая ощущение бесконечности и тайны космоса."
                ),
                        "photo": "galaxy_composition.jpg"
                    }
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
        markup = create_markup(list(TOUR_DATA.keys()))
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

    @bot.message_handler(func=lambda msg: user_tour_status.get(msg.chat.id) and msg.text in TOUR_DATA)
    def show_zone(message):
        chat_id = message.chat.id
        zone_name = message.text
        zone = TOUR_DATA[zone_name]  # Получаем данные зоны

        user_tour_status[chat_id] = {
            "current_location": "zone",
            "current_zone": zone_name,
            "current_hall": None
        }
        #zone = TOUR_DATA[zone_name]

        # Специальная обработка для главного цеха
        if zone_name == "🏭 Главный цех":
            send_workshop_messages(chat_id, bot,zone)
        else:
            send_zone_info(chat_id, bot, zone_name, zone)
            show_zone_submenu(chat_id, bot, zone)



    def send_zone_info(chat_id, bot, zone_name, zone):
        """Отправка информации о зоне (кроме главного цеха)"""
        send_message_with_photo(
            bot, chat_id,
            caption=f"{zone_name}\n\n{zone['description']}",
            photo_path=zone['photo']
        )


    def send_workshop_messages(chat_id, bot, zone):
        """Последовательная отправка сообщений о главном цехе"""

        if chat_id not in user_tour_status:
            user_tour_status[chat_id] = {
                "current_location": "main",
                "current_zone": None,
                "current_hall": None
            }
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

            # После всех сообщений показываем меню подразделов
        show_zone_submenu(chat_id, bot, zone)

    def show_zone_submenu(chat_id, bot, zone):
        """Показывает меню подразделов зоны (комнаты или залы)"""
        if chat_id not in user_tour_status:
            user_tour_status[chat_id] = {
                "current_location": "main",
                "current_zone": None,
                "current_hall": None
            }

        if 'rooms' in zone:
            show_rooms_menu(chat_id, bot, zone)
        elif 'halls' in zone:
            show_halls_menu(chat_id, bot, zone)
    def show_rooms_menu(chat_id, bot, zone):
        # Проверяем, есть ли запись о пользователе в словаре состояний
        if chat_id not in user_tour_status:
            user_tour_status[chat_id] = {
                "current_location": "main",
                "current_zone": None,
                "current_hall": None
            }

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
        markup = create_markup(list(zone['halls'].keys()))
        bot.send_message(chat_id, "Выберите зал музея:", reply_markup=markup)
        user_tour_status[chat_id]["current_location"] = "halls"

    @bot.message_handler(
        func=lambda msg: user_tour_status.get(msg.chat.id) and msg.text in get_current_rooms_or_halls(msg.chat.id))
    def show_room_or_hall(message):
        chat_id = message.chat.id
        zone_name = user_tour_status[chat_id]["current_zone"]
        zone = TOUR_DATA[zone_name]

        if user_tour_status[chat_id]["current_location"] == "rooms":
            show_room_detail(chat_id, bot, zone['rooms'][message.text], message.text)
        elif user_tour_status[chat_id]["current_location"] == "halls":
            show_hall_detail(chat_id, bot, zone['halls'][message.text], message.text)

    def show_room_detail(chat_id, bot, room_data, room_name):
        send_message_with_photo(
            bot, chat_id,
            caption=f"🔍 *{room_name}*\n\n{room_data['description']}",
            photo_path=room_data['photo'],
            parse_mode="Markdown",
            markup=create_markup(["⬅️ Назад"])
        )
        user_tour_status[chat_id]["current_location"] = "room_detail"

    def show_hall_detail(chat_id, bot, hall, hall_name):
        send_message_with_photo(
            bot, chat_id,
            caption=f"🏛️ *{hall_name}*\n\n{hall['description']}",
            photo_path=hall['photo'],
            parse_mode="Markdown"
        )

        markup = create_markup(list(hall['exhibits'].keys()) + ["⬅️ Назад"])
        bot.send_message(chat_id, "Выберите экспонат:", reply_markup=markup)

        user_tour_status[chat_id].update({
            "current_location": "hall_detail",
            "current_hall": hall_name
        })

    @bot.message_handler(
        func=lambda msg: user_tour_status.get(msg.chat.id) and msg.text in get_current_exhibits(msg.chat.id))
    def show_exhibit(message):
        chat_id = message.chat.id
        zone_name = user_tour_status[chat_id]["current_zone"]
        hall_name = user_tour_status[chat_id]["current_hall"]
        exhibit_name = message.text

        exhibit_data = TOUR_DATA[zone_name]['halls'][hall_name]['exhibits'][exhibit_name]

        send_message_with_photo(
            bot, chat_id,
            caption=f"🖼️ *{exhibit_name}*\n\n{exhibit_data['description']}",
            photo_path=exhibit_data['photo'],
            parse_mode="Markdown",
            markup=create_markup(["⬅️ Назад"])
        )
        user_tour_status[chat_id]["current_location"] = "exhibit_detail"

    @bot.message_handler(func=lambda msg: user_tour_status.get(msg.chat.id) and msg.text == "⬅️ Назад")
    def handle_back(message):
        chat_id = message.chat.id
        current_location = user_tour_status[chat_id]["current_location"]
        zone_name = user_tour_status[chat_id]["current_zone"]
        zone = TOUR_DATA[zone_name]

        navigation_map = {
            "room_detail": lambda: show_rooms_menu(chat_id, bot, zone),
            "rooms": lambda: show_zones_menu(chat_id, bot),
            "hall_detail": lambda: show_halls_menu(chat_id, bot, zone),
            "halls": lambda: show_zones_menu(chat_id, bot),
            "exhibit_detail": lambda: show_hall_detail(
                chat_id, bot,
                zone['halls'][user_tour_status[chat_id]["current_hall"]],
                user_tour_status[chat_id]["current_hall"]
            ),
        }

        if current_location in navigation_map:
            navigation_map[current_location]()
        else:
            exit_tour(chat_id, bot)

    def exit_tour(chat_id, bot):
        user_tour_status.pop(chat_id, None)
        bot.send_message(
            chat_id,
            "Экскурсия завершена. Что вас интересует?",
            reply_markup=get_main_menu()
        )

    # Вспомогательные функции
    def create_markup(buttons):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for button in buttons:
            markup.add(types.KeyboardButton(button))
        if "⬅️ Назад" not in buttons:
            markup.add(types.KeyboardButton("⬅️ Назад"))
        return markup

    def send_message_with_photo(bot, chat_id, caption, photo_path=None, parse_mode=None, markup=None):
        """Универсальная функция для отправки сообщений с фото или без"""
        try:
            if photo_path:
                full_path = os.path.join(TOUR_IMAGES_DIR, photo_path)
                with open(full_path, 'rb') as photo_file:
                    bot.send_photo(
                        chat_id,
                        photo_file,
                        caption=caption,
                        parse_mode=parse_mode,
                        reply_markup=markup
                    )
            else:
                bot.send_message(
                    chat_id,
                    caption,
                    parse_mode=parse_mode,
                    reply_markup=markup
                )
        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")
            bot.send_message(
                chat_id,
                caption,
                parse_mode=parse_mode,
                reply_markup=markup
            )

    def get_current_rooms_or_halls(chat_id):
        """Возвращает список доступных комнат или залов для текущей зоны"""
        zone_name = user_tour_status.get(chat_id, {}).get("current_zone")
        if not zone_name or zone_name not in TOUR_DATA:
            return []

        zone = TOUR_DATA[zone_name]
        location = user_tour_status[chat_id]["current_location"]

        if location == "rooms":
            return list(zone.get('rooms', {}).keys())
        elif location == "halls":
            return list(zone.get('halls', {}).keys())
        return []

    def get_current_exhibits(chat_id):
        """Возвращает список экспонатов для текущего зала"""
        zone_name = user_tour_status.get(chat_id, {}).get("current_zone")
        hall_name = user_tour_status.get(chat_id, {}).get("current_hall")

        if not all([zone_name, hall_name]):
            return []

        return list(TOUR_DATA.get(zone_name, {}).get('halls', {}).get(hall_name, {}).get('exhibits', {}).keys())

    @bot.message_handler(func=lambda msg: user_tour_status.get(msg.chat.id))
    def handle_other_commands(message):
        bot.send_message(
            message.chat.id,
            "Используйте кнопки навигации или '⬅️ Назад'",
            reply_markup=get_back_button()
        )