import random


def calc_game():
    description = "What is the result of the expression?"
    operations = ["+", "-", "*"]

    def calculate(a, b, op):
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b

    def game_logic():
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        op = random.choice(operations)

        question = f"{a} {op} {b}"
        answer = str(calculate(a, b, op))

        return question, answer

    return description, game_logic