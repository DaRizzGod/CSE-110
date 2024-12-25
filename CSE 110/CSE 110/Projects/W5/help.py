# Initialize the shopping cart and the total
items = []
total = 0

# Define a dictionary with prices for each item
prices = {"Fruit": 1.5, "Vegetables": 2.0, "Broth": 1.0, "Socks": 5.0, "Juice": 3.0}

# Add items to the shopping cart
items.append("Fruit")
items.append("Vegetables")
items.append("Broth")  
items.append('Socks')

# Display the contents of the shopping cart
for index, item in enumerate(items):
    print(f'{index + 1}. {item}')  # print each item, not the whole list

# Add a new item
items.insert(3, 'juice')
print(f'Here is the modified list: {items}')

# Update the total
for item in items:
    if item in prices:
        total += prices[item]

print(f'The total cost of the items in the cart is: ${total:.2f}')

# Remove an item
to_remove = input('What item shall I remove? ').lower()
if to_remove in items:
    items.remove(to_remove)  # remove the item user specified
    total -= prices[to_remove]  # update the total
else:
    print(f'{to_remove} is not in the list.')
print(f'Here is the list again: {items}')
print(f'The updated total cost of the items in the cart is: ${total:.2f}')

