# Alexia 1913 Engineer 84000
# Herman 4266 Manager 106000
# Jay 5849 Engineer 93000
# Ahmad 1326 Tester 85000
# Ciaran 2019 Engineer 62000
# Callum 8005 Engineer 73000
# Samantha 4802 Tester 80000
# Antonio 1423 Tester 51000
# May 5575 CFO 112000
# Sebastian 7378 Scientist 102000
# Kaitlyn 4542 Support 63000
# William 7364 Tester 74000
# Sophie 3437 Engineer 109000
# Isaiah 1518 Designer 58000
# Aimee 8093 CEO 125000
# Patrick 2214 Sales 87000
# Gloria 4414 Designer 79000
# Joseph 9427 Sales 91000
# Barbara 5967 Engineer 104000

# with open('hr_system.txt') as hr_file:
#   for line in hr_file:
#     line = line.strip()
#     hr_data = line.split(",")
#     name = hr_file[0]
#     ID = hr_file[1]
  
# print(f"Name: {hr_data[0]}, Title: {hr_data[2]}")
   
# for line in hr_file:
#         line = line.strip()
#         hr_data = line.split(" ")
#         hr_name = hr_data[0]
#         hr_ID = int(hr_data[1])
#         hr_title = hr_data[2]
#         hr_salary = float(hr_data[3])
#         if hr_title.lower() == "engineer":
#             hr_salary += 1000
#         print(f"{hr_name} (ID: {hr_ID}), {hr_title} - ${hr_salary:.2f}")

# #Jacobs code
with open("hr_system.txt") as hr_file:
    for line in hr_file:
        line = line.strip()
        hr_data = line.split(' ')

        name = hr_data[0]
        ID = hr_data[1]
        job = hr_data[2]
        salary = float(hr_data[3])/24
        if job == "Engineer":
            salary = salary + 1000
            # befor the strech challenges
        # print(f'Name: {name}, Title: {job}')
        print(f"{name} (ID: {ID}), {job} - ${salary:.2f}")
        
# with open('Week 6/hr_system.txt') as hr_info:
#     for info in hr_info:
#         info = info.strip()
#         info = info.split()
#         name = info[0]
#         num = info[1]
#         role = info[2]
#         pay = int(info[3])
#         if role == 'Engineer':
#             print(f'Name: {name:12} ID: {num:10}  Title: {role:12}  ${pay/24+1000:.2f}')
#         else:
#             print(f'Name: {name:12} ID: {num:10}  Title: {role:12}  ${pay/24:.2f}')