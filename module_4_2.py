
def test_function():
    # Внутренняя функция
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов внутренней функции
    inner_function()

# Вызов главной функции
test_function()