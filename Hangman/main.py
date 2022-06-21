# This is a main file to run the Hangman

# Imports
import random
from hangman_words import word_list
from hangman_art import stages, logo


# Print the LOGO
print(f"{logo}")

# Maximum chances for guess
lives = 6

# Randomly chose the word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create an empty list which will have "_"
display = []
for char in range(word_length):
    display += "_"

# Game logic
while "_" in display and lives != 0:

    # Display the guesses
    print(f"\nWord to be guessed {''.join(display)}")

    # User input to guess a word
    guess = input("Guess a letter : ").lower()


    # Guessed already ?
    if guess in display:
        print(f"\nYou've already guessed {guess}, Try again :)")

    # Wright guess logic
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Wrong guess logic
    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou have {lives} lives remaining !\n{stages[lives]}")
        if lives == 0:
            print(f"\nSorry you lost :( \nThe word is {chosen_word}")
            exit()

# Print the final result
print("\nYou win :)")
