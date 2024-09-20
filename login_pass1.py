import re

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm and self.validate_password(password):
            self.password = password
        else:
            self.password = None  # Или можно вызвать исключение

    def validate_password(self, password):
        # Проверка на наличие хотя бы одной заглавной буквы и одной цифры
        return bool(re.search(r'[A-Z]', password) and re.search(r'[0-9]', password))


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Привет! Выберите действие: \n1 - вход \n2 - регистрация \n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен дляпользователя: , {login}')
                    break
                else:
                    print('Неверный пароль!')
            else:
                print('Пользователь не найден!')
        elif choice == 2:
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            password_confirm = input("Повторите пароль: ")
            user = User(username, password, password_confirm)
            if user.password:
                database.add_user(user.username, user.password)
                print("Пользователь успешно зарегистрирован.")
            else:
                print('Пароли не совпадают или не удовлетворяют требованиям. '
                      'Убедитесь, что пароль содержит хотя бы одну заглавную букву и одну цифру.')
        print("Текущие пользователи:", database.data)
