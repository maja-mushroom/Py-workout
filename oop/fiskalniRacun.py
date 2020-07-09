class Obveznik:

    def __init__(self, jib, naziv, adresa):
        self.jib = jib
        self.naziv = naziv
        self.adresa = adresa 
    
    def __str__(self):
        return self.naziv + ' ' + 'JIB: '+ self.jib
    

class Racun:

    def __init__(self, obveznik):
        self.obveznik = obveznik
        self.nazivRacuna = 'MALOPRODAJNI FISKALNI RACUN'
        self.stavke = []
        self.__totalIznosSaPorezom = 0
        self.__totalIznosBezPoreza = 0
        self.__totalIznosPoreza = 0
    
    
    def __str__(self):
        s = ''
        s = s +'   ' + self.obveznik.naziv + '\n'
        s = s + '   ' + self.obveznik.adresa + '\n'
        s = '\n' + s + '----------------------------' + '\n'
        s = s + self.nazivRacuna + '\n'
        s = '\n' + s + '----------------------------' + '\n'

        for i in self.stavke:
            s = s + i.nazivArtikla + '\n'
            s = s + '\t' + str(i.cijena)+ '\t'
            s = s + str(i.kolicina) + '\t'
            s = s + str(i.ukupnaCijena) + '\n'
        
        s = '\n' + s + '----------------------------' + '\n'

        s = s + 'Total s PDV'+ '\t'+ '\t' + str(round(self.__totalIznosSaPorezom, 2)) + '\n'
        s = s + 'Total bez PDV'+ '\t'+ '\t' + str(round(self.__totalIznosBezPoreza, 2)) + '\n'
        s = s + 'Total iznos PDV'+ '\t'+ '\t' + str(round(self.__totalIznosPoreza, 2))  + '\n'

        s = '\n' + s + '----------------------------' + '\n'
        s = s + 'Ukupno' + '\t'+ '\t' + '\t' + str(self.__totalIznosSaPorezom) + '\n'
        
        return s 
    
    def dodajStavku(self, stavkaRacuna):
        self.stavke.append(stavkaRacuna)
        self.__totalIznosSaPorezom += stavkaRacuna.ukupnaCijenaSaPorezom
        self.__totalIznosBezPoreza += stavkaRacuna.ukupnaCijenaBezPoreza
        self.__totalIznosPoreza += (stavkaRacuna.ukupnaCijenaSaPorezom - stavkaRacuna.ukupnaCijenaBezPoreza)



class StavkaRacuna:

    def __init__(self, nazivArtikla, cijena, kolicina):
        self.nazivArtikla = nazivArtikla
        self.cijena = cijena
        self.kolicina = kolicina
        self.poreskaStopa = 1.17
        self.ukupnaCijena = self.cijena * self.kolicina
        self.ukupnaCijenaBezPoreza = (self.ukupnaCijena / self.poreskaStopa)
        self.ukupnaCijenaSaPorezom = self.ukupnaCijena
    


obveznik1 = Obveznik('123456789', 'Knjizara Kultura', 'Kralja Petra 83')
#print(obveznik1)
racun1 = Racun(obveznik1)
sr1 = StavkaRacuna('Olovka Lakubo', 0.9, 5)
sr2 = StavkaRacuna('Gumica Vozic', 0.5, 1)
racun1.dodajStavku(sr1)
racun1.dodajStavku(sr2)
print(racun1)


