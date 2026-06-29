def display_word(word, guessed_letters):
    display = []

    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")

    return " ".join(display)


def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word) 
