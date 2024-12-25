grade = float(input("What is your percentage grade in your class? "))
# A >= 90
if  grade >=90:
	letter = "A"
# B >= 80
elif  grade >= 80:
	letter = "B"
# C >= 70
elif  grade >= 70:
	letter = "C"
# D >= 60
elif  grade >= 60:
	letter = "D"
# F < 60
else:
	letter = "F"
#+ or -
digit = grade % 10
if digit >=7:
	modifier = "+"
elif digit <=3:
	modifier = "-"
else:
    modifier = ""

if letter.lower()[0] in ["a","e","i","o","u"]:
	preterite = "an"
else:
    preterite = "a"

if grade == "F":
	print(f"You got {preterite} {letter} in the class.")
else:
	print(f"You got {preterite} {letter}{modifier} in the class.")

if grade >= 70:
	print("You have passed this class. Congratulations!")
else:
  print("You Failure. See you next time!")
  