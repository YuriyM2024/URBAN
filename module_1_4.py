# Создаем переменную my_string и присваиваем ей значение строки с произвольным текстом
my_string = input("Введите текст: ")
# Выводим количество символов введенного текста
print(len(my_string))
# Выводим строку my_string в верхнем регистре
print(my_string.upper())
# Выводим строку my_string в нижнем регистре
print(my_string.lower())
# Изменяем строку my_string, удаляя все пробелы
my_string = my_string.replace(' ', '')
print(my_string)
# Выводим первый символ строки my_string
print(my_string[0])
# Выводим последний символ строки my_string
print(my_string[-1])