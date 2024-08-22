def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Убираем базовый случай для рекурсии
    if len(str_number) <= 1:
        return int(str_number)  # Возвращаем последнее число если оно одно

    # Отделяем первую цифру
    first = int(str_number[0])

    # Рекурсивный вызов для оставшихся цифр
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования
result = get_multiplied_digits(40203)
print(result)