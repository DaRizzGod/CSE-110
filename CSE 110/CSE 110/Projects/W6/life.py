largest_country = ''
largest_case = -99999999999
largest_year = ''

smallest_country = ''
smallest_case = 9999999999
smallest_year = ''

max_age_country = ''
max_age_case = -9999999999

min_age_country = ''
min_age_case = 99999999999
age_sum = 0
age_count = 0

sickness = input(f'Enter the year of interest:{largest_year}')

with open('life-expectancy.csv') as file:
    lines = file.readlines()
    lines = lines[1:]
    for line in lines:
        stripped_line = line.strip()
        split_line = stripped_line.split(',')
        
        year = split_line[2]
        country = split_line[0]
        case = split_line[3]
        
        if largest_case < float(case):
            largest_country = country
            largest_case = float(case)
            largest_year = year
            
        if smallest_case > float(case):
            smallest_country = country
            smallest_case = float(case)
            smallest_year = year
        
        if sickness == year:
            age_sum += float(case)
            age_count +=1 
            if max_age_case < float(case):
                largest_country = country
                largest_case = float(case)
                
            if sickness == year:
                age_sum += float(case)
                age_count -1
                if min_age_case < float(case):
                    smallest_country = country
                    smallest_case = float(case)
            
            if min_age_case > float(case):
                smallest_case = float(case)
                smallest_year = year
            
         
                
            
        
        

age_average = age_sum/age_count            
print(f'The overall max life expectancy is: {largest_case} from {largest_country} in {largest_year}')
print(f'The overall min life excpectancy is: {smallest_case} from {smallest_country} in {smallest_year}')
        
print(f'For the year {sickness}')

print(f'The average life expectancy across all the countries was {age_average}')
print(f'The min life expectancy was in {smallest_country} with {smallest_case}')
print(f'The min life expectancy was in {largest_country} with {largest_case}')

        
