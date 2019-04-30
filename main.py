# -*- coding: utf-8 -*-
import telebot
import random

cities = ["moscow.jpg", "nursultan.jpg", "london.jpg", "pekin.jpg", "berlin.jpg", "monaco.jpg", "paris.jpg", "san-francisco.jpg", "nursultan2.jpg"]
names = ["Москва", "Нурсултан", "Лондон", "Пекин", "Берлин", "Монако", "Париж", "Сан-Франциско", "Нурсултан"]
username = ""
asking_for_name = False
y = 0

score = 0
d = {"moscow.jpg": "Москва",
     "nursultan.jpg": "Нурсултан",
     "london.jpg": "Лондон",
     "pekin.jpg": "Пекин",
     "berlin.jpg": "Берлин",
     "monaco.jpg": "Монако",
     "paris.jpg": "Париж",
     "san-francisco.jpg": "Сан-Франциско",
     "nursultan2.jpg": "Нурсултан"
     }

l = {"Москва": "moscow.jpg",
     "Нурсултан": "nursultan.jpg",
     "Лондон": "london.jpg",
     "Пекин": "pekin.jpg",
     "Берлин": "berlin.jpg",
     "Монако": "monaco.jpg",
     "Париж": "paris.jpg",
     "Сан-Франциско": "san-francisco.jpg"
     }

running = False
showing = False
answer = ""
bot = telebot.TeleBot('826527038:AAHKyzEnrQd40qgrPxdjeuk1xTubZ03nt_g');

@bot.message_handler(commands=['age'])
def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    global username, asking_for_name
    if not username:
        bot.send_message(message.from_user.id, "Можете представиться? Я с незнакомцами не общаюсь.")
        tmp = "Как вас зовут?"
        bot.send_message(message.from_user.id, tmp)
        asking_for_name = True
        return
    bot.send_message(message.from_user.id, "Доступные команды:\n/help - помощь\n/start - начать игру\n/stop - закончить игру\n/show - показать города\n")

@bot.message_handler(commands=['start'])
def start(message):
    global username, asking_for_name, showing
    showing = False
    if not username:
        bot.send_message(message.from_user.id, "Можете представиться? Я с незнакомцами не общаюсь.")
        tmp = "Как вас зовут?"
        bot.send_message(message.from_user.id, tmp)
        asking_for_name = True
        return
    global running, cities, answer, y
    running = True
    bot.send_message(message.from_user.id, "Я показываю вам фотографию, вы должны назвать город. Поехали!")
    bot.send_photo(message.from_user.id, open(cities[y], 'rb'))
    answer = d[cities[y]]
    if y < len(cities) - 1:
        y += 1
    else:
        y = 0    
    
@bot.message_handler(commands=['stop'])
def stop(message):
    global username, asking_for_name
    if not username:
        bot.send_message(message.from_user.id, "Можете представиться? Я с незнакомцами не общаюсь.")
        tmp = "Как вас зовут?"
        bot.send_message(message.from_user.id, tmp)
        asking_for_name = True
        return
    global running, score, showing
    tmp = username + ", пожалуйста, не спамьте командой /stop"
    if running:
        tmp = "Игра закончена. Вы смогли набрать " + str(score) + " очков!"
    running = False
    if showing:
        tmp = "Кажется, вы узнали все что вам нужно."
    showing = False
    bot.send_message(message.from_user.id, tmp)

@bot.message_handler(commands=['show'])
def show(message):
    global username, asking_for_name, running
    running = False
    if not username:
        bot.send_message(message.from_user.id, "Можете представиться? Я с незнакомцами не общаюсь.")
        tmp = "Как вас зовут?"
        bot.send_message(message.from_user.id, tmp)
        asking_for_name = True
        return
    global showing
    tmp = "Назовите город, и я покажу вам, как он выглядит!"
    bot.send_message(message.from_user.id, tmp)
    showing = True

@bot.message_handler(func=lambda x: True)
def get_text_messages(message):
    global running, cities, answer, showing, username, asking_for_name, score, y
    if not username and not asking_for_name:
        tmp = "Как вас зовут?"
        bot.send_message(message.from_user.id, tmp)
        asking_for_name = True
        return
    elif not username:
        username = message.text
        tmp = "Приятно познакомиться, " + username + ". Я бот, с которым ты можешь поиграть в 'Города'!"
        bot.send_message(message.from_user.id, tmp)
        asking_for_name = False
    elif not running and not showing:
        bot.send_message(message.from_user.id, "Не знаю такой команды!")
    elif running:
        if message.text == answer:
            score += 1
            tmp = "Верно! " + username + ", вы ответили правильно уже на " + str(score) + " вопросов!"
            bot.send_message(message.from_user.id, tmp)
        else:
            tmp = 'Неверно! Ответ: ' + answer
            bot.send_message(message.from_user.id, tmp)
        if y < len(cities) - 1:
            y += 1
        else:
            y = 0
        bot.send_photo(message.from_user.id, open(cities[y], 'rb'))
        answer = d[cities[y]]        
    elif showing:
        if message.text in names:
            bot.send_photo(message.from_user.id, open(l[message.text], 'rb'))
        else:
            tmp = "Такого города я не знаю :(\n" + "Возможно вы хотите сыграть со мной в игру, " + username + "?"
            bot.send_message(message.from_user.id, tmp)
        
bot.polling(none_stop=True, interval=0)