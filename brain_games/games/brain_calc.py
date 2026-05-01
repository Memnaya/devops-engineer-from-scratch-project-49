import random

TASK = "What is the result of the expression?"

operations = ["+", "-", "*"]


def calculate(a: int, b: int, op: str) -> int:
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b


def game_logic():
    a = random.randint(1, 100)  # NOSONAR
    b = random.randint(1, 100)  # NOSONAR
    op = random.choice(operations)  # NOSONAR

    question = f"{a} {op} {b}"
    correct_answer = str(calculate(a, b, op))

    return question, correct_answer