# books = []

# books.append('Jacob')
# books.append('Enos')
# books.append('Nephi')
# books.append('Alma')

# print(f'The length of your list is {len(looks)}')

# tips_collected = [1.25, 2.50, 1.65, 3.25, 5.00]

# sum = 0

# for tip_amount in tips_collected:
#     sum += tip_amount
    
# print(f'Your total tips for the day are {sum:.2f}')


fruits = ['apple', 'banana', 'cantaloupe','grape', 'lemon']

# for index in range(5):
for index in range(len(fruits)):
    print(f'{index + 1}. {fruits[index]}')

#  for index, fruit in enumerate(fruits):
#     print(f'{index + 1}. {fruit}')

#add a item
# fruits[0] = avacado
#remove an item
# fruits.pop()

# popme = int(input('Which item shall I pop?'))
# fruits.pop(popme)
# fruits.pop(popme - 1)

# fruits.remove('apple')
# print(f'Here is the list: {fruits}')


# fruits.remove('banana')
# print(f'Here is the list again: {fruits}')

# to_remove = input('What fruite shall I remove? ').lower()

# print(fruits)
# while to_remove in fruits:
#     fruits.remove(to_remove)
# print(f'Here is the list again: {fruits}')

# fruits.insert(2, 'zoom_zoom')
# print(f'Here is the modified list: {fruits}')

# fruits = ['apple','banana','cherry', 'grape','lemon']
# to find  = 'apple'
# if to find in fruits:
#     found positioon = fruits.index(to find)
#     print(f'{to find} was found in {fruits} at index {found position}')
# else:
#     print(f'{to find} was not found in {fruits}.')

fruits = ['apple','banana','cherry','grape','lemon']
prices = [1.50, 2.00, 2.50, 3.00, 1.25]

fruits_prices = [['apple', 1.50],['banana',2.00], ['cherry',3.00]]
# for index in range(len(fruits)):
#     print(f'{fruits[index]} sell for ${prices[index]:.2f} per pund.')
    
for index, fruit in enumerate(fruits):
    print(f'{fruit} sells for ${prices[index]:.2f} per pound.')