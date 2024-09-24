class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук, который издает лошадь

    def run(self, dx):
        self.x_distance += dx  # увеличиваем x_distance на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy  # увеличиваем y_distance на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()  # инициализируем родительский класс (первый в MRO - Horse)
        Eagle.__init__(self)  # инициализируем второй родительский класс (Eagle)

    def move(self, dx, dy):
        super().run(dx)  # вызываем метод run из Horse через super()
        super().fly(dy)  # вызываем метод fly из Eagle через super()

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # возвращаем текущую позицию

    def voice(self):
        print(f"Pegasus sound: {self.sound}")  # выводим звук


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()