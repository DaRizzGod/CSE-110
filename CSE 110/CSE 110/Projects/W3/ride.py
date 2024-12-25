#Prompt the user for the age and height of the first person. 
#Then, ask whether there is a second rider, and if so, ask for their age and height.

# person1_height = float(input("What your height (in)? "))
# person1_age = int(input("What is your age? "))

# if person1_height <= 36:
# 	print("I'm not sorry, you may not ride this ride. ")

# else:
# #Handle the case of a single rider.
# person2_bool = input("Is there a second rider?(yes/no) ").lower()

# if person2_bool == "yes":
# 	person2_height = float(input("What is your height (in)? "))
#     person2_age = int(input("What is your age? "))
    
#     if person2_age >= 18 or person1_age >= 18:
#     	print("Congratulations, you may ride the ride!" )
    
# elif person2_bool == "no":
# 	if person1_height >= 62 and person1_age >= 18:
#     	print("Congratulations! You arrived at your destination. Enjoy! ")
        
#     elif person1_height <= 62 or person1_age <= 18:
#     	print("Bye Buddy! Hope you find another rider! ")



# Finish implementing the basic rules.





# #For the stretch goal:
#     elif person1_age  >= 12 and person2_age  >= 12 and person1_height >= 52 and person2_height >= 52 :
#         print("You may ride!")

#  elif person1_age >= 16 and person2_age >= 14 and person1_age <=18 and person2_age <= 18:
#     	print("Welcome to your DOOM!")
     
proceed = True

while proceed:
    desire  = input("Do you want to continue? (Y/N) ")
    if desire != 'Y' or desire != 'yes':
        proceed = False
    print(story)