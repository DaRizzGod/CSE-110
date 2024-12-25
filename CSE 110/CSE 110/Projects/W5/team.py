#Compute the sum, or total, of the numbers in the list.

#Compute the average of the numbers in the list.

#Find the maximum, or largest, number in the list.

numbers = []
number = 1
sum = 0
closet_to_number = 0

while number != 0:
	number = float(input("Please enter the numbers here, type 0 when done: "))
	numbers.append(number)
	
number = number -1
for number in numbers:
	sum += number


length_list = len(numbers) - 1
ave = sum / length_list

for number in numbers:
    for closest_to_number in numbers:
        if number > 0 and closest_to_number > number:
            number_0 = number
print(number_0)


print(sum)
print(ave)	



