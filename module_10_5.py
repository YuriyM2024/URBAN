import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())   # Добавляем строку в список без пробелов
    # return all_data


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # перебор списка файлов

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"{linear_duration:.6f} (линейный)")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multi_process_duration = time.time() - start_time
    print(f"{multi_process_duration:.6f} (многопроцессный)")
