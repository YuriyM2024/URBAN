from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:  # Открываем файл для добавления данных (append mode)
            for item in data_set:
                file.write(f"{item}\n")  # Записываем элемент в файл (каждый с новой строки)

    return write_everything


# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем переданные слова в атрибут

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из коллекции


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Случайный выбор
print(first_ball())  # Случайный выбор
print(first_ball())  # Случайный выбор
