import prompt

from brain_games.engine import run_games
from brain_games.games.brain_calc import calc_game
from brain_games.games.brain_even import even_game
from brain_games.games.brain_gcd import gcd_game
from brain_games.games.brain_prime import prime_game
from brain_games.games.brain_progression import progression_game

GAMES = {
    "even": even_game,
    "calc": calc_game,
    "gcd": gcd_game,
    "progression": progression_game,
    "prime": prime_game,
}


def start_cli():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    
    print("\nAvailable games:")
    for game in GAMES:
        print(f"- {game}")

    game_name = prompt.string("\nSelect game: ")

    if game_name not in GAMES:
        print("Unknown game")
        return

    run_games(GAMES[game_name], name)
