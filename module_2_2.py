# Ввод трех целых чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Условная конструкция для проверки равенства чисел
if first == second and second == third:
    print(3)  # Все три числа равны
elif first == second or second == third or first == third:
    print(2)  # если два числа равны
else:
    print(0)  # Нет равных чисел
