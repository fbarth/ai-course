from SearchAlgorithms import SubidaMontanhaPGB
from Graph import State
from random import randrange

class N_QueensProblem(State):

    def __init__(self, board):
        self.board = board
    
    def sucessors(self):
        sucessors = []

        next_state = self.board

        #Escolher uma linha aleatoria para mover a rainha
        line_number = randrange(len(self.board))
        #Tirar a rainha da posicao atual
        for x in range(len(self.board)):
            next_state[line_number][x] = 0
        #Colocar a rainha em uma nova posicao aleatoria na mesma linha
        next_state[line_number][randrange(len(self.board))] = 1
  
        sucessors.append(N_QueensProblem(next_state))
        return sucessors


    def is_goal(self):
        pass
    
    def description(self):
        return "Implementation of the N-Queens problem, where N can be any real number between 4 and 10"
    
    def cost(self):
        return 1

    def print(self):
        pass

    def printEnv(self):
        return self.board
    
    def h(self):
        #Mapear o numero de rainhas que estão ameaçando outra rainha
        h = 0
        for x in range(len(self.board)):
            queen_y_index = self.board[x].index(1)
            #Como não irão existir rainhas numa mesma linha
            #iremos verificar rainhas que estão em uma mesma coluna
            for x in range(len(self.board)):
                if self.board[x][queen_y_index] == 1:
                    h = h + 1
            #Agora temos que verificar rainhas que estao em uma mesma diagonal
            #como?
        return h


def main():
    print('Hill-climbing Algorithm')

    #Gerar um tabuleiro aleatorio inicial contendo N linhas, N Colunas e N rainhas
    #a unica restricao inicial é que cada linha contem uma unica rainha
    n = 4
    board = [[0 for x in range(n)] for y in range(n)]
    for x in range(n):
        board[x][randrange(n)] = 1

    state = N_QueensProblem(board)
    algorithm = SubidaMontanhaPGB()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.printEnv())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()