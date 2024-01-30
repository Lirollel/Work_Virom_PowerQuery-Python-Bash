import telebot
import sqlite3

from bot_token import token

bot = telebot.TeleBot(token)

import markups as m

### Включение БД

conn = sqlite3.connect('c:\\Users\\q\\Projects\\Work_git\\Programms_and_macros\\Telefram-bot_sequensing\\db\\database', check_same_thread=False)
cursor = conn.cursor()

table_name = 'names_list'

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
result = cursor.fetchone()
if result is not None:
    print(f"The '{table_name}' table exists in the database.")
else:
    print(f"The '{table_name}' table does not exist in the database.")
	
def db_names_list_val(user_id: int, user_name: str, username: str):
	cursor.execute('INSERT INTO names_list (user_id, user_name, username) VALUES (?, ?, ?)', (user_id, user_name, username))
	conn.commit()

def db_projects_list_val(user_id: int, project_name: str, start_sample: int, end_sample: int):
	cursor.execute('INSERT INTO projects_list  (user_id, project_name, start_sample, end_sample) VALUES (?, ?, ?, ?)', (user_id, project_name, start_sample, end_sample))
	conn.commit()

cursor.execute("SELECT MAX(end_sample) FROM projects_list")
inf_start_sample = cursor.fetchone()[0]
print(f"The start sample is: '{inf_start_sample}'")


### Прветствие и работа с сообщениями

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Добро пожаловать!\n\nЕсли Вы запускаете проект по секвенированию, я Вам в этом помогу - подскажу какие номера проб сейчас свободны, а еще создам для Вас список Ваших проектов')

	user_id = message.from_user.id
	cursor.execute(f"SELECT user_id FROM names_list WHERE user_id = ?", (user_id,))
	result = cursor.fetchone()
		
	if result is None:
		bot.send_message(message.chat.id, 'Напишите пожалуйста свое <b>ИМЯ</b> и <b>ФАМИЛИЮ</b>', parse_mode="HTML")
		bot.register_next_step_handler(message, get_name)
	else:
		bot.send_message(message.chat.id, 'Выберите функцию из списка', reply_markup=m.first_markup)
		bot.register_next_step_handler(message, text_command)

### Команда список проектов

@bot.message_handler(content_types=['text'])
def text_command(message):

	if message.text == m.first_btn1:
		bot.send_message(message.chat.id, 'Введите <b>НАЗВАНИЕ ПРОЕКТА</b> и <b>КОЛ-ВО ПРОБ</b> через запятую', parse_mode="HTML")
		bot.register_next_step_handler(message, get_project)
	
	if message.text == m.first_btn2:
		user_id = [int(message.from_user.id)]
		cursor.execute("SELECT project_name, start_sample,end_sample FROM projects_list WHERE user_id = ?", 
		(user_id))
		data = cursor.fetchall()
		for row in data:
			bot.send_message(message.chat.id, f'"{row[0]}": {row[1]} - {row[2]}')
	
	if message.text == m.first_btn3:
		cursor.execute("SELECT names_list.user_name, projects_list.project_name, projects_list.start_sample, projects_list.end_sample FROM projects_list JOIN names_list ON names_list.user_id = projects_list.user_id")
		data = cursor.fetchall()
		for row in data:
			bot.send_message(message.chat.id, f'{row[0]} "{row[1]}": {row[2]} - {row[3]}')
		
		
### Спрашиваем имя
	
@bot.message_handler(content_types=['text'])
def get_name(message):
	
	cursor.execute(f"SELECT user_id FROM names_list")
	result = cursor.fetchone()
	if result is None:
		bot.send_message(message.from_user.id, 'Спасибо! Приятно познакомиться :)')
		bot.send_message(message.chat.id, 'Теперь Вы можете выбрать любую функцию из списка', reply_markup=m.first_markup)
		user_name = message.text
		username = message.from_user.username
		user_id = message.from_user.id
		
		db_names_list_val(user_id, user_name, username)
	
	else:
		bot.send_message(message.from_user.id, 'Ваше имя уже есть в спике')
		bot.send_message(message.chat.id, 'Выберите функцию из предложенных', reply_markup=m.first_markup)

	bot.register_next_step_handler(message, text_command)

### Данные проекта

@bot.message_handler(content_types=['text'])
def get_project(message):

	bot.send_message(message.from_user.id, 'Данные вашего проекта добавлены в базу', reply_markup=m.first_markup)
	
	project_data = message.text.split(',')
	project_name = str(project_data[0])
	sample_count = int(project_data[1].replace(' ',''))
	user_id = message.from_user.id

	cursor.execute("SELECT end_sample FROM projects_list ORDER BY ID DESC LIMIT 1")
	result = cursor.fetchone()
	if result is None:
		start_sample = 1
	else:
		start_sample = result[0]+1

	end_sample = start_sample + sample_count - 1

	db_projects_list_val(user_id, project_name, start_sample, end_sample)

	bot.send_message(message.from_user.id, 'Название Вашего проекта "' + project_name + '"')
	bot.send_message(message.from_user.id, 'Ваши номера проб:' + str(start_sample) + "-" + str(end_sample))


### Чтобы бот работал постоянно 

bot.polling()