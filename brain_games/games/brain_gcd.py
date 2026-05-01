import random


def gcd_game():
    description = "Find the greatest common divisor of given numbers."

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def game_logic():
        a = random.randint(1, 100) # NOSONAR
        b = random.randint(1, 100) # NOSONAR

        question = f"{a} {b}"
        answer = str(gcd(a, b))

        return question, answer

    return description, game_logic