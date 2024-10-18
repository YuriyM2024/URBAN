def all_variants(text):
    n = len(text)

    for i in range(n):   # Генерируем все возможные неподобные подстроки
        for j in range(i + 1, n + 1):
            yield text[i:j]  # Возвращаем подстроку с помощью оператора yield


# Пример использования
a = all_variants("abc")
for i in a:
    print(i)
