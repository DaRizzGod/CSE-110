# Add a new item

# Display the contents of the shopping cart

# Remove an item (only needed for the final project deliverable)

# Compute the total (only needed for the final project deliverable)

# Quit
items = []
price = []
shop = ''
print('Welcome to Walley World!')
while shop != '5':
    
    print('1. Add item')
    print('2.View cart')
    print('3.Remove item')
    print('4.Compute total')
    print('5.quit')
    shop = input('Please enter an action:')
        
    if shop == '1':
            
        toappend = input('What item shall I add? ')
        total = float(input('What is the price of the item? '))
        items.append(toappend)
        price.append(total)

    elif shop == '2':
        print(f'\nHere is the modified list:')
        index= 0
        for item in items:
            print(f"{index + 1} {item} {price:.2f[index]}")
            index =+ index +1
            
    elif shop == '3':
        index = 0
        for item in items:
            print(f"{index + 1} {item} {price:.2f[index]}")
            index =+ index +1
        to_remove = int(input('What item shall I remove? '))
        items.pop(to_remove -1)
        price.pop(to_remove -1)
        print('Item removed')
    elif shop == '4':
        total = 0
        for every_price in price:
            total += every_price  
        print(f'\nThe total price of items is: ${total:.2f}')

    elif shop == '5':
            print('Thank you for shopping with us, Have a terrible day!')

