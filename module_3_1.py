
# Глобальная переменная для подсчета вызовов функций
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)


def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()  # Приводим строку к нижнему регистру
    # Приводим все элементы списка к нижнему регистру для сравнения
    for item in list_to_search:
        if string_lower == item.lower():
            return True
    return False


# Примеры вызова функций
print(string_info('Capybara'))       # Информация о строке 'Capybara'
print(string_info('Armageddon'))     # Информация о строке 'Armageddon'
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))   # No matches


# Вывод значения переменной calls
print("Всего вызовов: ", calls)
