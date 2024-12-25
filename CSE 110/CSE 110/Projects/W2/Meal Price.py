#Determine the meal's subtotal (before adding sales tax) 
#by multiplying the number of children by the price of their meal,
#and multiplying the number of adults by the price of their meal
#and adding those two values together.
import math

X= float(input(f'The price of a childs meal'))
print('Your Total:, ' + str(X))
Y= float(input(f'The price of an adults meal'))
print('Your Total:, ' + str(Y))
Z= int(input(f'The number of children'))
print('You have:, '+ str(Z))
A= int(input(f'The number of adults'))
print('You have:, '+ str(A) )
B= float(input(f'The sales tax rate'))
print('Your Total:, ' + str(B))

print(X*Z)
print(Y*A)
subtotal= X*Z + (Y*A)
tax= B/100*subtotal
total= tax + subtotal
print(total)
print(subtotal)

