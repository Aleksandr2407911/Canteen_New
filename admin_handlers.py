from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message,
                            KeyboardButton, ReplyKeyboardMarkup)

#инициализируем роутер уровня модуля
router = Router()

# Создаем объект кнопок главного меню
button_1 = KeyboardButton(text='Добавить меню 🍲')
button_2 = KeyboardButton(text='Подтверждение заказов 🕐')


# Создаем объект клавиатуры и добавляем кнопки главного меню
Keyboard = ReplyKeyboardMarkup(keyboard=[[button_1], [button_2]], resize_keyboard= True)


# Этот хэндлер будет срабатывать на кнопку '/start'
# и отправлять в чат клавиатуру главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text= 'привет', reply_markup=Keyboard)
