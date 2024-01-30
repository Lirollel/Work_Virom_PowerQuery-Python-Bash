import telebot
import sqlite3

from bot_token import token

bot = telebot.TeleBot(token)

import markups as m

### Включение БД

conn = sqlite3.connect('c:\\Users\\q\\Projects\\Work_git\\Programms_and_macros\\Telefram-bot_sequensing\\db\\database', check_same_thread=False)
cursor = conn.cursor()

table_name = 'table_test'

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
result = cursor.fetchone()
if result is not None:
    print(f"The '{table_name}' table exists in the database.")
else:
    print(f"The '{table_name}' table does not exist in the database.")
	
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO table_test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()


### Прветствие и работа с сообщениями

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Добро пожаловать!\n\nЯ - бот, ведущищий записи о проектах по секвенированию')
	

	### Проверка на наличие в БД
	
	us_id = [int(message.from_user.id)]
	cursor.execute(f"SELECT user_id FROM '{table_name}' WHERE user_id = ?", (us_id))
	result = cursor.fetchone()
	
	if result is None:
		
		bot.send_message(message.chat.id, 'Напиши пожалуйста свое имя и фамилию ответным сообщением')
		
count_value = 1
if count_value == 1:
	@bot.message_handler(content_types=['text'])
	def get_name(message):

		bot.send_message(message.from_user.id, 'Ваше имя добавленно в базу данных')
		bot.send_message(message.chat.id, 'Выберите функцию из предложенных', reply_markup=m.first_markup)
		us_name = message.text
		username = message.from_user.username
		us_id = message.from_user.id

		db_table_val(user_id=us_id, user_name=us_name, username=username, user_surname='')
		count_value = 2	

@bot.message_handler(content_types=['text'])
def command_message(message):
	if message.text == 'Архив':
	    bot.send_message(message.chat.id, reply_markup=m.list_markup)
	
#Последний номер сиквенса
#Создать новые проект
#Список моих проектов
#Все проекты

### Чтобы бот работал постоянно 

bot.polling()