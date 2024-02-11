import numpy as np

def binary_search_predict(number: int = 1) -> int:
    
    
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict_number = (low + high) // 2
        if number == predict_number:
            break
        elif number > predict_number:
            low = predict_number + 1
        else:
            high = predict_number - 1

    return count

def score_game(binary_search_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_search_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(42)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(binary_search_predict)
