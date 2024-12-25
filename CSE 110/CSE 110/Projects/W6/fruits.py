fruit_file =open('fruits.txt')

# fruit_file.close()

# with open('fruits.txt') as fruit_file:
#     print('File is now open.')
# print('File is now closed.')

# with open ('C:/Users/miles/Desktop/CSE 110/Projects/W6/fruits.py') as fruit_file:
#     print('Found it!.')

# with open('fruits.txt') as fruit_file:
#     for line in fruit_file:
#         print(line)

# with open('fruits.txt') as fruit_file:
#     for line in fruit_file:
#         line = line.strip()
#         print(line)

with open('fruits.txt') as fruit_file:
    for line in fruit_file:
        line = line.strip()
        fruit_data = line.split(',')
        print(fruit_data)


# with open('fruits.txt') as fruit_file:
#     for line in fruit_file:
#         line = line.strip()
#         fruit_data = line.split(',')
        furit_name = fruit_data[0]
        fruit_cost = float(fruit-data[2])
        print(f'{fruit_name} comes from {fruit_origin} and cost ${fruit_cost:.2f} per pound')
        
# with open('fruits.txt') as fruit_file:
#     fruit,file.readline()
#     for line in fruit_file:
#         line = line.strip()
#         fruit_data = line.split(',')
#         fruit_name = fruit_data[0]
#         fruit_cost = float(fruit_data[2])
#         print(f'{fruit_name} costs ${fruits_cost:.2f} per pound')        
        

