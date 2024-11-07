import numpy as np

# 1. Создание массива
arr = np.array([1, 2, 3, 4, 5])
print("Созданный массив:", arr)

# 2. Вычисление среднего значения
mean_value = np.mean(arr)
print("Среднее значение массива:", mean_value)

# 3. Создание двумерного массива и вычисление его транспонированной версии
matrix = np.array([[1, 2, 3], [4, 5, 6]])
transposed_matrix = matrix.T
print("Исходная матрица:\n", matrix)
print("Транспонированная матрица:\n", transposed_matrix)

# 4. Элементы массива, которые больше заданного порога
threshold = 3
elements_greater_than_threshold = arr[arr > threshold]
print("Элементы массива больше", threshold, ":", elements_greater_than_threshold)
