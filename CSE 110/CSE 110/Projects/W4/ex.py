# Word Guessing Game
# Computer picks a random word
# Player tries to guess it
# Computer only responds with yes or no

import random

# List of words
words = ["python", "jumble", "hide", "mama"]

# Pick a random word
word = random.choice(words)

# Initialize the number of tries and the hint
tries = 0
hint = "_" * len(word)

# Welcome message
print("Welcome to the word game!")
print("\nI'm going to think of a word and you have to guess it!")
print("\nGuess which letters are in the word, then you have to guess the whole thing!")
print("\nGood luck!")

# Main loop
while tries < 5:
    # Ask the player to guess a letter
    guess = input("The word is " + str(len(word)) + " letters long. Guess a letter: ")

    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Check if the guess is correct
    if guess in word:
        print("Good job! The letter " + guess + " is in the word.")
        # Update the hint with the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                hint = hint[:i] + guess.upper() + hint[i+1:]
    else:
        print("Sorry, the letter " + guess + " is not in the word.")
        # Update the hint with the wrong letter
        hint = hint + " " + guess.lower()

    # Show the hint
    print("The hint is: " + hint)

    # Increment the number of tries
    tries += 1

# Ask the player to guess the word
final = input("Try to guess the word: ")

# Check if the final guess is correct
if final == word:
    print("Amazing! You guessed the word " + word + "!")
else:
    print("Sorry. The word was " + word + ". Better luck next time!")

# Exit message
input("\n\nPress enter to exit")

