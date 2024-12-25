import math

def compute_area_square(side):
	return compute_area_rectangle(side, side)
  
def compute_area_rectangle(side1, side2):
	return side1 * side2
  
def compute_area_circle(radius):
	return radius * radius * math.pi
  
def compute_area(shape, vlaue):
    if shape == 'square':
        return compute_area_square(value)
    elif shape == 'circle':
        return compute_area_circle(value)
    return -1

choice = input("What kind of shape do you have {quit to exit}? ").lower()
while choice != 'quit':
    if choice == 'square':
        side = float(input('What is the lenth of the side of the square? '))
        area = computer_area('square', side)
        print(f'The area is: {area}')
        
choice  = input('What kind of shape do you have (quit to exit)? ').lower()
while choice != 'quit':
    if choice == 'square':
        side = float(input('What is the length of the side of the square? '))
        area = compute_area('square', side)
        print(f'The area is: {area:.2f}')
    elif choice == 'rectangle':
        side1 = float(input('What is the length of the first side of the rectangle? '))
        side2 = float(input('What is the length of the second side of the rectangle? '))
        print(f'The area is {compute_area_rectangle(side1, side2):.2f}')
    elif choice == 'circle':
        radius = float(input('What is the length of the radius of your circle? '))
        print(f'The area is {compute_area('circle', radius):.2f}')
    else:
        print('That is not a valid option. ')
    print()
    choice = input('What kind of shape do you have (quit to exit)? ').lower()
        
