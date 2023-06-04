"""Game Guess the number: computer pretends to be smart"""
import numpy as np


def smart_predict(number: int = 1) -> int:
    """Guessing the number using middle number in section

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Amount of attempts
    """
    count = 0  # Setting count of the attempts
    middle = 50  # Setting middle in section from 1 to 100
    x = 0  # Setting var to search number by +-1

    while True:

        if number < middle:  # Searching in the section 1-50
            middle_1_50 = round(middle / 2)
            count += 1  # Since the move is equal to "Number == 50?"
            # with an answer "The number is smaller"
            if number < middle_1_50:  # Searching in the section 1-25
                middle_1_25 = round(middle / 4)
                count += 1
                if number < middle_1_25:  # Searching in the section 1-12
                    middle_1_12 = round(middle_1_25 / 2)
                    count += 1
                    if number < middle_1_12:  # Searching in the section 1-6
                        x = middle_1_12
                        while x != number:
                            x -= 1
                            count += 1
                        if x == number:
                            break
                    elif number > middle_1_12:  # Searching in the section 6-12
                        x = middle_1_12
                        while x != number:
                            x += 1
                            count += 1
                        if x == number:
                            break
                    else:
                        break

                elif number > middle_1_25:  # Searching in the section 12-25
                    middle_13_25 = round(middle_1_25 + middle / 8)
                    count += 1
                    if number < middle_13_25:  # Searching in the section 12-18
                        x = middle_13_25
                        while x != number:
                            x -= 1
                            count += 1
                        if x == number:
                            break
                    elif number > middle_13_25:  # Searching in the section 18-25
                        x = middle_13_25
                        while x != number:
                            x += 1
                            count += 1
                        if x == number:
                            break
                    else:
                        break

                else:
                    break

            elif number > middle_1_50:  # Searching in the section 25-50
                middle_25_50 = round(middle - middle / 4)
                count += 1
                if number < middle_25_50:  # Searching in the section 25-38
                    x = middle_25_50
                    while x != number:
                        x -= 1
                        count += 1
                    if x == number:
                        break
                elif number > middle_25_50:  # Searching in the section 38-50
                    x = middle_25_50
                    while x != number:
                        x += 1
                        count += 1
                    if x == number:
                        break
                else:
                    break
            else:
                break

        elif number > middle:  # Searching in the section 50-100
            middle_50_100 = round(middle + middle / 2)
            count += 1
            if number < middle_50_100:  # Searching in the section 50-75
                middle_50_75 = round(middle + middle / 4)
                count += 1
                if number < middle_50_75:  # Searching in the section 50-62
                    x = middle_50_75
                    while x != number:
                        x -= 1
                        count += 1
                    if x == number:
                        break
                elif number > middle_50_75:  # Searching in the section 62-75
                    x = middle_50_75
                    while x != number:
                        x += 1
                        count += 1
                    if x == number:
                        break
                else:
                    break
            elif number > middle_50_100:  # Searching in the section 75-100
                middle_75_100 = round(100 - middle / 4)
                if number < middle_75_100:  # Searching in the section 75-87
                    x = middle_75_100
                    while x != number:
                        x -= 1
                        count += 1
                    if x == number:
                        break
                elif number > middle_75_100:  # Searching in the section 87-100
                    middle_75_100
                    while x != number:
                        x += 1
                        count += 1
                    if x == number:
                        break
                else:
                    break

            else:
                break

        else:
            break  # Exit the loop when number is guessed

    return count  # Getting an amount of attempts


def score_game(smart_predict) -> int:
    """Function to find mean amount of attempts for 1000 games

    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: Mean attempts amount
    """
    count_ls = []
    np.random.seed(1)  # Fixing seed
    # Creating a list of numbers to guess:
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(smart_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


print(score_game(smart_predict))

if __name__ == "__main__":
    # RUN
    score_game(smart_predict)