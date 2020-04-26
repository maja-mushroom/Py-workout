import os
here = os.path.dirname(os.path.abspath(__file__))
filename_u = os.path.join(here,"ulaz1.txt")
filename_i = os.path.join(here,"izlaz1.txt")

lista_next_x = []
lista_next_y = []
lista_next =[]
# ova funkcija nam vraća sve moguće poteze skakača
# ulaz je int
# izlaz je lista
def moves(knight):
    lista_next =[]
    x_next = 0
    y_next = 0
    a = int(knight[0])
    b = int(knight[1])
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]
    for x,y in zip(x_move, y_move):
        x_next = x + a
        y_next = y + b
        if x_next < 0 or y_next < 0 or x_next > 7 or y_next > 7:
          pass
        else:
          lista_next_x.append(x_next)
          lista_next_y.append(y_next)
          lista_next.append(str(x_next) + str(y_next))
    #print(lista_next)
    return (lista_next)
#print(moves(knight))

pos_move = []
#ova funkcija nam provjerava sva slobodna polja na tabli
#ulaz je lista
#izlaz je lista
def pos_moves(lista_next, board_moves):
    pos_move = []
    board_moves.pop(1)
    #elem = list(set(lista_next) - set(board_moves))
    for x in lista_next:
        if x not in board_moves:
             x = x[0].replace("0","a") + x[1]
             x = x[0].replace("1","b") + x[1]
             x = x[0].replace("2","c") + x[1]
             x = x[0].replace("3","d") + x[1]
             x = x[0].replace("4","e") + x[1]
             x = x[0].replace("5","f") + x[1]
             x = x[0].replace("6","g") + x[1]
             x = x[0].replace("7","h") + x[1]
             pos_move.append(x)
    #print(pos_move)
    return(pos_move)
#print(pos_moves(lista_next, board_moves))

#funkcija obradi nam provjerava prilikom poteza koje su moguće opcije skakača i gdje i na koje polje smije da skoci
#ulaz je lista
#izlaz je lista
def obradi(ulaz):
  board_moves = []
  for x in ulaz:
        x = x[0].replace("a","0") + x[1]
        x = x[0].replace("b","1") + x[1]
        x = x[0].replace("c","2") + x[1]
        x = x[0].replace("d","3") + x[1]
        x = x[0].replace("e","4") + x[1]
        x = x[0].replace("f","5") + x[1]
        x = x[0].replace("g","6") + x[1]
        x = x[0].replace("h","7") + x[1]
        board_moves.append(x)
  #print (board_moves)
  knight = board_moves[1]   
  lista_next = moves(knight)
  #print(lista_next)
  if (pos_moves(lista_next, board_moves)) == []:
        return ("Impossible\n" +  "Skakac se nalazi na polju: " + str(pos_moves(lista_next, board_moves)) )
  else:
      return ("Ovo su vasi moguci potezi" + str (pos_moves(lista_next, board_moves)))

f_u = open(filename_u,'r')
f_i = open(filename_i,'w')              
for line in f_u:
    line = line.replace("\n","")
    x = line.split(" ")
    f_i.write(str(obradi(x)) + "\n")
f_u.close()
f_i.close()
