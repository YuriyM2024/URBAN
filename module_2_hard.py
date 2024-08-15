
#Импорт модуля для генерации случайных чисел.
import random

# Генерация первого списка с числами от 3 до 20 в случайном порядке
first_list = random.sample(range(3, 21), 18)

print(" Первое поле : ", first_list)

# Инициализация второго списка
second_list = []

# Проходим по каждому числу из первого списка
for number in first_list:
    # Инициализация переменной для индекса
    i = 1  # начинаем с 1 (число 1)

    # Список для хранения найденных пар для текущего числа
    pairs = []

    # Используем цикл while для поиска пар
    while i < 20:
        j = i + 1  # начинаем с числа, следующего за i
        while j <= 20:
            # Проверяем, не равно ли i или j текущему number
            if i != number and j != number:
                pair_sum = i + j
                # Проверяем кратность
                if number % pair_sum == 0:
                    pairs.append(f"{i}{j}")

            j += 1
        i += 1

    # Если нашли пары, добавляем строку с ними в второй список
    if pairs:
        second_list.append(f"{number} = {''.join(pairs)}")

# Вывод результатов
for result in second_list:
    print(" Пароль для" , result)
