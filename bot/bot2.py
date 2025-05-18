import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Настройка логгирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


load_dotenv()  # Загружает переменные из .env
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Главное меню
main_menu_buttons = [
    [KeyboardButton('Создать дизайн')],
    [KeyboardButton('Пройти тест "Кто ты из продукции Неман"')],
    [KeyboardButton('Интерактивный гид по заводу и музею')],
    [KeyboardButton('Связаться с менеджером')],
]
main_menu_markup = ReplyKeyboardMarkup(main_menu_buttons, resize_keyboard=True)

# Вопросы для теста
QUIZ_QUESTIONS = [
    {
        'question': '1. Ваш любимый цвет?',
        'options': ['🔵 Синий', '🟢 Зеленый', '🔴 Красный', '⚪ Прозрачный']
    },
    {
        'question': '2. Какой стиль вам ближе?',
        'options': ['🏛 Классика', '🪩 Модерн', '🎭 Авангард', '🌿 Натуральный']
    },
    {
        'question': '3. Ваш идеальный вечер?',
        'options': ['🍷 Ужин при свечах', '🎨 Творческая мастерская', '🏕️ Пикник на природе', '🎪 Вечеринка с друзьями']
    },
    {
        'question': '4. Какой предмет вам нужен?',
        'options': ['🥂 Для праздника', '🖼️ Для украшения дома', '🎁 Для подарка', '💎 Для коллекции']
    },
    {
        'question': '5. Ваш девиз?',
        'options': ['«Красота в деталях»', '«Смелость — моя философия»', '«Традиции — это вечно»',
                    '«Главное — практичность»']
    },
    {
        'question': '6. Любимый материал?',
        'options': ['💎 Хрусталь', '🪔 Матовое стекло', '🎨 Цветное стекло', '✨ Граненое стекло']
    },
    {
        'question': '7. Ваша суперсила?',
        'options': ['🕊️ Умение вдохновлять', '🏹 Решительность', '🧿 Творческая энергия', '🛡️ Надежность']
    }
]

# Результаты теста
QUIZ_RESULTS = {
    'Бокал "France"': {
        'description': 'Вы — бокал "France"! 🍷 Элегантный хрустальный бокал с тонкой гравировкой. Символ утонченности и французского шика. Ваш стиль — изысканность и традиции.',
        'image': 'https://example.com/france.jpg'
    },
    'Декоративная ваза "Охота на утку"': {
        'description': 'Вы — ваза "Охота на утку"! 🦆 Ваза с ручной росписью в охотничьем стиле. Ваша жизнь — это движение, а ваш дом — галерея впечатлений.',
        'image': 'https://example.com/hunting_vase.jpg'
    },
    'Декоративное изделие "Дракон"': {
        'description': 'Вы — "Дракон"! 🐉 Стеклянная скульптура мифического дракона. Ваша харизма завораживает, а вкус ломает стереотипы.',
        'image': 'https://example.com/dragon.jpg'
    },
    'Декоративное изделие "Мешочек"': {
        'description': 'Вы — "Мешочек"! 🛍️ Миниатюрный стеклянный мешочек с позолотой. Вы умеете хранить самое ценное и создавать гармонию вокруг.',
        'image': 'https://example.com/pouch.jpg'
    },
    'Шкатулка "Яйцо"': {
        'description': 'Вы — шкатулка "Яйцо"! 🥚 Хрустальное яйцо с секретным отделением. В вас сочетаются тайна и совершенство форм.',
        'image': 'https://example.com/egg.jpg'
    },
    'Менажница "Трио"': {
        'description': 'Вы — менажница "Трио"! 🍽️ Практичный набор из трех разноцветных менажниц. Вы объединяете людей и любите эксперименты.',
        'image': 'https://example.com/trio.jpg'
    },
    'Прибор "Респект"': {
        'description': 'Вы — прибор "Респект"! 🥃 Строгий набор для напитков из матового стекла. Ваш стиль — это уверенность и безупречный вкус.',
        'image': 'https://example.com/respect.jpg'
    }
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Здравствуйте! Добро пожаловать в чатбот стеклозавода «Неман».\n\n"
        "Я помогу вам:\n"
        "- Создать собственный дизайн стеклянного изделия\n"
        "- Пройти тест «Кто ты из продукции Неман»\n"
        "- Познакомиться с интерактивным гидом по заводу и музею\n"
        "- Связаться с нашим менеджером\n\n"
        "Пожалуйста, выберите действие из меню ниже."
    )
    await update.message.reply_text(welcome_text, reply_markup=main_menu_markup)


# Сценарий создания дизайна
async def start_design(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎨 Давайте создадим ваш дизайн! Выберите тип изделия:",
        reply_markup=ReplyKeyboardMarkup([
            ["Бокал", "Ваза", "Стакан"],
            ["В главное меню"]
        ], resize_keyboard=True)
    )
    context.user_data["design_stage"] = "type"


async def handle_design(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stage = context.user_data.get("design_stage")
    text = update.message.text

    if text == "В главное меню":
        await update.message.reply_text("Возвращаемся в главное меню.", reply_markup=main_menu_markup)
        context.user_data.clear()
        return

    if stage == "type":
        context.user_data["design_type"] = text
        await update.message.reply_text(
            "🌈 Теперь выберите цвет стекла:",
            reply_markup=ReplyKeyboardMarkup([
                ["Прозрачный", "Синий", "Зеленый", "Розовый"],
                ["В главное меню"]
            ], resize_keyboard=True)
        )
        context.user_data["design_stage"] = "color"

    elif stage == "color":
        context.user_data["design_color"] = text
        await update.message.reply_text(
            "✨ Добавьте узор (или пропустите):",
            reply_markup=ReplyKeyboardMarkup([
                ["Геометрический", "Цветочный", "Без узора"],
                ["В главное меню"]
            ], resize_keyboard=True)
        )
        context.user_data["design_stage"] = "pattern"

    elif stage == "pattern":
        context.user_data["design_pattern"] = text
        await update.message.reply_text(
            f"✅ Ваш дизайн готов!\n\n"
            f"Тип: {context.user_data['design_type']}\n"
            f"Цвет: {context.user_data['design_color']}\n"
            f"Узор: {context.user_data['design_pattern']}\n\n"
            f"Мы сохранили ваш запрос. Менеджер свяжется для уточнения деталей!",
            reply_markup=main_menu_markup
        )
        context.user_data.clear()


# Сценарий теста
async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["quiz_answers"] = []
    context.user_data["current_question"] = 0
    await ask_question(update, context)


async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current = context.user_data["current_question"]
    if current < len(QUIZ_QUESTIONS):
        question = QUIZ_QUESTIONS[current]
        options = question['options'] + ["В главное меню"]

        await update.message.reply_text(
            question['question'],
            reply_markup=ReplyKeyboardMarkup(
                [options[i:i + 2] for i in range(0, len(options), 2)],
                resize_keyboard=True
            )
        )
    else:
        await finish_quiz(update, context)


async def handle_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "В главное меню":
        await update.message.reply_text("Тест прерван. Возвращаемся в главное меню.", reply_markup=main_menu_markup)
        context.user_data.clear()
        return

    context.user_data["quiz_answers"].append(text)
    context.user_data["current_question"] += 1
    await ask_question(update, context)


async def finish_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Простая логика определения результата (можно усложнить)
    answers = context.user_data["quiz_answers"]
    result_key = list(QUIZ_RESULTS.keys())[hash(tuple(answers)) % len(QUIZ_RESULTS)]
    result = QUIZ_RESULTS[result_key]

    await update.message.reply_text(
        result['description'],
        reply_markup=main_menu_markup
    )
    # Здесь можно добавить отправку фото
    # await update.message.reply_photo(photo=result['image'])
    context.user_data.clear()


# Сценарий интерактивного гида
async def send_tour(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏭 Добро пожаловать в интерактивный тур по заводу Неман!",
        reply_markup=ReplyKeyboardMarkup([
            ["История завода", "Технологии производства"],
            ["Музей стекла", "В главное меню"]
        ], resize_keyboard=True)
    )


async def handle_tour(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "В главное меню":
        await update.message.reply_text("Возвращаемся в главное меню.", reply_markup=main_menu_markup)
        return

    responses = {
        "История завода": "📜 Завод Неман основан в 1883 году...",
        "Технологии производства": "🔧 У нас используются уникальные технологии...",
        "Музей стекла": "🖼️ В нашем музее собрано более 5000 экспонатов..."
    }

    await update.message.reply_text(
        responses.get(text, "Выберите раздел из меню."),
        reply_markup=ReplyKeyboardMarkup([
            ["История завода", "Технологии производства"],
            ["Музей стекла", "В главное меню"]
        ], resize_keyboard=True)
    )


# Сценарий связи с менеджером
async def request_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Оставьте ваш номер телефона или нажмите кнопку ниже:",
        reply_markup=ReplyKeyboardMarkup([
            [KeyboardButton("Отправить номер", request_contact=True)],
            ["В главное меню"]
        ], resize_keyboard=True)
    )


async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    await update.message.reply_text(
        f"Спасибо, {contact.first_name}! Менеджер свяжется с вами в течение часа.",
        reply_markup=main_menu_markup
    )


# Главный обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'Создать дизайн':
        await start_design(update, context)
    elif text == 'Пройти тест "Кто ты из продукции Неман"':
        await start_quiz(update, context)
    elif text == 'Интерактивный гид по заводу и музею':
        await send_tour(update, context)
    elif text == 'Связаться с менеджером':
        await request_contact(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите действие из меню.", reply_markup=main_menu_markup)


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))

    application.run_polling()


if __name__ == '__main__':
    main()