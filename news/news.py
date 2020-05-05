import csv
import random
import os
here = os.path.dirname(os.path.abspath(__file__))
filename_i = os.path.join(here,"izlaz.txt")
csv_ulaz = open ("ulaz.csv")
csv_fraze = open ("phrases.csv")
csv_fraze1 = csv.reader(csv_fraze, delimiter =",")
with open("ulaz.csv") as f:
    reader = csv.reader(f)
    chosen_row = list(reader)



def phrases_append(csv_phrases):
    phrase1 = []
    phrase2 = []
    phrase3 = []    
    for row1 in csv_fraze1:
        if row1[0] == "1":
            phrase1.append(row1[1])
        if row1[0] == "2":
            phrase2.append(row1[1])
        if row1[0] == "3":
            phrase3.append(row1[1])
    return (random.choice(phrase1),random.choice(phrase2),random.choice(phrase3))
print(phrases_append(csv_fraze1))


def chosen_num(phrase1,phrase2,phrase3,csv_ulaz1):
    ulaz_values = [0]
    ulaz_values = chosen_row[1]
    print (ulaz_values[1])
    txt = phrase1.format(ulaz_values[1])
    print(txt)
    txt1 = phrase2.format(ulaz_values[2])
    txt2 = phrase3.format(ulaz_values[3])
    return(txt,txt1,txt2)
print(chosen_num(phrase1,phrase2,phrase3,chosen_row))



f_i = open(filename_i,'w')              
f_i.write((line) + "\n")
f_i.close(phrases_append(csv_fraze))
csv_ulaz.close()
csv_fraze.close()