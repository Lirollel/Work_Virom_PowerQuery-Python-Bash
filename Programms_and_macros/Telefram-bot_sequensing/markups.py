from telebot import types

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

first_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
first_btn1 = 'Создать проект'
first_btn2 = 'Мои проекты'
first_btn3 = 'Все проекты'
first_markup_btn1 = types.KeyboardButton(first_btn1)
first_markup_btn2 = types.KeyboardButton(first_btn2)
first_markup_btn3 = types.KeyboardButton(first_btn3)
first_markup.add(first_markup_btn1, first_markup_btn2, first_markup_btn3)

back_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
back_btn1 = types.KeyboardButton('Назад')
back_btn2 = types.KeyboardButton('Удалить последний проект')
back_markup.add(back_btn1, back_btn2)
