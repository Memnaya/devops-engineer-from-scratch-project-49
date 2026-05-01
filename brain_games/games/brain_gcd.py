import random

TASK = "Find the greatest common divisor of given numbers."


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def game_logic():
    a = random.randint(1, 100)  # NOSONAR
    b = random.randint(1, 100)  # NOSONAR

    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))

    return question, correct_answer