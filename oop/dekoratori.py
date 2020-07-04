'''
@property decortor;
'''

class TekuciRacun:

    def __init__(self):
        self.__stanje = 0

    @property
    def stanje(self):
        return self.__stanje
    
    @stanje.setter
    def stanje(self, vrijednost):
        self.__stanje = vrijednost

racun = TekuciRacun()

print(racun.stanje)

racun.stanje = 34

print(racun.stanje)