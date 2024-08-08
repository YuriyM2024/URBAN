# Работа со словарями
my_dict = {'Иван': 1990, 'Анна': 1995, 'Мария': 1997}
print("Dict: ", my_dict)

# Вывод значения по существующему ключу
print("Existing value: ", my_dict['Иван'])

# Вывод значения по отсутствующему ключу без ошибки
print("Not existing value:", my_dict.get('Елена'))

# Добавление двух пар в словарь
my_dict['Николай'] = 1992
my_dict['Ольга'] = 1993

# Удаление пары по ключу
a = my_dict.pop('Анна')
print("Deleted value: ", a)
print("Modified dictionary: ", my_dict)

# Работа с множествами
my_set = {'Иван', 1990, True, 'Анна', 1995, 1990, True}
print("Set: ", my_set)

# Добавление элементов в множество
my_set.add('Мария')
my_set.add(1997)

# Удаление элемента из множества
my_set.remove(True)
print("Modified set:", my_set)
