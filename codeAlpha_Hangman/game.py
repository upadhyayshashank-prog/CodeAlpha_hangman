import random
from words import WORDS
from utils import display_word, is_word_guessed

HANGMAN = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]


class HangmanGame:

    def __init__(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong = 6

    def play(self):

        print("\n========== HANGMAN ==========\n")

        while self.wrong_guesses < self.max_wrong:

            print(HANGMAN[self.wrong_guesses])

            print("Word :", display_word(self.word, self.guessed_letters))

            print("Guessed :", " ".join(sorted(self.guessed_letters)))

            guess = input("\nEnter a letter: ").lower().strip()

            if len(guess) != 1 or not guess.isalpha():
                print("Enter one alphabet only.\n")
                continue

            if guess in self.guessed_letters:
                print("Already guessed.\n")
                continue

            self.guessed_letters.add(guess)

            if guess in self.word:
                print("Correct!\n")

                if is_word_guessed(self.word, self.guessed_letters):
                    print(display_word(self.word, self.guessed_letters))
                    print("\nCongratulations! You Won!")
                    return

            else:
                self.wrong_guesses += 1
                print("Wrong Guess!\n")

        print(HANGMAN[self.wrong_guesses])
        print(f"\nGame Over!\nThe word was: {self.word}")