from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message,
                            KeyboardButton, ReplyKeyboardMarkup, CallbackQuery)
import xlsx_parse
import push_pull_to_DB
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

#инициализируем роутер уровня модуля
router = Router()

# Создаем объект кнопок главного меню
button_1 = KeyboardButton(text='Меню 🍲')
button_2 = KeyboardButton(text='Корзина 🧺')
button_3 = KeyboardButton(text='Мои заказы 🕐')

# Создаем объект клавиатуры и добавляем кнопки главного меню
Keyboard = ReplyKeyboardMarkup(keyboard=[[button_1], [button_2], [button_3]], resize_keyboard= True)


def modify_string_to_correct_size(string):
    if len(string.encode("utf-8")) > 64:
        string = string[:27] + '...'
    return string


# Функция для создания словарей под категории для будущего использования в инлайн кнопках (на основе БД)
def compose_dc_for_categories():
    list_for_dc = push_pull_to_DB.fetch_data_from_table('categories')
    dc_for_categories = {}
    
    for i in list_for_dc:
        dc_for_categories[modify_string_to_correct_size(f"c_{i['category']}")] = i[modify_string_to_correct_size('category')]

    return dc_for_categories


def compose_dc_products_in_exact_category(category_name):
    list_for_dc = push_pull_to_DB.fetch_productlist_based_on_category(category_name)
    dc_for_products = {}
    
    for i in list_for_dc:
        dc_for_products[modify_string_to_correct_size(f"p_{i['name']}")] = i[modify_string_to_correct_size('name')]
        
    return dc_for_products


# Функция создает клавиатуру на основе вытащенной из БД информации про категории
async def build_inline_keyboard(buttons):
    keyboard_list = InlineKeyboardBuilder()
    for callback, text in buttons.items():
        keyboard_list.add(InlineKeyboardButton(text=text, callback_data=callback))
    return keyboard_list.adjust(2).as_markup()


# Этот хэндлер будет срабатывать на кнопку '/start'
# и отправлять в чат клавиатуру главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Hi', reply_markup=Keyboard)

 
#этот хэндлер будет срабатывать на кнопку Меню 🍲
@router.message(F.text == 'Меню 🍲')
async def process_menu_command(message: Message):
    await message.answer(text='Меню 🍲', reply_markup= await build_inline_keyboard(compose_dc_for_categories()))


#хэндлер обрабатывает все кнопки category
@router.callback_query(lambda callback: callback.data.startswith('c_'))
async def get_back_from_category(callback: CallbackQuery):
    temp = compose_dc_for_categories()
    callback_data = temp[callback.data]
    await callback.message.answer(text= callback_data, reply_markup= await build_inline_keyboard(compose_dc_products_in_exact_category(callback_data)))


#@router.callback_query(lambda callback: callback.data.startswith('p_'))
#async def get_back_data_aboutproduct(callback: CallbackQuery):
