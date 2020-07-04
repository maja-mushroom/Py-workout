class Osoba:

    def __init__(self, name, lastname):
        #public attributes
        self.name = name
        self.lastname = lastname
        #protected
        self._years = 0
        #private
        self.__ages = 0

person1 = Osoba('Maja', 'Uiux')
#acces
print(person1.name)

#pristup protected atributu
print(person1._years)

#acces to privte attribute (you can't acces to  )
#print(person1.__ages)
#creates forcefully new object which has same name as in line ten
person1.__ages = 6
print(person1.__ages)
