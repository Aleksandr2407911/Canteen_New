from openpyxl import load_workbook
from datetime import datetime

# Функция, которая приводит строку к корректному виду


def correct_string(string):
    temp = string.split()
    for i in range(len(temp)):
        if r'\xa0' in temp[i]:
            temp[i] = temp[i].strip(r'\xa0')
        else:
            temp[i] = temp[i].strip()

    for i in range(len(temp)):
        if r'\xa0' in temp[i]:
            temp[i] = ' '.join(temp[i].split(r'\xa0'))

    return ' '.join(temp)


# Находит название сегодняшнего дня на аглийском
today = datetime.today()
day_name = today.strftime("%A")


dc_for_days = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'
}


book = load_workbook(filename="Menu.xlsx")

day_in_russian = dc_for_days[day_name]
data_in_day = book[day_in_russian]
count_lines = 0
list_for_daily_menu = []

# Находит кол-во линий в экселе
for _ in data_in_day:
    count_lines += 1


def find_daily_menu():
    for i in range(2, count_lines + 1):
        first = correct_string(data_in_day['A' + str(i)].value)
        second = correct_string(data_in_day['B' + str(i)].value)
        third = data_in_day['C' + str(i)].value
        fourth = correct_string(data_in_day['D' + str(i)].value)

        list_for_daily_menu.append((first, second, third, fourth))

    return list_for_daily_menu


# Функция возращает сортированный список состоящий из категорий товаров взятой в xl, 
# принимает функцию find_daily_menu, без скобочек
def take_categories(find_daily_menu):
    list_catigories = set()
    for i in find_daily_menu():
        list_catigories.add(i[3])
    return sorted(list_catigories)

"""
# Функция для создания словарей под продукты и категорию для будущего использования в кнопках (на основе Excel)
def compose_dc():
    list_for_dc = find_daily_menu()
    dc_for_products = {}
    dc_for_categories = {}
    
    for i in range(len(list_for_dc)):
        dc_for_products[f"{'A' + str(i + 1)}"] = list_for_dc[i][0]
        dc_for_categories[list_for_dc[i][3]] = list_for_dc[i][3]

    return dc_for_products, dc_for_categories

# Использование функции
# products_dict, categories_dict = compose_dc()
"""