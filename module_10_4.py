import threading
import random
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость, сидящий за столом, по умолчанию None

# Этот класс наследуется от Thread и представляет гостей кафе.


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Ожидаем случайное время от 3 до 10 секунд, проведенное в кафе
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Создаем очередь для гостей, ждущих столов
        self.tables = tables   # Сохраняем столы в кафе

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = self.find_free_table()
            if free_table:
                free_table.guest = guest
                guest.start()  # Запускаем поток гость
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)  # Помещаем в очередь, если нет свободных столов
                print(f"{guest.name} в очереди")

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:  # Находим свободный стол
                return table
        return None

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():  # Если гость закончил прием пищи
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty():  # Если в очереди есть гости
                        next_guest = self.queue.get()  # Берем следующего из очереди
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(2)  # Задержка 2sec

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
