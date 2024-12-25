numbers = [3,7,2,9,4]
max_number = -9999999


for number in numbers:
    print(f'Looking at numbers: {number}')
    if number > max_number:
        max_number = number
    print(f'The current max number is {max_number}')
    
print(f'The largesst number in the list is {max_number}')

numbers = [3,7,2,9,4]
min_number = 99999

for umber in numbers:
    print(f'Looking at number: {number}')
    if number < min_number:
        min_number = number
    print(f'The current min number is {min_number}')
    
print(f'The smallest number in the list is {min_number}')