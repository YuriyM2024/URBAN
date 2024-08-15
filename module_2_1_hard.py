
#Импорт модуля random для генерации случайных чисел
import random

# Генерация первого списка с числами от 3 до 20 в случайном порядке
first_list = random.sample(range(3, 21), 18)
print(" Первое поле : ", first_list)

# Инициализация второго списка
second_list = []

# Проходим по каждому числу из первого списка
for number in first_list:
    # Список для хранения найденных пар для текущего числа
    pairs = []

    # Генерируем пары чисел от 1 до 20
    for i in range(1, 21):
        for j in range(i + 1, 21):
            # Проверяем, не равно ли number одному из чисел в паре
            if number != i and number != j:
                pair_sum = i + j
                # Проверяем кратность
                if number % pair_sum == 0:
                    pairs.append(f"{i}{j}")

    # Если нашли пары, добавляем строку с ними в второй список
    if pairs:
        second_list.append(f"{number} - {''.join(pairs)}")

# Вывод результатов
for result in second_list:
    print(" Пароль для" , result)