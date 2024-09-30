
def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи в режиме текстового файла с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Получаем текущую позицию в байтах
            byte_position = file.tell()
            # Записываем строку в файл с добавлением символа новой строки
            file.write(string + '\n')
            # Сохраняем номер строки и ее начальную позицию в словарь
            strings_positions[(index + 1, byte_position)] = string

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for exits in result.items():
    print(exits)
