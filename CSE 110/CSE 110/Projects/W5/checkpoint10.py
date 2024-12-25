item_list = []

item = input('What are you adding to your shopping list? ').lower()
while item != 'quit':
    item_list.append(item)
    item = input('What are you adding to your shopping list? ').lower()
    
for item in item_list:
    print(item)

for index in range(len(item_list)):
    print(f'{index}. {item_list[index]}')
    
new_index = int(input('What item do you want to change? '))
new_item = input('What is the new item to your list? ')
item_list[new_index] = new_item
for index in range(len(item_list)):
    print(f'{index}. {item_list[index]}')
    