"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict1(number: int = 1) -> int:
    """Угадываем число за количество попыток не более 20

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min1  = 1 # нижняя граница
    max1 = 100 # верхняя граница
    predict_number = np.random.randint(1, 101)  # предполагаемое число, начинаем с рандома
    
    while True:
        count += 1
        if number > predict_number:
            min1 = predict_number
            predict_number = max1 - (max1 - min1)//2
        elif number < predict_number:
            max1 = predict_number
            predict_number = min1 + (max1 - min1)//2
        else:
            #print(f"Вы угадали число! Это число = {predict_number}, за {count} попыток")
            break  # выход из цикла если угадали

    return count


def score_game1(random_predict1) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict1(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    print(f'Среднее число попыток {int(np.mean(count_ls))}') 
    print(f'Максимальное количество попыток {max(count_ls)}') 
    print(f'Минимальное количество попыток {min(count_ls)}')
    return score


if __name__ == "__main__":
    # RUN
    score_game1(random_predict1)