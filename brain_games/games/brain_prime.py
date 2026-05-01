import random


def prime_game():
    description = (
    'Answer "yes" if given number is prime. '
    'Otherwise answer "no".'
    )

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2

        return True

    def game_logic():
        number = random.randint(1, 100) # NOSONAR

        question = str(number)
        answer = "yes" if is_prime(number) else "no"

        return question, answer

    return description, game_logic