
#На вход даны следующие данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в список
students_list = list(students)

# Сортируем список
students_sorted = sorted(students_list)

# Словарь для хранения средних баллов
averages = {}

# Цикл по ученикам
for student in students_sorted:
    # Получаем оценки ученика
    scores = grades[students_list.index(student)]
    # Вычисляем средний балл
    average = sum(scores) / len(scores)
    # Сохраняем результат в словаре
    averages[student] = average

# Выводим результаты
print(averages)
