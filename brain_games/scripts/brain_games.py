from brain_games.engine import run_games

# from brain_games.games.brain_even import even_game
# from brain_games.games.brain_calc import calc_game
from brain_games.games.brain_gcd import gcd_game


def main():
    game = gcd_game
    run_games(game)


if __name__ == "__main__":
    main()
