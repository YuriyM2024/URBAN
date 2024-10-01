import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем имена файлов в кортеже

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        # Приведение строки к нижнему регистру и удаление лишних символов
                        line = line.lower()
                        # Используем регулярное выражение для нахождения слов
                        words.extend(re.findall(r"[a-zа-яё']+", line))  # Подходим к русским и английским словам
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        """Ищет слово и возвращает словарь с позициями первого вхождения слова в каждом файле."""
        all_words = self.get_all_words()  # Получаем все слова из файлов
        word_lower = word.lower()  # Приводим искомое слово к нижнему регистру
        results = {}

        for name, words in all_words.items():
            try:
                # Применяем список в нижнем регистре, чтобы найти позицию
                position = words.index(word_lower)  # Находим позицию первого вхождения слова
                results[name] = position + 1  # Сохраняем результат в словарь, +1 для счёта с 1 слова
            except ValueError:
                results[name] = -1  # Если слово не найдено, устанавливаем -1
        return results

    def count(self, word):
        """Считает количество вхождений слова в каждом файле."""
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        results = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for name, words in all_words.items():
            count = words.count(word)  # Считаем количество вхождений слова
            results[name] = count  # Сохраняем результат в словарь
        return results


# Пример использования класса

if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте
