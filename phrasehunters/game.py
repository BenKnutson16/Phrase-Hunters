import random
from phrasehunters import phrase

class Game:
    def __init__(self):
        self.lives = 5
        self.phrases = [
            phrase.Phrase('shot in the dark'),
            phrase.Phrase('needle in a haystack'),
            phrase.Phrase('piece of cake'),
            phrase.Phrase('walk in the park'),
            phrase.Phrase('can of worms')
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']
        self.incorrect = []
    
    def start(self):
        self.welcome()
        while (self.lives > 0) and (not self.active_phrase.check_complete(self.guesses)):
            print("Number of guesses remaining: {}\n".format(self.lives))
            user_guess = self.get_guess()
            if (not self.active_phrase.check_letter(user_guess)) or (user_guess in self.guesses):
                self.lives -= 1
                self.incorrect.append(user_guess)
            self.guesses.append(user_guess)
            self.active_phrase.display(self.guesses)
            print("\nIncorrect guesses: " + (', '.join(self.incorrect)).upper())
        self.game_over()
        
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("\nWelcome to phrase hunters!\nTry to guess the phrase:\n")
        self.active_phrase.display(self.guesses)
        
    def get_guess(self):
        guess = input("Please enter your guess: ")
        print()
        while (len(guess) > 1) or (not guess.isalpha()):
            guess = input("That's not a valid guess. Please enter a letter: ")
        return guess.lower()
    
    def game_over(self):
        if self.lives <= 0:
            print("You Lose!")
        else:
            print("Congratulations! You win!")