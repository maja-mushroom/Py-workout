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
#print(moves([0,7]))
#print(moves([7,0]))
target = []  
#def count_moves(target):
knight_white = []
knight_white = moves([0,7])
print (knight_white)
knight_black = []
knight_black = moves([7,0])
N = 7
#print (knight_black)
queue = [] 
      
    # push starting position of knight 
    # with 0 distance 
queue.append((knight_white[0], knight_white[1], 0))
print (queue)
      
# make all cell unvisited  
visited = [[False for i in range(N + 1)]  
                      for j in range(N + 1)]
#print(visited) 
      
#visit starting state 
visited[knight_white[0]][knight_white[1]] = True

      
# loop untill we have one element in queue  
while(len(queue) > 0): 
          
    t = queue[0] 
    queue.pop(0)
          
    # if current cell is equal to target  
    # cell, return its distance
    
    if(t.x == target[0] and  t.y == target[1]): 
          return t.dist 
              
   # iterate for all reachable states  
    for i in range(8): 
              
        x = t.x + dx[i] 
        y = t.y + dy[i] 
              
        if(isInside(x, y, N) and not visited[x][y]): 
            visited[x][y] = True
            queue.append(cell(x, y, t.dist + 1)) 

while count < 4:
        dist = 0
        knight_white = moves([])
        for i in knight_white:
            if i == target:
                print("Pobjeda", knight_white)
            if i != target:
                dist = len(moves(i))
                lista_dist.append(dist)
        minpos = lista_dist.index(min(lista_dist))
        knight_white[minpos]
        print(knight_white[minpos])"""

        """if len(knight_white) == 4 and len(knight_black) == 4:
       if len(knight_white)> len(knight_black):
           return (knight_black)
       elif len(knight_black) > len(knight_white):
           return (knight_white)
       elif len(knight_white)== len(knight_black):
           return ("Nerijeseno")
    else:
        return ()