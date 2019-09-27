import config
import telebot
import requests
from datetime import datetime
from time import sleep

# telebot.apihelper.proxy = {'https': 'socks5://171.103.9.22:4145/'}

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}


bot = telebot.TeleBot(config.token)

n = 28


@bot.message_handler(commands=['start', 'help', 'bell', 'week', 'tomorrow'])
def command_handler(message):
    if 'start' in message.text:
        bot.send_message(message.chat.id, text='Привет, Я Бот, который тебе будем помогать в учебе.')
    elif 'help' in message.text:
        bot.send_message(message.chat.id, text='Давай я помогу тебе настроить меня.')
    elif 'week' in message.text:  # расписание на неделю
        for i in range(1, len(config.shedule)+1):
            bot.send_message(message.chat.id, text=config.shedule[str(i)])
    elif 'tomorrow' in message.text:  # расписание на следующий учебный день
        if (int(datetime.now().strftime("%w"))+1) % 7 != 0:
            bot.send_message(message.chat.id, text=config.shedule[str((int(datetime.now().strftime("%w"))+1) % 7)])
        else:
            bot.send_message(message.chat.id, text=config.shedule['1'])
    elif 'bell' in message.text:  # расписание звонков
        bot.send_message(message.chat.id, text='Расписание звонков.\n'
                                               'Первая пара: ' + config.bells['first'] + '.\n'
                                               'Вторая пара: ' + config.bells['second'] + '.\n'
                                               'Третья пара: ' + config.bells['third'] + '.\n'
                                               'Четвертая пара: ' + config.bells['fourth'] + '.\n'
                                               'Пятая пара: ' + config.bells['fifth'] + '.\n')




# @bot.message_handler(content_types=["text"])
# def calendar(message):
#     while True:
#         if int(datetime.now().strftime("%w")) != 7:
#             if int(datetime.now().strftime("%H")) == 14 and int(datetime.now().strftime("%M")) == n:
#                 bot.send_message(message.chat.id, text=config.shedule[datetime.now().strftime("%w")])
#                 sleep(60 - n)
#         else:
#             bot.send_message(message.chat.id, text="Сегодня выходной")

if __name__ == '__main__':
    bot.polling(none_stop=True)
