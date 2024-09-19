class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
        else:
            self.password = None  # Или можно вызвать исключение


if __name__ == '__main__':
    user = User(input("Ведите логин: "), input("Введите пароль: "), input("Повторите пароль: "))

    if user.password:  # Проверяем, инициализирован ли пароль
        database = Database()
        database.add_user(user.username, user.password)
        print(database.data)
    else:
        print("Пароли не совпадают. Пользователь не добавлен.")