class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'black', 'white', 'green']

    def __init__(self, owner: str, model: str,  color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power


    def is_valid_color(self, color: str) -> bool:
        return color.lower() in (variant.lower() for variant in self.__COLOR_VARIANTS)

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if self.is_valid_color(new_color):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        Vehicle.__init__(self, owner, model, engine_power, color)


# Исходный код:
# Tекущие цвета
__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# # Меняем свойства ( вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
vehicle1.print_info()
