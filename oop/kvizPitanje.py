class Player:

    def __init__(self, name):
        self.name = name
        self.played = ' '
        self.__score = 0
    
    def print_p(self):
        print(self.name  + ' score: ' , self.__score ,'turn: ')

    def addPoint(self):
        self.__score += 1
    
    def subPoint(self):
        if self.__score >= 0.5:
            self.__score -= 0.5
    
    def getScore(self):
        return self.__score
  

class Question:

    def __init__(self, question, trueAnswer, answer1, answer2, answer3):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.trueAnswer = trueAnswer
    
    def showQuestion(self):
        print(self.question)
        print('a', self.answer1)
        print('b', self.answer2)
        print('c', self.answer3)


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.questions = []
    
    def addQuestion(self, question):
        self.questions.append(question)


    def game(self, player1, player2):
        
        for i in self.questions:
            print('***********************************************')
            print('Pitanje glasi.. ', '\n')
            i.showQuestion()
            print(player1.name)
            player1.played = input("Unesite odgovor na postavljeno pitanje: ")
            
            print(player2.name)
            player2.played = input('Unesite odgovor na postavljeno pitanje: ')

            print('***********************************************')

            if player1.played == i.trueAnswer:
                print()
                print(player1.name, 'odgovor je tacan!\n')
                player1.addPoint() 
            else:
                print()
                print(player1.name,'odgovor je netacan!\n')
                player1.subPoint()

            if player2.played == i.trueAnswer:
                print()
                print(player2.name, 'odgovor je tacan!\n')
                player2.addPoint()    
            else:
                print()
                print(player2.name, 'odgovor je netacan!\n')
                player2.subPoint()     


    def getWiner(self):
        p1 = self.player1.getScore()
        p2 = self.player2.getScore()
        if p1 > p2:
            print('***********************************************')
            print('Pobjednik je', self.player1.name, 's brojem osvojenih bodova', p1, '\n')
            print(self.player2.name, 'je osvojio', p2)
            print('***********************************************')
            return self.player1
        elif p1 == p2:
            print('***********************************************')
            print('Rezultat je izjednacen!')
            print(self.player1.name, 'je osvojio,' , p1)
            print(self.player2.name, 'je osvojio,' , p2)
            print('***********************************************')
        else:
            print('***********************************************')
            print('Pobjednik je', self.player2.name, 's brojem osvojenih bodova', p2, '\n')
            print(self.player1.name, 'je osvojio', p1)
            print('***********************************************')
            return self.player2

        

p1 = Player('maja')
p2 = Player('bilja')

game1 = Game(p1,p2)
q1 = Question('Koje boje je slon?','c', 'plave', 'ljubicaste', 'sive')
q2 = Question('Mis ima koliko nogu?','b', 'dvije', 'cetri', 'tri')

q3 = Question('Kakve pruge ima zebra?', 'c', 'crveno-crne', 'zuto-plave', 'crno-bijele')
q4 = Question('Ko je pojeo crvenkapinu baku?', 'b', 'tigar', 'vuk', 'mis')

q5 = Question('Koje boje je ptica Tviti', 'a', 'zute', 'smedje', 'sarene')
q6 = Question('Gdje zivi krokodil?', 'c', 'jezeru', 'rijeci', 'mocvari')


game1.addQuestion(q1)
game1.addQuestion(q2)
game1.addQuestion(q3)
game1.addQuestion(q4)
game1.addQuestion(q5)
game1.addQuestion(q6)

game1.game(p1, p2)
print(game1.getWiner())
