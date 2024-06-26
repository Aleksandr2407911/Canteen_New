from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message,
                           KeyboardButton, ReplyKeyboardMarkup, CallbackQuery)
import xlsx_parse
import push_pull_to_DB
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

# инициализируем роутер уровня модуля
router = Router()

# Создаем объект кнопок главного меню
button_1 = KeyboardButton(text='Меню 🍲')
button_2 = KeyboardButton(text='Корзина 🧺')
button_3 = KeyboardButton(text='Мои заказы 🕐')

# Создаем объект клавиатуры и добавляем кнопки главного меню
Keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2], [button_3]], resize_keyboard=True)


<<<<<<< HEAD
#Создаем объекты кнопок - категории меню нужно взять из базы данных
list_buttons = []
for i in xlsx_parse.take_categories(xlsx_parse.find_daily_menu).items():
    button = [InlineKeyboardButton(text=i[0], callback_data=i[0])] # НЕОБХОДИМО ПОМЕНЯТЬ CALBACK_DATA, чтобы не было случайного вызова
    list_buttons.append(button)
=======
def modify_string_to_correct_size(string):
    """
    Функция, которая принимает строку, проверяет ее размер, 
    если он больше 64 байт, то сокращает ее и возвращает,
    если меньше, то просто возвращает
    """
    if len(string.encode("utf-8")) > 64:
        string = string[:27] + '...'
    return string
>>>>>>> VB2


# Функция для создания словарей под категории для будущего использования в инлайн кнопках (на основе БД)
def compose_dc_for_categories():
    """
    Создает слоаварь, на основе БД таблица категорий, типа {ключ(callback): значение(text)}
    Цели создание словаря: удобство создавать кнопки и их callback, а также при нажатии кнопки быстро находит значение
    Впереди ключа ставлю c_ сокращено categories_, для дальнейшего удобство при ловле в хендлер
    """
    list_for_dc = push_pull_to_DB.fetch_data_from_table('categories')
    dc_for_categories = {}

    for i in list_for_dc:
        dc_for_categories[modify_string_to_correct_size(
            f"c_{i['category']}")] = i[modify_string_to_correct_size('category')]

    return dc_for_categories


# Функция для создания словарей под продукты для будущего использования в инлайн кнопках (на основе БД)
def compose_dc_products_in_exact_category(category_name):
    """
    Создает слоаварь, на основе БД таблица категорий, типа {ключ(callback): значение(text)}
    Цели создание словаря: удобство создавать кнопки и их callback, а также при нажатии кнопки быстро находит значение
    Впереди ключа ставлю p_ сокращено products_, для дальнейшего удобство при ловле в хендлер
    """
    list_for_dc = push_pull_to_DB.fetch_productlist_based_on_category(
        category_name)
    dc_for_products = {}

    for i in list_for_dc:
        dc_for_products[modify_string_to_correct_size(
            f"p_{i['name']}")] = i[modify_string_to_correct_size('name')]

    return dc_for_products


# Функция создает клавиатуру на словаря про категории
async def build_inline_keyboard_for_categories(buttons):
    """
    Сначала создает элемент клавиатуры keyboard_list
    Проходит по словарю с методом items() 
    Добавляет в клавиатуру текст и callback
    Возвращает клавиатру. 
    .adjust(2) - указывает, что кнопок будет 2 в ряд 
    .as_markup() - обязательно писать в конце, иначе работать не будет
    """
    keyboard_list = InlineKeyboardBuilder()
    for callback, text in buttons.items():
        keyboard_list.add(InlineKeyboardButton(
            text=text, callback_data=callback))
    return keyboard_list.adjust(2).as_markup()


# Функция создает клавиатуру на основе словаря про продукты
async def build_inline_keyboard_for_products(buttons):
    """
    Сначала создает элемент клавиатуры keyboard_list
    Проходит по словарю с методом items() 
    Добавляет в клавиатуру текст и callback
    После for добавляет кнопку назад
    Возвращает клавиатру. 
    .adjust(2) - указывает, что кнопок будет 2 в ряд 
    .as_markup() - обязательно писать в конце, иначе работать не будет
    """
    keyboard_list = InlineKeyboardBuilder()
    for callback, text in buttons.items():
        keyboard_list.add(InlineKeyboardButton(
            text=text, callback_data=callback))
    back_button = InlineKeyboardButton(text="Назад", callback_data="back_c")
    keyboard_list.row(back_button)
    return keyboard_list.adjust(1).as_markup()


# Создаем объекты кнопок товара
#handlers_prosucts = []
for key, value in xlsx_parse.take_categories(xlsx_parse.find_daily_menu).items():
    list_buttons = []
    for v in value:
        button = [InlineKeyboardButton(text=v, callback_data=v)]
        list_buttons.append(button)
    keyboard_food = InlineKeyboardMarkup(inline_keyboard=list_buttons)
    #эти хэндлеры будут срабатывать на нажатие кнопок категорий
    @router.message(F.data == key)
    async def process_categories_comands(message: Message):
        await message.answer(text='key', reply_markup=keyboard_food)

    #handlers_prosucts.append(process_categories_comands)


# Этот хэндлер будет срабатывать на кнопку '/start'
# и отправлять в чат клавиатуру главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Hi', reply_markup=Keyboard)


# этот хэндлер будет срабатывать на кнопку Меню 🍲
@router.message(F.text == 'Меню 🍲')
async def process_menu_command(message: Message):
    await message.answer(text='Меню 🍲', reply_markup=await build_inline_keyboard_for_categories(compose_dc_for_categories()))

<<<<<<< HEAD
'''# этот роутер будет отлавливать нажатие на кнопки категориий 
@router.message(F.data in xlsx_parse.take_categories(xlsx_parse.find_daily_menu).keys())
async def process_categories_command(message: Message):
    await message.answer(text='Меню 🍲', reply_markup=keyboard_categories)'''

=======

# хэндлер обрабатывает все кнопки category и вывод, что находится в категории
@router.callback_query(lambda callback: callback.data.startswith('c_'))
async def get_back_from_category(callback: CallbackQuery):
    temp = compose_dc_for_categories()
    callback_data = temp[callback.data]
    await callback.message.edit_text(text=callback_data, reply_markup=await build_inline_keyboard_for_products(compose_dc_products_in_exact_category(callback_data)))


# хэндлер реагирует на кнопку назад
@router.callback_query(F.data == "back_c")
async def return_to_category(callback: CallbackQuery):
    await callback.message.edit_text(text='Меню 🍲', reply_markup=await build_inline_keyboard_for_categories(compose_dc_for_categories()))

# @router.callback_query(lambda callback: callback.data.startswith('p_'))
# async def get_back_data_aboutproduct(callback: CallbackQuery):
>>>>>>> VB2
