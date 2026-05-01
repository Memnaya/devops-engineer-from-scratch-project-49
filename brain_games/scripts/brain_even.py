import random

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return "yes" if num % 2 == 0 else "no"


def game_logic():
    task = random.randint(1, 100)
    return task, is_even(task)
