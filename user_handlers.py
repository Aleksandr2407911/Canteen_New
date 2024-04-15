from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message,
                            KeyboardButton, ReplyKeyboardMarkup)
import xlsx_parse
from aiogram import F

#инициализируем роутер уровня модуля
router = Router()

# Создаем объект кнопок главного меню
button_1 = KeyboardButton(text='Меню 🍲')
button_2 = KeyboardButton(text='Корзина 🧺')
button_3 = KeyboardButton(text='Мои заказы 🕐')

# Создаем объект клавиатуры и добавляем кнопки главного меню
Keyboard = ReplyKeyboardMarkup(keyboard=[[button_1], [button_2], [button_3]], resize_keyboard= True)


#Создаем объекты кнопок для категорий меню нужно взять из базы данных
list_buttons = []
for i in xlsx_parse.take_categories(xlsx_parse.find_daily_menu):
    button = [InlineKeyboardButton(text=i, callback_data=i)] # НЕОБХОДИМО ПОМЕНЯТЬ CALBACK_DATA, чтобы не было случайного вызова
    list_buttons.append(button)

# Создаем объект клавиатуры для категорий меню
keyboard_categories = InlineKeyboardMarkup(inline_keyboard=list_buttons)


# Этот хэндлер будет срабатывать на кнопку '/start'
# и отправлять в чат клавиатуру главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Hi', reply_markup=Keyboard)

#этот хэндлер будет срабатывать на кнопку Меню 🍲
@router.message(F.text == 'Меню 🍲')
async def process_menu_command(message: Message):
    await message.answer(text='Меню 🍲', reply_markup=keyboard_categories)

