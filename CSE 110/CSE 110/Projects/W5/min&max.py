num_list = [2, 5, 6, 1, 9, 3]

#min num
min_num = 0
for num in num_list:
    if num < min_num:
        min_num =num
print(f'with out min function {min_num}')

#max num
max_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
print(f'with out man function {max_num}')

