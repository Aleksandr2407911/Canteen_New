import pymysql
import queries_function
import xlsx_parse


# выдает список меню актуального дня
actual_day_menu = xlsx_parse.find_daily_menu()


# заполняет таблицу категорий в БД на основе экселя
def fill_categories_table(actual_day_menu):
    with connection.cursor() as cursor:
        for line in actual_day_menu:
            queries_function.insert_categories(cursor, line[3])
    connection.commit()
    connection.close()


# очищает любую таблицу, которую передашь в функцию
def clear_table(table_name):
    with connection.cursor() as cursor:
        queries_function.delete_data_from_tables(cursor, table_name)
    connection.commit()
    connection.close()


# достает информацию из любой таблицу в БД
def fetch_data_from_table(table_name):
    with connection.cursor() as cursor:
        queries_function.get_rows_from_table(cursor, table_name)
    data = cursor.fetchall()
    return data


# заполняет таблицу продуктов
def fill_product_table(actual_day_menu):
    with connection.cursor() as cursor:
        for i in actual_day_menu:
            queries_function.insert_product(cursor, i)
    connection.commit()
    connection.close()


# достает информацию из таблицы продуктов на основе категории
def fetch_productlist_based_on_category(category_name):
    with connection.cursor() as cursor:
        queries_function.fetch_product_based_on_category(cursor, category_name)
    data = cursor.fetchall()
    return data


try:
    # Подключение к БД MySQL
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='tg_bot',
        cursorclass=pymysql.cursors.DictCursor
    )

    #print(fetch_data_from_table('categories'))
    #clear_table('product')
    #fill_product_table(actual_day_menu)
    #print(fetch_productlist_based_on_category('Горячее'))


except Exception as e:
    print('Error3:', e)
