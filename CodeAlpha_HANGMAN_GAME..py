import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'software']
    word = random.choice(words)
    guessed_letters = set()
    display_word = ['_'] * len(word)
    max_incorrect_guesses = 6
    incorrect_guesses = 0

    print("Welcome to Hangman Game!")

    while incorrect_guesses < max_incorrect_guesses and '_' in display_word:
        print(" ".join(display_word))
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Enter a single letter:")
            continue

        if guess in guessed_letters:
            print("Already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            display_word = [guess if letter == guess else dw for letter, dw in zip(word, display_word)]
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess. {max_incorrect_guesses - incorrect_guesses} guesses left.")
    
    if '_' not in display_word:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
