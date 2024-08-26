
def calculate_structure_sum(*args):
    total_sum = 0

    for data in args:
        if isinstance(data, (list, tuple, set)):  # Рекурсивно обрабатываем элементы список кортеж и множество
            for item in data:
                total_sum += calculate_structure_sum(item)

        elif isinstance(data, dict):
            for key, value in data.items():
                # Учитываем ключ и значение отдельно
                total_sum += calculate_structure_sum(key)    # Суммируем ключи
                total_sum += calculate_structure_sum(value)  # Суммируем значения

        elif isinstance(data, str):
            total_sum += len(data)  # Считаем длину строк

        elif isinstance(data, (int, float)):
            total_sum += data  # Суммируем числовые значения

    return total_sum

# входные данные:
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

