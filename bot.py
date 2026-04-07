import telebot
import random

    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8403897766:AAFzo-nftEUoJI5nS7G8Fph0e1_Yj_b9MtI")
    
@bot.message_handler(commands=['S'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
   bot.reply_to(message, "Пока! Удачи!")
    
    
@bot.message_handler(commands=['Choice'])
def echo_all(message):
    bot.reply_to(message, random.choice("Yes"))
    
    # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "English Article Test")
    answer_options = ["a", "an", "the", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="We are going to '' park.",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )


@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass
    
bot.polling()