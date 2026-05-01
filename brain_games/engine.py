from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_games(game):
    description, game_logic = game()

    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(description)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_logic()

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")