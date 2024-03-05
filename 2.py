account_balance = int(input("enter your account balance: "))
while 1:
    application = input("enter your application: ")
    if application == 'quit':
        break
    elif application == 'deposit':
        n = int(input("enter your amount: "))
        account_balance += n
    elif application == 'withdraw':
        n = int(input("enter your amount: "))
        account_balance -= n
    elif application == 'check':
        print('your account balance is: ',account_balance)
        
