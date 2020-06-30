class Auto:

    def __init__(self, tip, marka):
        self.tip = tip
        self.marka = marka


auto1 = Auto('GLC', 'Mercedes')
auto2 = Auto('Punto', 'Fiat')
auto3 = Auto('Golf2', 'Volkswagen')

print('Automobil marke ', auto1.marka, 'je tipa ', auto1.tip)
print('Automobil marke ', auto2.marka, 'je tipa ', auto2.tip)
print('Automobil marke ', auto3.marka, 'je tipa ', auto3.tip)