#
# This class implements all the rules
# and control for the game 4-in-row
#
# To understand how this game works: https://www.coolmathgames.com/0-4-in-a-row
#

import numpy as np
from RandomPlayer import RandomPlayer
from ManualPlayer import ManualPlayer
from BarthPlayer import BarthPlayer
import datetime

class FourInRow:

    def __init__(self, player1, player2):
        self.board = np.zeros( (6,7) )
        self.players = [player1, player2]

    def printBoard(self):
        print(self.board)
        print("\n")

    #
    # Only accepts player equal 1 or 2
    # and column between 0 and 6
    #
    def movement(self, player, column):
        try:
            if(player not in (1,2)):
                raise Exception('Only players 1 or 2')
            for i in range(5,-2,-1):
                if (self.board[i,column] == 0):
                    break
            if(i<0):
                raise Exception('Player '+str(player)+', you can not play in a full column')
            self.board[i, column] = player
        except IndexError:
            raise Exception('Player '+str(player)+', you only can choose a column between 0 and 6')

    def endOfGame(self):
        # horizontally
        for i in range(6):
            current = None
            counter = 0
            for j in range(6):
                if ((self.board[i, j] in (1,2)) and (self.board[i, j] == self.board[i, j + 1])):
                    if (self.board[i, j]==current):
                        counter = counter + 1
                        current = self.board[i, j]
                    else:
                        counter = 1
                        current = self.board[i, j]
                else:
                    counter = 0
                if (counter==3):
                    return True
        # vertically
        for i in range(6):
            current=None
            counter = 0
            for j in range(5):
                if ((self.board[j, i] in (1,2)) and (self.board[j,i] == self.board[j+1,i])):
                    if(self.board[j,i]==current):
                        counter = counter + 1
                        current = self.board[j,i]
                    else:
                        counter = 1
                        current = self.board[j,i]
                else:
                    counter = 0
                if (counter == 3):
                    return True
        # "main" diagonal
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(self.board, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]
                if (counter == 3):
                    return True
        # "anti" diagonal
        # [::-1] rotaciona as linhas da matriz
        temp = self.board[::-1]
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(temp, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]
                if (counter == 3):
                    return True

        return False

    def game(self):
        k=1
        while (not self.endOfGame()):
            k = (int)(not k)
            inicio = datetime.datetime.now()
            self.movement(k+1, self.players[k].move(k+1, self.board))
            dur = (datetime.datetime.now() -inicio).total_seconds()
            if(dur > 10):
                print('Player '+ self.players[k].name() + ' duration (seconds): '+ str(dur))
            self.printBoard()
        print('Player ' + self.players[k].name() + ' is the winner!')

def main():
    FourInRow(BarthPlayer(), ManualPlayer()).game()

if __name__ == '__main__':
    main()