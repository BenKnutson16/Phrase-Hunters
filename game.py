import random
from phrase import Phrase

class Game:
    def __init__(self):
        self.lives = 5
        self.phrases = [Phrase('shot in the dark'), Phrase('needle in a haystack'), Phrase('piece of cake'), Phrase('walk in the park'), Phrase('can of worms')]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']
    
    def start(self):
        self.welcome()
        while (self.lives > 0) and (not self.active_phrase.check_complete(self.guesses)):
            print("Number of guesses remaining: {}".format(self.lives))
            user_guess = self.get_guess()
            if (not self.active_phrase.check_letter(user_guess)) or (user_guess in self.guesses):
                self.lives -= 1
            self.guesses.append(user_guess)
            self.active_phrase.display(self.guesses)
        self.game_over()
        
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("Welcome to phrase hunters!")
        
    def get_guess(self):
        guess = input("Please enter your guess: ")
        while (len(guess) > 1) or (not guess.isalpha()):
            guess = input("That's not a valid guess. Please enter a letter: ")
        return guess.lower()
    
    def game_over(self):
        if self.lives <= 0:
            print("You Lose!")
        else:
            print("Congratulations! You win!")