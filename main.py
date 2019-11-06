"""This is the main module"""

from helpers import parse
from game import Game

def main():
    args = parse()
    game = Game(args)
    game.run()

if __name__ == "__main__":
    main()
