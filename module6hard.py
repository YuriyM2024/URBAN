import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self._sides = []
        self.__color = [0, 0, 0]
        self.filled = False
        self.set_color(*color)
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
#        else:
#            raise ValueError("Invalid color values. Must be integers between 0 and 255.")

    def __is_valid_sides(self, *new_sides):
        # Проверка на корректность числа сторон
        if len(new_sides) != self.sides_count:
            return False
        # Проверка для круга (один параметр - радиус)
        if self.sides_count == 1:
            return isinstance(new_sides[0], (int, float)) and new_sides[0] > 0
        # Проверка для многоугольников
        return all(isinstance(side, (int, float)) and side > 0 for side in new_sides)

    def get_sides(self):
        return tuple(self._sides)

    def __len__(self):
        return sum(self._sides)  # Изменили на сумму сторон

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)
        self.radius = circumference / (2 * math.pi)  # Вычисляем радиус

    def get_square(self):
        return math.pi * (self.radius ** 2)

    def get_sides(self):  # Переопределяем для круга
        return [self.radius]  # Возвращаем радиус как только одну "сторону"


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # Устанавливаем пустое значение для сторон
        if len(sides) == 0:
            self._sides = [1, 1, 1]  # По умолчанию

    def get_square(self):
        a, b, c = self._sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color)
        self.set_sides(*([side_length] * Cube.sides_count))  # Устанавливаем стороны куба

    def get_volume(self):
        return self._sides[0] ** 3  # Объем куба

# Входные данные
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина
print(len(circle1))

# Проверка объема (куба):
print(cube1.get_volume())
