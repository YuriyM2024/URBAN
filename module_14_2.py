import sqlite3

# Создаем файл базы данных и подключаемся к нему
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создаем таблицу Users, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполняем таблицу 10 записями
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000),
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

# Обновляем balance у каждой 2ой записи начиная с 1ой
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

# Удаляем каждую 3ю запись начиная с 1ой
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

# Удаляем запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчитываем общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчитываем сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Выводим средний баланс
if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0

print(f'Средний баланс всех пользователей: {average_balance}')

# Закрываем соединение с базой
conn.commit()
conn.close()