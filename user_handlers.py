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


# Функция для создания словарей под категории для будущего использования в инлайн кнопках (на основе БД)
def compose_dc_for_categories():
    list_for_dc = push_pull_to_DB.fetch_data_from_table('categories')
    dc_for_categories = {}
    
    for i in list_for_dc:
        dc_for_categories[f"category_{i['category']}"] = i['category']

    return dc_for_categories


def compose_dc_products_in_exact_category(category_name):
    list_for_dc = push_pull_to_DB.fetch_productlist_based_on_category(category_name)
    dc_for_products = {}
    
    for i in list_for_dc:
        dc_for_products[f"product_{i['name']}"] = i['name']
        
    return dc_for_products


# Функция создает клавиатуру на основе вытащенной из БД информации про категории
async def build_inline_keyboard(buttons):
    keyboard_list = InlineKeyboardBuilder()
    for callback, text in buttons.items():
        keyboard_list.add(InlineKeyboardButton(text=text, callback_data=callback))
    return keyboard_list.adjust(2).as_markup()
    

"""
ЭТО ТО ЧТО САНЯ ДЕЛАЛ

#Создаем объекты кнопок для категорий меню нужно взять из базы данных
list_buttons = []
for i in xlsx_parse.take_categories(xlsx_parse.find_daily_menu):
    button = [InlineKeyboardButton(text=i, callback_data=i)] # НЕОБХОДИМО ПОМЕНЯТЬ CALBACK_DATA, чтобы не было случайного вызова
    list_buttons.append(button)

# Создаем объект клавиатуры для категорий меню
keyboard_categories = InlineKeyboardMarkup(inline_keyboard=list_buttons)
"""

# Этот хэндлер будет срабатывать на кнопку '/start'
# и отправлять в чат клавиатуру главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Hi', reply_markup=Keyboard)

""" 
#этот хэндлер будет срабатывать на кнопку Меню 🍲
@router.message(F.text == 'Меню 🍲')
async def process_menu_command(message: Message):
    await message.answer(text='Меню 🍲', reply_markup= await build_inline_keyboard(compose_dc_for_categories()))
""" 


@router.message(F.text == 'Меню 🍲')
async def process_menu_command(message: Message):
    temp = compose_dc_products_in_exact_category('Горячее')
    keyboard = await build_inline_keyboard(temp)
    await message.answer(text='Меню 🍲', reply_markup=keyboard)
""" 
    

#хэндлер обрабатывает все кнопки category
@router.callback_query(lambda callback: callback.data.startswith('category_'))
async def get_back_from_category(callback: CallbackQuery):
    temp = compose_dc_for_categories()
    callback_data = temp[callback.data]
    await callback.message.answer(text= callback_data, reply_markup= await build_inline_keyboard(compose_dc_products_in_exact_category(callback_data)))
""" 

#@router.callback_query(lambda callback: callback.data.startswith('product_'))
#async def get_back_data_aboutproduct(callback: CallbackQuery):
