"""
intro = "e8 a4 a7 b7 c7 e7 d7"
privremeno = intro.split(" ")
print(intro)

konj = intro[1]
kolona, red = ["e8","a4","a7","b7","c7","e7""d7]
X = [2, 1, -1, -2, -2, -1, 1, 2]; 
Y = [1, 2, 2, 1, -1, -2, -2, -1]; 


column = letterNumberSwap(column)
kolona, red = list(position.strip().upper())
k = int(kolona)
r = int(red) 
lista_konj = []

if (0 < (k + 2) <= 8):
        if (0 < (r - 1) <= 8):
            lista_konj.append([k + 2, r -1])
        if (0 < (r + 1) <= 8):
            lista_konj.append([k + 2, r + 1])
if (0 < (k - 2) <= 8):
        if (0 < (r - 1) <= 8):
            lista_konj.append([k - 2, r - 1])
        if (0 < (r + 1) <= 8):
            lista_konj.append([k - 2, r + 1])
if (0 < (k - 1) <= 8):
        if (0 < (r - 2) <= 8):
            lista_konj.append([k - 1, r - 2])
        if (0 < (r + 2) <= 8):
            lista_konj.append([k - 1, r + 2])
if (0 < (k + 1) <= 8):
        if (0 < (r - 2) <= 8):
            lista_konj.append([k + 1, r - 2])
        if (0 < (r + 2) <= 8):
            lista_konj.append([k + 1, r + 2])
"""
import os
here = os.path.dirname(os.path.abspath(__file__))
filename_u = os.path.join(here,"ulaz1.txt")
filename_i = os.path.join(here,"izlaz1.txt")
N = 8
intro = "58 14 06 27 37 47 57"
column = []
row = []
column = intro.split(' ')
board_moves =list(column)
knight = board_moves[1]

sol = []
lista_next_x = []
lista_next_y = []
lista_next =[]
def moves(knight):
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
    return (lista_next)
#print(moves(knight))
pos_move = []
def pos_moves(lista_next, board_moves):
    board_moves.pop(1)
    for x in lista_next:
        if not x in board_moves:
             x = x[0].replace("0","a") + x[1]
             x = x[0].replace("1","b") + x[1]
             x = x[0].replace("2","c") + x[1]
             x = x[0].replace("3","d") + x[1]
             x = x[0].replace("4","e") + x[1]
             x = x[0].replace("5","f") + x[1]
             x = x[0].replace("6","g") + x[1]
             x = x[0].replace("7","h") + x[1]
             pos_move.append(x)
             
    return(pos_move)
#print(pos_moves(lista_next, board_moves))

def make_alph(pos_moves):
   for i in pos_move:
      print(i)
  
#print(pos_move)
#return(pos_move)
        
"""
    for x in lista_next:
        for y in board_moves:
            temp = y
            if x in temp:
                pos_move.append(x)
                
    return(pos_move)

print(pos_moves(lista_next, board_moves))
 

def pos_moves(lista_next, board_moves):
    pos_move = []
    board_moves.pop(1)
    for i in range(0,len(lista_next)):
        if lista_next[i]!=board_moves[i]:
            pos_move.append(i)
    return (pos_move)
#print (pos_moves(lista_next,board_moves))

def pos_moves(lista_next, board_moves):
    pos_move = []
    board_moves.pop(1)
    for x in lista_next:
        if x in board_moves:
            pos_move.append(x)
        else:
            pos_move.append("0")
    return(pos_move)
        


    for x in lista_next:
        for y in board_moves:
            if x  y:
                 pos_move.append(x)
    return(pos_move)
#print(pos_moves(lista_next,board_moves))

def pos_moves( lista_next, board_moves):
    pos_move = []
    for x in lista_next:
        for y in board_moves:
            pos_move.append(x==y)
    return(pos_move)
print(pos_moves(lista_next,board_moves))


def pos_moves( lista_next, board_moves):
    pos_move = []
    for x in lista_next:
        for y in board_moves:
            if x != y:
                break 
            else:
                pos_move.append(x)
                return (pos_move)         
print(pos_moves(lista_next,board_moves))

def pos_moves( lista_next, board_moves):
    pos_move = []
    for x in lista_next:
        for y in board_moves:
            if x != y:
                break 
            else:
                pos_move.append(x)
                return (pos_move)         
print(pos_moves(lista_next,board_moves))


  for y in board_moves:
    for x in lista_next:
      if set(y) ==set(x):
        break
      else:
       if x not in pos_move:
           pos_move.append(x)
           break
  return(pos_move)
print(pos_moves( lista_next, board_moves))
pos_move = []

def pos_moves( lista_next, board_moves):
  board_moves.pop(1)
  for y in board_moves:
    for x in lista_next:
      if y == x:
        break
      else:
       if x not in pos_move:
           pos_move.append(x)
           break
  return(pos_move)
print(pos_moves( lista_next, board_moves))


#def make_l(pos_moves):
"""for i in pos_move:
  i = i[0].replace("1","a")
  i = i[0].replace("2","b")
  i = i[0].replace("3","c")
  i = i[0].replace("4","d")
  i = i[0].replace("5","e")
  i = i[0].replace("6","f")
  i = i[0].replace("7","g")
  i = i[0].replace("8","h")
print(pos_move)
  #return(pos_move)"""


"""
def obradi(ulaz):
  moves(knight)
  return pos_moves(lista_next, board_moves)
    

f_u = open(filename_u,'r')
f_i = open(filename_i,'w')              
for line in f_u:
    line = line.replace("\n","")
    x = line.split(",")
    f_i.write(str(obradi(x)) + "\n")
f_u.close()
f_i.close()

    
        
           

          


