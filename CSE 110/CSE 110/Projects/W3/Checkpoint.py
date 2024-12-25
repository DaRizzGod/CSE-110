if input("The number is greater!") == "YAY!":
    print ("The number is greater")

number_1 = int(input("Enter a whole numnber: "))
number_2 = int(iinput('Enter a another whole number: '))

if number_1 > number_2:
    print("The first number is greater")
else:
    print("The first number is not greater")

if number_1 == number_2:
    print("The numbers are equal")
else:
    print("The number are not equal")

favorite_animal = "horse"

guess = input("What is your favorite animal? ").lower()
if favorite_animal == guess:
     print("That's my favorite animal too!")
else:
    print("That is not my favorite animal")
