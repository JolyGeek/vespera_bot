import logging
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from openai_api import generate_text

# Включаем логирование для отладки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Инициализируем бота
bot = telegram.Bot(token='YOUR_TOKEN_HERE')

# Функция, которая будет вызываться при получении нового сообщения
def echo(update, context):
    # Получаем текст сообщения от пользователя
    user_input = update.message.text

    # Генерируем ответ на основе текста пользователя, используя мой API
    response = generate_text(user_input)

    # Отправляем сгенерированный ответ пользователю
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Инициализируем обновление сообщений
updater = Updater(token='YOUR_TOKEN_HERE', use_context=True)

# Получаем диспетчер сообщений
dispatcher = updater.dispatcher

# Регистрируем функцию echo как обработчик сообщений
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запускаем бота
updater.start_polling()

# Останавливаем бота при нажатии Ctrl+C
updater.idle()
```

Не забудьте установить библиотеку python-telegram-bot перед запуском этого кода, используя команду `pip install python-telegram-bot`.
