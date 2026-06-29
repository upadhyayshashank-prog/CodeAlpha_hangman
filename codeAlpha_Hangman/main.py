from game import HangmanGame

def main():

    while True:

        game = HangmanGame()

        game.play()

        again = input("\nPlay Again? (y/n): ").lower()

        if again != "y":
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main() 
    