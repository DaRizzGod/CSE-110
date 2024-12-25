# import random

# number = random.randint(1, 10)

# while number > 1:
#     number = int(input("Your guess is too low, try again: "))
#     if number < 10:
#   	    int(input("Your guess is too high, guess again: "))

# print(f'The number is {number}')

# answer = input("what is the magic number? ")
# while guess != 'yes':
  
#     print(f" You got it the number is {number}")


import random

number = random.randint(1, 10)
print(number)

count = 1

guess = int(input("what is the magic number? "))
while guess != number:
		if number < guess:
  			int(input("Your guess is too high, guess again: "))
    count = count + 1
  	else number > guess:
      count = count + 1
int(input("your guess is too low, guess again:"))
print(f" You got it the number is {number}")
print(f" This took you {count} guesses. ")