import json

isCode = False
isRun = True

def account(isDeposit):
    accCode = input("Please enter your account code: ").upper()
    with open("data.json", mode="r") as file:
        accounts = json.load(file)
    if any( True for i in range(0, len(accounts)) if accCode in accounts[i]['code']):
        for i in range(0, len(accounts)):
            selectedAcc = accounts[i]
            if accCode in selectedAcc['code']:
                previousBal = selectedAcc['balance']
                
                if isDeposit == True:
                    while True:
                        try:
                            accDeposit = float(input('Please enter your amount to deposit: '))
                            accounts[i]['balance'] += accDeposit
                            with open("data.json", "w") as jsonFile:
                                json.dump(accounts, jsonFile)
                            print(f"Successfully deposit of {accDeposit}RS into your account - {accCode}.\n")
                            break
                        except ValueError:
                            print("Please enter number only")
                
                elif isDeposit == False:
                    while True:
                        try:
                            accWithdraw = int(input('Please enter your amount to withdraw: '))
                            
                            if previousBal != 0 and accWithdraw <= previousBal: 
                                accounts[i]['balance'] -= accWithdraw
                                with open("data.json", "w") as jsonFile:
                                    json.dump(accounts, jsonFile)
                                print(f"Successfully withdraw of {accWithdraw}RS into your account - {accCode}.\n")
                                break
                            else:
                                print(f"insufficient balance - {previousBal}RS \n\n")
                                return None
                        except ValueError:
                            print("Please enter number only")
                else:    
                    return selectedAcc
                break
    else:
        print(f"{accCode} account not found or", end=" ")
        print("Create a new account, Type 'CREATE' \n\n")
        return None

print('==========================')
print('=   Bank of Programmer   =')
print('==========================')

print("Welcome to our bank")

while True:
    print()    
    print("Hello, If you need any help, type 'HELP'")
    userInput = input("What service can I offer: ").upper()
    print()

    if userInput == 'HELP':
        print("i.   For Create a new account, type 'CREATE' ")
        print("ii.  For Deposit, type 'DEPOSIT' ")
        print("iii. For Withdraw, type 'WITHDRAW' ")
        print("iv.  Check account balance, type 'BALANCLE' ")
        print("v.   Shutdown system, Type 'CLOSE'\n")

    elif userInput == 'CREATE':
        print("For create a new account, provide your name. \n")

        while True:
            AccName = input("Enter your name: ")
            if any(char.isdigit() for char in AccName):
                print("Please do not include digits in your name.")
            else:
                break

        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                genCode = str(len(data)+1)
                AccCode = f'ACC00{genCode}'

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                accounts = []
                json.dump(accounts, file, indent=2)
            
            with open("data.json", mode="r") as file:
                data = json.load(file)
                genCode = str(len(data)+1)
                AccCode = f'ACC00{genCode}'
        
        finally:
            detail = {
                    'code': AccCode,
                    'name': AccName,
                    'balance': 0.0
                }
            data.append(detail)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=2)
  

        print("Your account is created successfully.")
        print(f" This is your account name - {AccName} and your account code - {AccCode}\n")
        print('*******Thank you*******\n\n')

    elif userInput == 'DEPOSIT':
        print("********DEPOSIT******** \n")
        isCode = True
        while isCode:
            isDeposit = True
            detail = account(isDeposit)
            if detail is not None or detail == None:
                isCode = False            

    elif userInput == 'WITHDRAW':
        print("********WITHDRAW********\n")
        isCode = True
        while isCode:
            isDeposit = False
            detail = account(isDeposit)
            if detail is not None or detail == None:
                isCode = False    

    elif userInput == 'BALANCE':
        isDeposit = None
        selectAccDetail = account(isDeposit)
        name = selectAccDetail['name']
        balance = selectAccDetail['balance']
        print(f"Account holder name: {name} \nAccount balance: {balance}RS")

    elif userInput == 'CLOSE':
        print("System is shutdown.")
        break
    else:
        print("Please provide right input.\n\n")
    
