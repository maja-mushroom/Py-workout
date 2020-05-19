import csv
import os
import webbrowser

here = os.path.dirname(os.path.abspath(__file__))
f = open('index.html','w')
csv_ulaz = open("ulaz.csv")
csv_ulaz = csv.reader(csv_ulaz, delimiter =",")
next(csv_ulaz)

ime = []
datum = []
zanimanje = []
grad = []
kurs = []


for i in csv_ulaz:
    ime.append(i[0])
    datum.append(i[1])
    zanimanje.append(i[2])
    grad.append(i[3])
    kurs.append(i[4])
    
parent_dir = "C:\html\index_page"

message = """<html>
<head><link rel="stylesheet" href="bilja.css">
<link rel="stylesheet" href="hana.css">
<link rel="stylesheet" href="maja.css">
</head>
<body><h1>{}</h1></br>
<h2>{}</h2>
<h3>{}</h3>
<h4>{}</h4>
<h5>{}</h5>
</body>
</html>"""

path = parent_dir + "\index.html"
open_dic = webbrowser.open(path)     
print (open_dic)


entries = os.listdir('index_page/')
print(entries)
i = 0
for x in entries:
    path = os.path.join(parent_dir, x, "index.html")
    print(path)
    f1 = open(path,'w')
    f1.write(message.format(ime[i],datum[i],zanimanje[i],grad[i],kurs[i]))
    f1.close()
    webbrowser.open_new_tab(path)
    i += 1

    

f.close()
csv_ulaz.close()