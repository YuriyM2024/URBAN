import os
import time

# Задайте путь к каталогу для обхода

# print(os.getcwd())  # посмотрели путь у папке
# directory = r'C:\Users\Х\PycharmProjects\pythonProject\directory'  # Укажите нужный каталог"

directory = os.getcwd()  # работа в текущей директории

# Обход каталога
for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        # Формирование полного пути к файлу
        filepath = os.path.join(dirpath, file)

        # Получение времени последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получение размера файла
        filesize = os.path.getsize(filepath)

        # Получение родительской директории файла
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, \n Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
