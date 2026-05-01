from brain_games.engine import run_games
from brain_games.games.brain_calc import calc_game


def main():
    game = calc_game
    run_games(game)


if __name__ == "__main__":
    main()
