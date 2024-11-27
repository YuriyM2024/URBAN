import unittest
from tests_12_3 import RunnerTest, TournamentTest


# Создание TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))


# Запуск тестов
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
