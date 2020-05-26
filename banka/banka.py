import getpass
import csv

#welcome note
print('\nWelcome, you have just entered in OT bank system!\n')
print('\n')


#pass check
p = getpass.getpass(prompt='Enter your valid password? ')
i=1

#inp=0
while i<=2:
    if p.lower() == 'mica123':
        print ('Welcome.\n')
        inp = int(input('Otvaranje racuna - opcija 1\nUplata na racun - opcija 2\nIsplata sa racuna - opcija 3\nPrenos s jednog na drugi racuna - opcija 4\n'))
        break
    elif p.lower() == 'lazo123':
        print ('Welcome.\n')
        inp = int(input('Uplata na racun - opcija 2\nIsplata sa racuna - opcija 3\nPrenos s jednog na drugi racuna - opcija 4\nZatvaranje racuna - opcija 5\n'))
        break
    elif p.lower() == 'admin123':
        print ('Welcome.\n')
        inp = int(input('Otvaranje racuna - opcija 1\nUplata na racun - opcija 2\nIsplata sa racuna - opcija 3\nPrenos s jednog na drugi racuna - opcija 4\nZatvaranje racuna - opcija 5\n'))
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



def count():
    account_num = ''
    account_owner = ''
    date = ''

    account_owner = input('Enter the user name and last name...\n')
    owner_jmgb = input('Enter the user JMBG: \n')
    date = input('Enter the date od openig the account:\n')


    with open('stanje.csv', "a") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([account_owner, owner_jmgb, date])
    return ("Points written sucessfully to file")
    

if inp == 1:
    count()
    print('status OK')



