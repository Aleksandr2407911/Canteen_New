import pymysql
import queries_function
import xlsx_parse


# выдает список меню актуального дня
actual_day_menu = xlsx_parse.find_daily_menu()


def fill_categories_table(actual_day_menu):
    with connection.cursor() as cursor:
        for line in actual_day_menu:
            queries_function.insert_categories(cursor, line[3])
    connection.commit()
    connection.close()


def clear_table(table_name):
    with connection.cursor() as cursor:
        queries_function.delete_data_from_tables(cursor, table_name)
    connection.commit()
    connection.close()


def fetch_data_from_table(table_name):
    with connection.cursor() as cursor:
        queries_function.get_rows_from_table(cursor, table_name)
    data = cursor.fetchall()
    return data


def fill_product_table(actual_day_menu):
    with connection.cursor() as cursor:
        for i in actual_day_menu:
            print(queries_function.insert_product(cursor, i))
    connection.commit()
    connection.close()


try:
    # Подключение к БД MySQL
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='cahat50',
        database='canteen',
        cursorclass=pymysql.cursors.DictCursor
    )

    print(fetch_data_from_table('categories'))
    #clear_table('categories')


except Exception as e:
    print('Error3:', e)
