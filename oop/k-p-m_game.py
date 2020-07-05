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


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round_game = 0   


    def play(self):
        
        if self.player1.played == self.player2.played:
            self.round_game = 0
        elif self.player1.played == 'k':  
            if self.player2.played == 'p':
                self.round_game = 2
            else:
                self.round_game = 1
        elif self.player1.played == 'p':
            if self.player2.played == 'm':
                self.round_game = 2
            else:
                self.round_game = 1
        elif self.player1.played == 'm':
            if self.player2.played == 'k':
                self.round_game = 2
            else:
                self.round_game = 1
    
    
    def game_winer(self, player1, player2):
        i=1
        player1.score = 0
        player2.score = 0
        
        while i<7:
            print('Igra:', i, '\n')
            player1.play_turn()
            player2.play_turn()
            player1.print_p()
            player2.print_p()
            

            if self.round_game == 1:
                player1.score += 1   
            elif self.round_game == 2:
                player2.score += 1 
            else:
                player1.score += 0.5
                player2.score += 0.5
                print('Igra je izjednacena\n')        
            
            if player1.score >= 3:
                print('Pobjednik je prvi igrac\n')
                return player1
            if player2.score >= 3:
                print('Pobjednik je drugi igrac\n')
                return player2
            i+=1

        

p1 = Osoba('maja', 'uiux')
p2 = Osoba('bilja', 'ds')

p3 = Osoba('hana', 'pu')
p4 = Osoba('raso', 'java')


g1 = Game(p1,p2)
winer1 = g1.game_winer(p1, p2)

g2 = Game(p3, p4)
winer2 = g2.game_winer(p3, p4)

g3 = Game(winer1, winer2)
g3.game_winer(winer1, winer2)

