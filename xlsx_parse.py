from openpyxl import load_workbook
from datetime import datetime

# Функция, которая приводит строку к корректному виду


def correct_string(string):
    """
    Функция удаляет случайные пробелы, которые могут быть поставлены заполнителем экселя
    """
    if string is not None and isinstance(string, str):
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
    if isinstance(string, int):
        return string


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


book = load_workbook(filename= "Menu.xlsx")

day_in_russian = dc_for_days[day_name]
data_in_day = book[day_in_russian]
list_for_daily_menu = []


# Находит кол-во линий в экселе
def count_lines_in_menu():
    count_lines = 0
    for _ in data_in_day:
        count_lines += 1
    return count_lines


def find_daily_menu():
    """
    Возвращает список кортежей меню из файла эксель
    """
    count_lines = count_lines_in_menu()
    for i in range(2, count_lines + 1):
        first = correct_string(data_in_day['A' + str(i)].value)
        second = correct_string(data_in_day['B' + str(i)].value)
        third = correct_string(data_in_day['C' + str(i)].value)
        fourth = correct_string(data_in_day['D' + str(i)].value)

        temp = (first, second, third, fourth)
        if temp != (None, None, None, None):    # Проверяет, чтобы кортеж не состоял из None
            list_for_daily_menu.append((first, second, third, fourth))

    return list_for_daily_menu