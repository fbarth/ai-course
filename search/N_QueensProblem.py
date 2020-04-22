#
# Implements a solution for N-queens problem, where N could 
# be any number between 4 and 10.
#

from SearchAlgorithms import SubidaMontanha
from SearchAlgorithms import SubidaMontanha2
from Graph import State
from random import randrange
import numpy as np
import random
import time

class N_QueensProblem(State):

    def __init__(self, size, board):
        self.size = size
        self.board = board

    def env(self):
        return self.board
    
    def sucessors(self):
        sucessores = []
        for i in range(0,self.size):
            for j in range(0,self.size):
                if(self.board[i][j] == 1):
                    #move up
                    if((i - 1) >=0 and self.board[i-1][j] == 0):
                        temp = self.board.copy()
                        temp[i][j] = 0
                        temp[i-1][j] = 1
                        sucessores.append(N_QueensProblem(self.size, temp))
                    #move down
                    if((i + 1) < self.size and self.board[i+1][j] == 0):
                        temp = self.board.copy()
                        temp[i][j] = 0
                        temp[i+1][j] = 1
                        sucessores.append(N_QueensProblem(self.size, temp))
                    #move left
                    if((j - 1) >=0 and self.board[i][j-1] == 0):
                        temp = self.board.copy()
                        temp[i][j] = 0
                        temp[i][j-1] = 1
                        sucessores.append(N_QueensProblem(self.size, temp))
                    #move right
                    if((j + 1) < self.size and self.board[i][j+1] == 0):
                        temp = self.board.copy()
                        temp[i][j] = 0
                        temp[i][j+1] = 1
                        sucessores.append(N_QueensProblem(self.size, temp))
        return sucessores
                      
    def is_goal(self):
        if self.h() == 0:
            return True
        return False
    
    def description(self):
        return "Queens Problem"
    
    def cost(self):
        return 1

    def print(self):
        pass
    
    def h(self):
        line_strikes = 0
        for i in range(0,self.size):
            temp = sum(self.board[i,:])
            if temp > 1:
                line_strikes = line_strikes + temp
        
        column_strikes = 0
        for i in range(0,self.size):
            temp = sum(self.board[:,i])
            if temp > 1:
                column_strikes = column_strikes + temp
        
        diag_strikes = 0
        for k in range((self.size-1)*-1, self.size-1):
            temp = sum(np.diag(self.board, k=k))
            if temp > 1:
                diag_strikes = diag_strikes + temp
        
        diag_strikes_inv = 0
        # by Daniel Shimoda
        inv = self.board[::-1]
        for k in range((self.size-1)*-1, self.size-1):
            temp = sum(np.diag(inv, k=k))
            if temp > 1:
                diag_strikes_inv = diag_strikes_inv + temp
        
        return line_strikes + column_strikes + diag_strikes + diag_strikes_inv

    def randomBoard(self):
        self.board = self.generateBoard()
        while not self.validBoard():
            self.board = self.generateBoard()

    def generateBoard(self):
        board = np.zeros( (self.size,self.size) )
        for i in range(0,self.size):
            line = random.randrange(0, self.size)
            column = random.randrange(0, self.size)
            board[line,column] = 1
        return board

    def validBoard(self):
        if np.sum(self.board) != self.size:
            return False
        return True

def main():
    print('Busca Subida da Montanha')
    state = N_QueensProblem(size = 7, board = None)
    state.randomBoard()
    #algorithm = SubidaMontanha()
    algorithm = SubidaMontanha2()
    print("Initial state with h = "+str(state.h()))
    start = time.time()
    result = algorithm.search(state)
    end = time.time()
    if result != None:
        #print('Achou!')
        print(result.env())
        print('Final state with h = '+str(result.h()))
        print('Duration in seconds = '+str(end-start))
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()