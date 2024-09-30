class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        # Создаем файл, если он не существует
        with open(self.__file_name, 'a') as f:
            pass

    def get_products(self):
        with open(self.__file_name, 'r') as f:
            return f.read().strip()

    def add(self, *products):
        existing_products = self.get_products().splitlines()  # создаем список продуктов
        existing_names = {p.split(',')[0] for p in existing_products}  # создаем множество с названиями продуктов

        for product in products:
            if product.name in existing_names:
                print(f"Продукт {product} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as f:
                    f.write(f"{product}\n")

# Пример использования классов
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Выводит: Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)  # Добавить продукты в магазин

print(s1.get_products())  # Вывод всех продуктов из файла
