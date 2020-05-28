import getpass
import csv

#welcome note
print('\nWelcome, you have just entered in OT bank system!\n')
print('\n')

"""
#pass check
p = getpass.getpass(prompt='Enter your valid password? ')
i=1

#inp=0
while i<=2:
    if p.lower() == 'mica123':
        print ('Welcome.\n')
        inp = int(input('Otvaranje racuna - opcija 1\nStanje racuna 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\n'))
        break
    elif p.lower() == 'lazo123':
        print ('Welcome.\n')
        inp = int(input('Uplata na racun - opcija 1\nStanje racuna 2\nIsplata sa racuna - opcija 3\nPrenos s jednog na drugi racuna - opcija 4\nZatvaranje racuna - opcija 5\n'))
        break
    elif p.lower() == 'admin123':
        print ('Welcome.\n')
        inp = int(input('Otvaranje racuna - opcija 1\nStanje racuna 2\nUplata na racun - opcija 3\nIsplata sa racuna - opcija 4\nPrenos s jednog na drugi racuna - opcija 5\nZatvaranje racuna - opcija 6\n'))
        break
    else:
        print ('Your password is not valid. Try again!\n')
        p = getpass.getpass(prompt='Enter your valid password? ')
        if (p.lower() != 'mica123') or (p.lower() != 'lazo123') or (p.lower() != 'admin123') :
            print ('You are out of attempts. Your password is not valid.\n')
            break
    i+=1

balance = 0
payment = []
payoff = []



def open_account():
    account_num = ''
    account_owner = ''
    date = ''
    number = ''
    balance = ''

    account_num = input('Enter the user name and last name...\n')
    account_owner = input('Enter the user JMBG: \n')
    number = input('Enter the user account number: \n')
    date = input('Enter the date od openig the account:\n')
    balance = input('User balance: \n')


    with open('stanje.csv', "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([account_num,account_owner,date,number,balance])
    return ("Points written sucessfully to file")
"""
def check_balance(account_n):
    balance = 0
    with open('stanje.csv','r') as csvfile:
        reader = csv.reader(csvfile,delimiter =',')
        for i in reader:
            for j in i:
                #print(j)
                if j == str(account_n):
                    balance = i[-1]
        return balance   
print(check_balance(39394858483))

    

if inp == 1:
    open_account()
    print('status OK')



