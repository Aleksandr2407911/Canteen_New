from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message,
                            KeyboardButton, ReplyKeyboardMarkup)
from filters import is_admin_filter
from aiogram import F

# Инициализируем роутер уровня модуля
router = Router()

# Ставим фильтр для роутера уровня модуля
router.message.filter(is_admin_filter)


# Создаем объекты кнопок главного меню
button_1 = KeyboardButton(text='Добавить меню 🍲')
button_2 = KeyboardButton(text='Подтверждение заказов 🕐')

# Создаем объект клавиатуры и добавляем кнопки главного меню
Keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True)


'''#Создаем объекты кнопок списка заказов нужно взять из базы данных
list_buttons = []
for i in range():
    button = [KeyboardButton(text='НОМЕР ЗАКАЗА')] # нужно взять из базы номер заказа и вписать в название кнопки
    list_buttons.append(button)

# Создаем объект клавиатуры для списка заказов
Keyboard_orders = ReplyKeyboardMarkup(keyboard=list_buttons)'''


# Этот хэндлер будет срабатывать на кнопку '/start'
# и отправлять в чат клавиатуру главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Hi', reply_markup=Keyboard)

@router.message(F.text)
async def deny_accept_order(message: Message):
    await message.answer('Hi')