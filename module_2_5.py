def get_matrix(n, m, value):
    # Проверяем, что n и m больше 0
    if n <= 0 or m <= 0:
        return []

    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для строк
    for i in range(n):
        # Создаем пустой список для текущей строки
        row = []

        # Внутренний цикл для столбцов
        for j in range(m):
            # Добавляем значение value в текущую строку
            row.append(value)

        # Добавляем заполненную строку в матрицу
        matrix.append(row)

    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
