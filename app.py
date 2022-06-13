from game import Game
from phrase import Phrase

if __name__ == '__main__':
    restart = True
    while restart:
        game = Game()
        game.start()
        play_again = input("Would you like to play again? (Y/N)")
        if play_again.lower() == 'y':
            restart = True
        else:
            restart = False