# Данные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для вычисления разницы длин строк из списков, если длины не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк на одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример выполнения кода
print(list(first_result))   # Результат: [1, 2]
print(list(second_result))  # Результат: [False, False, True]
