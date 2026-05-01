import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def game_logic():
    num = random.randint(1, 100)  # NOSONAR
    question = str(num)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return question, correct_answer