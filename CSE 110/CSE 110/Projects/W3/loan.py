

loan = int(input("How large is the loan?(1-10)"))
history = int(input("How good is your credit history?(1-10)"))
income = int(input("How high is your income?(1-10)"))
payment = int(input("How large is your down payment?(1-10)"))

is_approved = False

if loan >= 5:
    
    is_approved = True 
    
elif (history >= 7 or income >= 7) and payment >= '5':
    
    is_approved = True 
    
    else:
    
