import getpass
import csv

#welcome note
print('\nWelcome, you have just entered in OT bank system!\n')
print('\n')


# creates new account and writs values in two files stanje.csv and transakcije.log
# input var account_num - str, accout_owner - str, owner_jmbg - str, date - str
def open_account(account_num, account_owner, owner_jmgb, balance, date):

    with open('stanje.csv', "a") as csvfile:
        csvwriter = csv.writer(csvfile,  delimiter=',')
        csvwriter.writerow([account_owner, owner_jmgb, account_num , balance, date])
    print("New user has been entered sucessfully")

    with open('transkacije.log', 'a') as t_file:
        t_file.write('New user Created: ')
        t_file.write('First Name and Last Name: %s,' % account_owner)
        t_file.write('Owner JMBG:%s,' % owner_jmgb)
        t_file.write('Account Number:%s,' % account_num)
        t_file.write('%s,' % balance)
        t_file.write('%s' % date)
        t_file.write('\n') 


#checks users balance and writes values in two files stanje.csv and transakcije.log
# input var account_number - str, account_owner - str
def check_balance(account_number, account_owner):
    balance = 0
    with open('stanje.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter =',')
        for i in reader:
            #for j in i:
                #print(j)
            if i[2] == str(account_number) and i[1] == account_owner:
                balance = i[-2]
        print('User balance: ', balance) 


# account deposit and writes values in two files stanje.csv and transakcije.log
#input var account_number - str, amount - str
def deposit(account_number, amount):
    new_balance = []
    all_ = []
    with open('stanje.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        for i in reader:
            if i[2] == str(account_number):
                new_balance = i
                balance = i[-2]
                new_balance[-2] = str(int(balance) + amount)
                all_.append(new_balance)
                with open('transkacije.log', 'a') as t_file:
                    t_file.write('Amount of Deposite: %s,' % amount)
                    t_file.write('Total Blance:%s,' % new_balance[-2])
                    t_file.write('%s,' % new_balance[0])
                    t_file.write('%s' % new_balance[1])
                    t_file.write('\n')   
            else:
                all_.append(i)
    with open('stanje.csv','w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter =',')
        for i in all_:
            csvwriter.writerow(i) 


#account withdraw and writes values in two files stanje.csv and transakcije.log 
# input account_number - str, amount_of_withdraw - str
def withdraw(account_number, amount_of_withdraw): 
    new_balance = []
    all_ = []
    with open('stanje.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter =',')
        for i in reader:
            if i[2] == str(account_number):
                new_balance = i
                balance = i[-2]
                if int(balance) >= amount_of_withdraw: 
                    new_balance[-2] = str(int(balance) - amount_of_withdraw)
                    all_.append(new_balance)
                    print("You've just withdraw:", amount_of_withdraw) 
                    print ("New Total is:" , new_balance[-2])
                    with open('transkacije.log', 'a') as t_file:
                        t_file.write('Amount of Withdraw: %s,' % amount_of_withdraw)
                        t_file.write('Total Blance:%s,' % new_balance[-2])
                        t_file.write('%s,' % new_balance[0])
                        t_file.write('%s' % new_balance[1])
                        t_file.write('\n') 
                else:
                    with open('transkacije.log', 'a') as t_file:
                        t_file.write('There is no enough resources on the account for this transaction!,')
                        t_file.write('Total Blance:%s,' % new_balance[-2])
                        t_file.write('%s,' % new_balance[0])
                        t_file.write('%s' % new_balance[1])
                        t_file.write('\n')  
                    print("There is no enough resources on the account for this transaction! ")
            else:
                all_.append(i)        
    with open('stanje.csv','w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter =',')
        for i in all_:
            csvwriter.writerow(i)


#account transfer from one to another and writes values in two files stanje.csv and transakcije.log 
#input var account_of_withdraw - str, account_in_favour - str, amount_withdraw - str
def transfer(account_of_withdraw, account_in_favour, amount_withdraw): 
    new_balance = []
    balance_append =[]
    all_ =[]
    with open('stanje.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter =',')
        for i in reader: 
            if i[2] == str(account_of_withdraw):
                new_balance = i
                balance = i[-2]
                balance = int(balance) - amount_withdraw
                new_balance[-2] = str(balance)
                all_.append(new_balance)
                print('new balance', balance)

            elif i[2] == str(account_in_favour):
                balance_append = i
                balance = i[-2]
                balance = int(balance) + amount_withdraw
                balance_append[-2] = str(balance)
                print('in favour', balance_append[-2])
                all_.append(balance_append)
            else:
                all_.append(i)
    with open('stanje.csv','w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter =',')
        for i in all_:
            csvwriter.writerow(i)
    

    with open('transkacije.log', 'a') as t_file:
        t_file.write('Amount of Transfer: %s,' % amount_withdraw)
        t_file.write('Total Balance:%s,' % new_balance[-2])
        t_file.write('%s,' % new_balance[0])
        t_file.write('%s,' % new_balance[1])

        t_file.write('Acount in Favour: %s,' % account_in_favour)
        t_file.write('New Balance:%s,' % balance_append[-2])
        t_file.write('%s,' % balance_append[0])
        t_file.write('%s' % balance_append[1])
        t_file.write('\n')


#menu
# input inp - str
def menu(inp):
    if int(inp) == 1:
        print('Open Account')
        account_owner = input('First Name and Last Name:')
        owner_jmgb = input('Owner JMBG:')
        account_num = input('Account NUmber: ')
        balance = input('Account Balance: ')
        date = input('Date of opening')
        open_account(account_num, account_owner, owner_jmgb, balance, date)

    elif int(inp) == 2:
        print('Account Balance')
        account_number = input('Account Number: ')
        account_owner = input('First Name and Last Name: ')
        check_balance(account_number, account_owner)
    
    elif int(inp) == 3:
        print('Account Deposit')
        account_number = input('Account Number: ')
        account_owner = input('First Name and Last Name: ')
        amount = input('Enter amount: ')
        deposit(account_number, amount)
    
    elif int(inp) == 4:
        print('Account Withdraw')
        account_number = input('Account Number: ')
        account_owner = input('First Name and Last Name: ')
        amount = input('Enter amount: ')
        withdraw(account_number, amount)
    
    elif int(inp) == 5:
        print('Account Transfer')
        account_of_withdraw = input('Account Number of Withdraw: ')
        account_owner = input('First Name and Last Name of User of withdraw: ')
        amount_withdraw = input('Enter amount: ')
        account_in_favour = input('First Name and Last Name of User in favour: ')
        transfer(account_of_withdraw, account_in_favour, amount_withdraw)

    elif inp == 'q':
        print('Goodbuy.')


#menu for pass check
p = getpass.getpass(prompt='Enter your valid password? ')
i=1

inp=0
while i<=2:
    if p.lower() == 'mica123':
        print ('Welcome.\n')
        while inp != 'q':
            inp =input('Otvaranje racuna - opcija 1\nStanje racuna - opcija 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\nIzlazak - opcija q\n')
            menu(inp)
            break
    elif p.lower() == 'lazo123':
        print ('Welcome.\n')
        while inp != 'q':
            inp = int(input('Stanje racuna - opcija 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\nZatvaranje racuna - opcija 6\n'))
            menu(inp)
            break
    elif p.lower() == 'admin123':
        print ('Welcome.\n')
        while inp != 'q':
            inp = int(input('Otvaranje racuna - opcija 1\nStanje racuna - opcija 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\nZatvaranje racuna - opcija 6\n'))
            menu(inp)
            break
    else:
        print ('Your password is not valid. Try again!\n')
        p = getpass.getpass(prompt='Enter your valid password? ')
        if (p.lower() != 'mica123') or (p.lower() != 'lazo123') or (p.lower() != 'admin123'):
            print ('You are out of attempts. Your password is not valid.\n')
            break
    i+=1


