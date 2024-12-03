from rt_with_exceptions import Runner
import logging
import unittest


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s: %(levelname)s: %(message)s'
)


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Вася', -10)  # Передаем отрицательное значение
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Передаем что-то кроме строки
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            logging.info('"test_run" выполнен успешно')



if __name__ == "__main__":
    unittest.main()