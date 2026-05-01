import random


def even_game():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'

    def game_logic():
        num = random.randint(1, 100)
        answer = "yes" if num % 2 == 0 else "no"
        return num, answer

    return description, game_logic