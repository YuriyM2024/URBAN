
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Создание first_result: длины строк из first_strings, длина >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Создание second_result: пары слов одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Объединение списков для создания third_result: словарь с четной длиной строк
combined = first_strings + second_strings
third_result = {s: len(s) for s in combined if len(s) % 2 == 0}

# Пример выполнения кода
print(first_result)   # Результат: [10, 8, 8]
print(second_result)  # Примерный результат будет зависеть от строки
print(third_result)   # Результат: {'Programmer': 10, 'Monitors': 8, 'Computer': 8}
