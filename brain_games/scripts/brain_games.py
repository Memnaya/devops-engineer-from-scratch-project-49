from brain_games.engine import run_game
from brain_games.scripts.brain_even import description, game_logic


def main():
    run_game(description, game_logic)

    if __name__ == "__main__":
        main()
