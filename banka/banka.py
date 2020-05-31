import getpass
import csv

#welcome note
print('\nWelcome, you have just entered in OT bank system!\n')
print('\n')


# #pass check
# p = getpass.getpass(prompt='Enter your valid password? ')
# i=1

# #inp=0
# while i<=2:
#     if p.lower() == 'mica123':
#         print ('Welcome.\n')
#         inp = int(input('Otvaranje racuna - opcija 1\nStanje racuna - opcija 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\n'))
#         break
#     elif p.lower() == 'lazo123':
#         print ('Welcome.\n')
#         inp = int(input('Stanje racuna - opcija 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\nZatvaranje racuna - opcija 6\n'))
#         break
#     elif p.lower() == 'admin123':
#         print ('Welcome.\n')
#         inp = int(input('Otvaranje racuna - opcija 1\nStanje racuna - opcija 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\nZatvaranje racuna - opcija 6\n'))
#         break
#     else:
#         print ('Your password is not valid. Try again!\n')
#         p = getpass.getpass(prompt='Enter your valid password? ')
#         if (p.lower() != 'mica123') or (p.lower() != 'lazo123') or (p.lower() != 'admin123'):
#             print ('You are out of attempts. Your password is not valid.\n')
#             break
#     i+=1

balance = 0
payment = []
payoff = []


# def open_account():
#     account_num = ''
#     account_owner = ''
#     balance = ''
#     date = ''

#     account_owner = input('Enter the user name and last name...\n')
#     owner_jmgb = input('Enter the user JMBG: \n')
#     account_num = input('Enter the user account number: \n')
#     balance = input('Enter the user balance: \n')
#     date = input('Enter the date od openig the account: \n')

#     with open('stanje.csv', "a") as csvfile:
#         csvwriter = csv.writer(csvfile,  delimiter=',')
#         csvwriter.writerow([account_owner, owner_jmgb, account_num , balance, date])
#     return ("Points written sucessfully to file")
# open_account()

# def check_balance(account_n):
#     balance = 0
#     with open('stanje.csv','r') as csvfile:
#         reader = csv.reader(csvfile,delimiter =',')
#         for i in reader:
#             #for j in i:
#                 #print(j)
#             if i[2] == str(account_n):
#                 balance = i[-2]
#         return balance   

# print(check_balance(123456789))


# def deposit(balance):
#     amount_deposit=float(input("The Amount: "))
#     new_balance = balance + amount_deposit
    
#     print("New Amount: ", amount_deposit, '\n' "Total Blance:", new_balance)

# deposit(900)

# def withdraw(balance): 
#     amount_withdraw = float(input("The Amount of withdraw: ")) 
#     if balance >= amount_withdraw: 
#         new_balance = balance - amount_withdraw
#         print("You've just withdraw:", amount_withdraw) 
#         print ("New Total is:" , new_balance)
#     else: 
#         print("There is no enough resources on the account for this transaction! ") 
# print(withdraw(900))

def transfer(account_of_withdraw, account_in_favour, amount_withdraw): 
    new_balance = []
    balance_append =[]
    with open('stanje.csv','r+') as csvfile:
        reader = csv.reader(csvfile,delimiter =',')
        for i in reader:
            new_balance = i
            if i[2] == str(account_of_withdraw):
                balance = i[-2]
                balance = int(balance) - amount_withdraw
                new_balance[-2] = str(balance)
                #with open('stanje.csv','a') as csvfile:
                #csvwriter = csv.writer(csvfile, delimiter =',')
                #csvwriter.writerows([new_balance])
                print('new balance', balance)
            #i = new_balance
            #print(i)
            if i[2] == str(account_in_favour):
                balance = i[-2]
                print(balance)
                balance = int(balance) + amount_withdraw
                balance_append[-2] = str(balance)
                print('in favour', balance)
        csvwriter = csv.writer(csvfile, delimiter =',')
        csvwriter.writerows([new_balance])
        csvwriter.writerows([balance_append])

print(transfer(123456789, 123987654, 9))