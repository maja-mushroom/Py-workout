class Pas:

    def __init__(self, ime, rasa, datum_rodjenja):
        self.ime = ime
        self.rasa = rasa
        self.datum_rodjenja = datum_rodjenja


pas1 = Pas('Cvicko', 'pug', '03.03.2017')
pas2 = Pas('Brmbo', 'patuljasti snaucer', '01.01.2020')

print(pas1.ime, pas1.rasa, pas1.datum_rodjenja)
print(pas2.ime, pas2.rasa, pas2.datum_rodjenja)

