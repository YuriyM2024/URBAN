import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  # Создаем объект блокировки

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)  # Имитация задержки

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)  # Имитация задержки

# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запускаем потоки
th1.start()
th2.start()

# Ждем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
