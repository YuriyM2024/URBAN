import sqlite3


def initiate_db(db_name='products.db'):
    """Создаем таблицу Products, если она еще не создана."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # SQL запрос для создания таблицы
    create_table_query = ('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image_filename TEXT NOT NULL
    );
    ''')

    cursor.execute(create_table_query)
    connection.commit()
    connection.close()


def populate_db(db_name='products.db'):
    """Заполняем таблицу Products предопределенными записями."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Проверяем, есть ли записи в таблице
    cursor.execute('SELECT COUNT(*) FROM Products;')
    count = cursor.fetchone()[0]

    if count > 0:
        print("Таблица уже содержит записи, заполнение не требуется.")
        connection.close()
        return

    # Предопределенные записи
    products = [
        ('Баночка с орехами', 'Полезные орехи', 100, "1.jpg"),
        ('Баночка с семенами', 'Семена для здоровья', 200, "2.jpg"),
        ('Баночка с сухофруктами', 'Сладкие и полезные', 300, "3.jpg"),
        ('Баночка с супер смесями', 'Супер смеси для энергии', 500, "4.jpg"),
    ]

    # SQL запрос для вставки данных
    insert_query = 'INSERT INTO Products (title, description, price, image_filename) VALUES (?, ?, ?, ?);'

    cursor.executemany(insert_query, products)
    connection.commit()
    connection.close()


def get_all_products(db_name='products.db'):
    """Возвращает все записи из таблицы Products."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # SQL запрос для получения всех продуктов
    cursor.execute('SELECT * FROM Products;')
    products = cursor.fetchall()

    connection.close()
    return products


# Пример использования функций
if __name__ == "__main__":
    initiate_db()
    populate_db()


