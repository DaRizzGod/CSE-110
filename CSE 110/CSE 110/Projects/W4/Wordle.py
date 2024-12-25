# Compare each letter of the guess word with the letter in the secret word
# If the letter matches add the UPPERCASE letter to the hint
# If the letter doesn't match, check the secret word to see if the guess letter exists
# If the guess letter exists, add the lowercase letter to the hint, otherwise add an underscore

import random

guess = ''
words = ['alma']

word = random.choice(words)

print(f"The random word is {words}")

tries = 0
hint = "_" * len(word)

print("Welcome to the greatest game on earth:Wordle!")
print("\nI'm going to think of a singular word and you have to guess it!")
print("\nGuess correctly in the slots and you live, guess wrong and you go to Mordor!")
print("\nDare to Try?")

while word!= guess:
    
    print('The hint is: ' + hint)
    
    hint = ''
    
    tries += 1
    
    guess = input('The word is ' + str(len(word)) + " letters long. Guess a letter: " + hint)
    
    if len(guess) != 4:
        print("Invalid input. Please enter a single letter.")

    elif (guess) == word:
        print("Correct answer. Please continue onward")
        
        print(tries)
        
    else:
        for temple in range(len(guess)):
            if word [temple] == guess[temple]:
                hint += (guess[temple].upper()) 
            elif guess[temple] in word:
                hint += (guess[temple].lower()) 
            else: hint += ('-')
            
            
print('Thank you for Playing the game!')
        