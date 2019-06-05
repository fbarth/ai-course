#
# TODO implement a solution for N-queens problem, where N could 
# be any number between 4 and 10.
#

from SearchAlgorithms import SubidaMontanha
from Graph import State
from random import choice
from random import randrange
from collections import Counter

    # Team paradola:
    # Igor Ehlert - 11710374
    # Vinícius Gomes - 11710390

class N_QueensProblem(State):

    def __init__(self, v):
        self.value = v
    
    def sucessors(self):
        sucessors = []
        for i in range(1,5):
            c = self.value - randrange(0,3)
            sucessors.append(N_QueensProblem(c))
        return sucessors
    
    def is_goal(self):
        return 1
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        pass

    def printEnv(self):
        return "N: " + str(self.value)
    
    def h(self):
        # verificar se possui alguma rainha na coluna, na linha ou nas diagonais 
        # (diagonal 1 = col+1 lin+1; diagonal 2 = col+1 lin-1; diagonal 3 = col-1 lin+1) 
        return self.value
        
def main():
    print('Subidamontanha')

    state = N_QueensProblem(16)
    algorithm = SubidaMontanha()
    result = algorithm.search(state)
    
    if result != None:
        print('Achou!')
        print(result.printEnv())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()