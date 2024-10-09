def add_everything_up(a, b):
    try:
        # Проверяем, являются ли a и b разными типами (число и строка)
        if isinstance(a, str) and isinstance(b, (int, float)) or isinstance(b, str) and isinstance(a, (int, float)):
            raise TypeError
        # Если они одного типа, складываем
        result = a + b
        # Возвращаем строку с округлением до трех знаков после запятой
        return f"{result:.3f}" if isinstance(result, (int, float)) else result
    except TypeError:
        # В случае ошибки возвращаем строковое представление a и b
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))          # Вывод: 130.456
