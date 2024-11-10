import inspect


def introspection_info(obj):
    info_obj = {}


    # Определяем тип объекта
    info_obj['type'] = type(obj).__name__

    # Определяем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))]
    info_obj['attributes'] = attributes

    # Определяем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    info_obj['methods'] = methods

    # Определяем модуль, к которому принадлежит объект (если доступно)
    info_obj['module'] = getattr(obj, '__module__', None)

    return info_obj


# Пример создания своего класса и инстанса этого класса
class MyClass:
    def __init__(self, value):
        self.value = value

    def greet(self):
        return f'Привет! Этот атрибут {self.value}'


# Создаем объект своего класса
my_obj = MyClass(10)

# Интроспекция объекта
obj_info = introspection_info(my_obj)
print(obj_info)

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)
