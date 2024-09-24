# Базовые классы
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

# Классы наследники для животных
class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}.")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}, не съедобно.")

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}.")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}, не съедобно.")


# Классы наследники для растений
class Flower(Plant):
    def __init__(self, name):
        Plant.__init__(self, name)
        self.edible = False  # Цветы по умолчанию несъедобны

class Fruit(Plant):
    def __init__(self, name):
        Plant.__init__(self, name)
        self.edible = True  # Фрукты по умолчанию съедобны

# Выполняемый код(для проверки):
if __name__ == "__main__":
    # Создаем объекты
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
