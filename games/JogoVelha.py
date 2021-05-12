import numpy as np
import datetime
from ManualPlayerJV import ManualPlayerJV
from RandomPlayerJV import RandomPlayerJV
from termcolor import colored

class JogoVelha:

    def __init__(self, player1, player2):
        self.board = np.zeros( (9) )
        self.players = [player1, player2]

    def printSymbol(number):
        if number==1:
            return colored('●', 'red')
        elif number==2:
            return colored('△', 'blue')
        else: 
            return ' '

    def printBoard(self): 
        print('\n-----------')
        for i in range(0,3):
            print(JogoVelha.printSymbol(self.board[i])+" | ", end='')
        print('\n-----------')
        for i in range(3,6):
            print(JogoVelha.printSymbol(self.board[i])+" | ", end='')
        print('\n-----------')
        for i in range(6,9):
            print(JogoVelha.printSymbol(self.board[i])+" | ", end='')
        print('\n-----------')

   
    def movement(self, player, space):
        #
        # Only accepts player equal 1 or 2
        # and position between 0 and 8 where:
        #
        # | 0 | 1 | 2 |
        # | 3 | 4 | 5 |
        # | 6 | 7 | 8 |
        #
        try:
            if(player not in (1,2)):
                raise Exception('Only players 1 or 2')
            if (self.board[space] == 0):
                self.board[space] = player
            else:
                raise Exception('Player '+str(player)+', you only can play in an empty space')
        except IndexError:
            raise Exception('Player '+str(player)+', you only can choose a number between 0 and 8')

    def hasWinner(self):
        if((self.board[0] == self.board[1] == self.board[2]) & (self.board[0] != 0)):
            return True
        elif((self.board[3] == self.board[4] == self.board[5]) & (self.board[3] != 0)):
            return True
        elif((self.board[6] == self.board[7] == self.board[8]) & (self.board[6] != 0)):
            return True
        elif((self.board[0] == self.board[3] == self.board[6]) & (self.board[0] != 0)):
            return True
        elif((self.board[1] == self.board[4] == self.board[7]) & (self.board[1] != 0)):
            return True
        elif((self.board[2] == self.board[5] == self.board[8]) & (self.board[2] != 0)):
            return True
        elif((self.board[0] == self.board[4] == self.board[8]) & (self.board[0] != 0)):
            return True
        elif((self.board[2] == self.board[4] == self.board[6]) & (self.board[2] != 0)):
            return True
        else:
            return False

    def isDraw(self):
        for i in range(0,9):
            if self.board[i] == 0:
                return False
        if self.hasWinner():
            return False
        else:
            return True

    def game(self):
        k=1
        while (not self.hasWinner()) and (not self.isDraw()):
            k = (int)(not k)
            inicio = datetime.datetime.now()
            self.movement(k+1, self.players[k].move(k+1, self.board))
            dur = (datetime.datetime.now() -inicio).total_seconds()
            if(dur > 10):
                print('Player '+ self.players[k].name() + ' duration (seconds): '+ str(dur))
            self.printBoard()
        
        if self.isDraw():
            print('Draw!')
            # returning the winner name only for Tournament purpose
            return 'draw'
        else:
            print('Player '+ JogoVelha.printSymbol(k+1)+ ": " + self.players[k].name() + ' is the winner!')
            # returning the winner name only for Tournament purpose
            return self.players[k].name()
            

def main():
    JogoVelha(RandomPlayerJV(), RandomPlayerJV()).game()
    JogoVelha(RandomPlayerJV(), RandomPlayerJV()).game()

if __name__ == '__main__':
    main()