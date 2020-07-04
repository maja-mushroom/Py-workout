class Pravougaonik:

    def __init__(self):
        self.__duzina = 0
        self.__sirina = 0
    
    def postaviSirinu(self, value):
        if value > 20:
            print('Vrijednost je veca od max, i postavljena je na 20.')
            self.__sirina = 20
        elif value <= 0:
            print('Vrijednost manja od dozvoljene je postavljena na 0.1.')
            self.__sirina = 0.1
        else:
            self.__sirina = value
    
    def postaviDuzinu(self, value):
        if value > 20:
            print('Vrijednost je veca od max, i postavljena je na 20.')
            self.__duzina = 20
        elif value <= 0:
            print('Vrijednost manja od dozvoljene je postavljena na 0.1.')
            self.__duzina  = 0.1
        else:
            self.__duzina = value

    def obimPravouganika(self):
        return (2 * self.__sirina) + (2 * self.__duzina)


p1 = Pravougaonik()
p1.postaviSirinu(2)
p1.postaviDuzinu(30)  
print(p1.obimPravouganika()) 
