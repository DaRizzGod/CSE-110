# Bank Account
balances = []
accounts = []

balances = input('What is the amount in this account?')
while balances != 'quit':
  accounts = float(input('What is the amount? '))
  balances.append(balances)
  accounts.append(accounts)
  balances = input("What is the name of this account (quit to exit)?")
  
for index in range (len(balances)):
  print(f' {balances[index]} - ${accounts[index]:.2f}')
  