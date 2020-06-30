import random

class Osoba:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.score = 0
        self.played = '-'
    
    def print_p(self):
        print(self.name , self.lastname + ' score: ' , self.score ,'turn: ', self.played)
    
    def play_turn(self):
        n = random.randint(0,3)
        if n == 1:
            self.played = 'k'
        elif n == 2:
            self.played = 'p'
        else:
            self.played = 'm'
    

def game(choice1, choice2):
    if choice1 == choice2:
        return 0
    elif choice1 == 'k':  
        if choice2 == 'p':
            return 2
        else:
            return 1
    elif choice1 == 'p':
        if choice2 == 'm':
            return 2
        else:
            return 1
    elif choice1 == 'm':
        if choice2 == 'k':
            return 2
        else:
            return 1


player1 = Osoba('maja', 'uiux')
player2 = Osoba('bilja', 'ds')

player3 = Osoba('hana', 'green')
player4 = Osoba('raso','java')



###first round 
i=1
while i<7:
    print('Igra:', i, '\n')
    player1.play_turn()
    player1.print_p()
    player2.play_turn()
    player2.print_p()
    
    round_game = game(player1.played, player2.played)
    
    if round_game == 1:
        player1.score += 1
        
    elif round_game == 2:
        player2.score += 1
        
    else:
        player1.score += 0.5
        player2.score += 0.5
        print('Igra je izjednacena\n')        
    
    if player1.score >= 3:
        #new object created
        p1 = player1
        print('Pobjednik je prvi igrac\n')
        break
    if player2.score >= 3:
        #new object created
        p1 = player2
        print('Pobjednik je drugi igrac\n')
        break
    i+=1


##second round
i=1
while i<7:
    print('Igra:', i, '\n')
    player3.play_turn()
    player3.print_p()
    player4.play_turn()
    player4.print_p()
    
    round_game = game(player3.played, player4.played)
    
    if round_game == 1:
        player3.score += 1
        
    elif round_game == 2:
        player4.score += 1
        
    else:
        player3.score += 0.5
        player4.score += 0.5
        print('Igra je izjednacena\n')        
    
    if player3.score >= 3:
        p2 = player3
        print('Pobjednik je prvi igrac\n')
        break
    if player4.score >= 3:
        p2 = player4
        print('Pobjednik je drugi igrac\n')
        break
    i+=1

p1.print_p()
p2.print_p()


###final round
p1.score = 0
p2.score = 0
i=1
while i<7:
    print('Igra:', i, '\n')
    p1.play_turn()
    p1.print_p()
    p2.play_turn()
    p2.print_p()
    
    round_game = game(p1.played, p2.played)
    
    if round_game == 1:
        p1.score += 1
        
    elif round_game == 2:
        p2.score += 1
        
    else:
        p1.score += 0.5
        p2.score += 0.5
        print('Igra je izjednacena\n')        
    
    if p1.score >= 3:
        print('Pobjednik je prvi igrac\n')
        break
    if p2.score >= 3:
        print('Pobjednik je drugi igrac\n')
        break
    i+=1