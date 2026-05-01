import random


def progression_game():
    description = "What number is missing in the progression?"

    def make_progression(start, step, length):
        return [start + i * step for i in range(length)]

    def game_logic():
        length = random.randint(5, 10) # NOSONAR
        start = random.randint(1, 20) # NOSONAR
        step = random.randint(1, 10) # NOSONAR

        progression = make_progression(start, step, length)

        hidden_index = random.randint(0, length - 1) # NOSONAR
        correct_answer = str(progression[hidden_index])

        progression[hidden_index] = ".."

        question = " ".join(str(x) for x in progression)

        return question, correct_answer

    return description, game_logic