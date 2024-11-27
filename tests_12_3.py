import unittest


def skip_if_frozen(test_func):
    """Декоратор для пропуска тестов, если is_frozen = True."""
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertEqual(2 * 2, 4)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(3 + 3, 6)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertEqual(5 - 2, 3)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertTrue(False)
