import random

def hangman():
    # List of words to guess from
    words = ["python", "hangman", "challenge", "programming", "developer"]
    word_to_guess = random.choice(words).lower()
    guessed_word = ["_" for _ in word_to_guess]
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman! Can you guess the word?")

    while attempts > 0 and "_" in guessed_word:
        print("\nCurrent word:", " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        if guessed_letters:
            print(f"Letters guessed so far: {', '.join(sorted(guessed_letters))}")
        else:
            print("No letters guessed yet.")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter just one alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try something else.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Nice! '{guess}' is in the word.")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Oops! '{guess}' isn't in the word.")
            attempts -= 1

    if "_" not in guessed_word:
        print("\nHooray! You guessed the word:", word_to_guess)
    else:
        print("\nOut of attempts! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
