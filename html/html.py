import csv
import os
import webbrowser

here = os.path.dirname(os.path.abspath(__file__))
f = open('helloworld.html','w')
csv_ulaz = open("ulaz.csv")
csv_ulaz = csv.reader(csv_ulaz, delimiter =",")
next(csv_ulaz)

parent_dir = "C:/Users/Maja/Desktop/Python vježbaona/Py-workout/html/index_page"

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

for i in csv_ulaz:
    directory = i[0]
    # Path 
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)
 

entries = os.listdir('index_page/')
for f in entries:
    f = open('index.html','w')
    f.write(message)
    f.close()
    




f.write(message)
f.close()
webbrowser.open_new_tab('index.html')

"""
f_i = open(filename_i,'w')              
f_i.write (obradi(csv_fraze1))
f_i.close()
csv_ulaz.close()
csv_fraze.close()"""