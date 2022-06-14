from phrasehunters import game
from phrasehunters import phrase

if __name__ == '__main__':
    restart = True
    while restart:
        play_game = game.Game()
        play_game.start()
        play_again = input("\nWould you like to play again? (Y/N) ")
        if play_again.lower() == 'y':
            restart = True
        else:
            restart = False