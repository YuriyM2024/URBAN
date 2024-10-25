import threading
import time

class Knight(threading.Thread):
    total_enemies = 100  # Общее количество врагов
    total_days = 0       # Общее количество дней сражения

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        while Knight.total_enemies > 0:
            # Задержка в 1 секунду
            time.sleep(1)
            Knight.total_days += 1
            Knight.total_enemies -= self.power

            # Убедимся, что количество врагов не стало отрицательным
            remaining_enemies = max(Knight.total_enemies, 0)

            print(f"{self.name}, сражается {Knight.total_days} день..., осталось {remaining_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {Knight.total_days} дней!")


# Создание и запуск потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидаем завершения сражений
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
