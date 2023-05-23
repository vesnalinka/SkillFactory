"""Game Guess the number: computer plays by itself"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Amount of attempts
    """
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # Guessing the number
        if number == predict_number:
            break # Exit the loop if number is guessed
    return count # Getting an amount of attempts

print(f'Количество попыток: {random_predict(10)}')

def score_game(random_predict) -> int:
    """Function to find mean amount of attempts for 1000 games 

    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: Mean attempts amount
    """
    count_ls = []
    np.random.seed(1) # Fixing seed
    # List of numbers to guess:
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls ))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score

if __name__ == '__main__':
    # Run
    score_game(random_predict)
