class Osoba:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.weight = 100

    def print(self):
        return self.name + ' ' + self.lastname
    
    def print2(self):
        print(self.name + ' ' + self.lastname)

objekat1 = Osoba('bilja', 'ds')
objekat2 = Osoba('maja', 'uiix')


print('Ime i prezime osobe 1 je: ',objekat1.name, objekat1.lastname,'teska je ',  objekat1.weight)
print('Ime i prezime osobe 2 je: ',objekat2.name, objekat2.lastname, 'teska je ', objekat2.weight)

objekat1.name = 'bibi'
print('novo ime objekta je: ', objekat1.name)

objekat3 = Osoba('Cicko', 'fux')
objekat3.weight = 95
print('Ime i prezime osobe 3 je: ',objekat3.name, objekat3.lastname, 'teska je ', objekat3.weight)

print(objekat1.print())
objekat2.print2()