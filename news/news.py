import csv
import random
import os

here = os.path.dirname(os.path.abspath(__file__))
filename_i = os.path.join(here,"izlaz.txt")
csv_ulaz = open("ulaz.csv")
csv_fraze = open("phrases.csv")
csv_fraze1 = csv.reader(csv_fraze, delimiter =",")
with open("ulaz.csv") as f:
    reader = csv.reader(f)
    chosen_row = list(reader)
    next(csv_ulaz)

#ova funkcija nam sve fraze po tipu vraca u liste koje koristimo dalje za random odabir
#ulazi nam lista fraza (csv_file)
#izlazi nam lista fraza po tipu i slucajnom odabiru fraza

def fraze_random(csv_fraze1):
    fraze1 = []
    fraze2 = []
    fraze3 = []
    fraze4 = []
    fraze5 = []
    fraze6 = []

    for row1 in csv_fraze1:
        if row1[0] == "1":
            fraze1.append(row1[1])    
        if row1[0] == "2":
            fraze2.append(row1[1])    
        if row1[0] == "3":
            fraze3.append(row1[1])
        if row1[0] == "4":
            fraze4.append(row1[1])
        if row1[0] == "5":
            fraze5.append(row1[1])
        if row1[0] == "6":
            fraze6.append(row1[1])
        
    random1 = random.choice(fraze1)
    random2 = random.choice(fraze2)
    random3 = random.choice(fraze3)
    random4 = random.choice(fraze4)
    random5 = random.choice(fraze5)
    random6 = random.choice(fraze6)
    return random1,random2,random3,random4,random5,random6

#ova funkacija nam vraca broj novozarazneih
#ulazi nam lista sa ukupnim brojem zarazenih
#izlaz je broj koji predstavlja novozarazene


def racuna(ukupnoZarazenih):
    ukupnoZarazenih = [] 
    for col in csv_ulaz:
        ukupnoZarazenih.append(col[15:18])
    brojNovozarazenih = []
    for i in range(1,len(ukupnoZarazenih)):
        x = int(ukupnoZarazenih[i]) - int(ukupnoZarazenih[i-1])
        brojNovozarazenih.append(x)
    broj = brojNovozarazenih[0]
    broj1 = abs(brojNovozarazenih[0]) - abs(brojNovozarazenih[1])
    return broj,broj1


#ova funkcija nam formatira tekset
#ulaz je lista sa frazama (csv_file)
#izlaz je lista sa frazama i brojem 

def formatiranje(p,csv_ulaz):
    ulaz_values = [0]
    ulaz_values = chosen_row[1]

    fraze1 = p[0]
    txt = fraze1.format(ulaz_values[1])
    fraze2 = p[1]
    broj = racuna(csv_ulaz)
    txt1 = fraze2.format(abs(broj[0]))
    fraze3 = p[2]
    txt2 = fraze3.format(ulaz_values[3])
    fraze4 = p[3]
    fraze5 = p[4]
    fraze6 = p[5]
    txt5 = fraze6.format(ulaz_values[4])
    if broj[1] < 0:
        txt3 = fraze4.format(abs(broj[1]))
        return txt,txt1,txt2,txt3,txt5
    else:
        txt4 = fraze5.format((broj[1]))
        return txt,txt1,txt2,txt4,txt5
    
    

#ova funkcija ubacije u izlazni file fraze sa brojem
#ulaz je csv_fie
#izlaz je txt file

def obradi(csv_fraze1):
    p = fraze_random(csv_fraze1)
    fraze = formatiranje(p,chosen_row)
    p1,p2,p3,p4,p5 = fraze
    return p1 + "\n" + p2 + "\n" + p3 + "\n" + p4 + "\n" + p5 + "\n" 


f_i = open(filename_i,'w')              
f_i.write (obradi(csv_fraze1))
f_i.close()
csv_ulaz.close()
csv_fraze.close()