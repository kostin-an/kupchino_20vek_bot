import telebot

bot = telebot.TeleBot('1665765568:AAFMCQmN5SRkIUE7-HFuvrIMKrxIMIWU2zI')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Первый', 'Второй', 'Третий')
keyboard1.row('Четвертый', 'Пятый', 'Шестой')
keyboard1.row('Седьмой')
keyboard1.row('Отправить свою историю или отзыв')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id, text='Выберите интересующий экспонат:', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def message_input(message):
    chat_id = message.chat.id
    if message.text == 'Первый':
        audio = open('sound/audio_1.ogg', 'rb')
        bot.send_audio(chat_id, audio)
    elif message.text == 'Второй':
        audio = open('sound/audio_1.ogg', 'rb')
        bot.send_audio(chat_id, audio)
    elif message.text == 'Третий':
        audio = open('sound/audio_1.ogg', 'rb')
        bot.send_audio(chat_id, audio)
    elif message.text == 'Четвертый':
        audio = open('sound/audio_1.ogg', 'rb')
        bot.send_audio(chat_id, audio)
    elif message.text == 'Пятый':
        audio = open('sound/audio_1.ogg', 'rb')
        bot.send_audio(chat_id, audio)
    elif message.text == 'Шестой':
        audio = open('sound/audio_1.ogg', 'rb')
        bot.send_audio(chat_id, audio)
    elif message.text == 'Седьмой':
        audio = open('sound/audio_1.ogg', 'rb')
        bot.send_audio(chat_id, audio)
    elif message.text == 'Отправить свою историю или отзыв':
        bot.send_message(message.from_user.id, text='Просто отправьте здесь свое аудиосообщение')
    else:
        bot.send_message(message.from_user.id, text='Бот не работает с текстовыми сообщениями, выберите интересующий экспонат')

@bot.message_handler(content_types=['voice'])
def handle_docs_audio(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f'input_sound/{message.from_user.first_name}_{message.from_user.last_name}_@{message.from_user.username}_{message.voice.file_id}.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
        bot.send_message(message.from_user.id, 'Спасибо, сообщение принято')


bot.polling(none_stop=True)
