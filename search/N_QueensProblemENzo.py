from SearchAlgorithms import AEstrela
from Graph import State

# Projeto realizado por Enzo Scapinelli

class Queens(State):


    def __init__(self, size, queens, isQueensSafe, op):
        self.size = size
        self.queens = queens
        self.isQueensSafe = isQueensSafe
        self.operator = op
        
    def sucessors(self):
        sucessors = []

        if (self.queens[0] - 1 >= 0):
            sucessors.append(Queens(self.size, [self.queens[0] - 1, self.queens[1]], self.isQueensSafe, "Queen up"))

        if (self.queens[0] + 1 >= 0):
            sucessors.append(Queens(self.size, [self.queens[0] + 1, self.queens[1]], self.isQueensSafe, "Queen down"))

        if (self.queens[1] - 1 >= 0):
            sucessors.append(Queens(self.size, [self.queens[0], self.queens[1] - 1], self.isQueensSafe, "Queen left"))

        if (self.queens[1] + 1 >= 0):
            sucessors.append(Queens(self.size, [self.queens[0], self.queens[1] + 1], self.isQueensSafe, "Queen right"))

        self.isSafe(self.queens)
        
        return sucessors

    def printEnv(self):
        # self.buildBoard()
        return self.queens
        # """ + str(self.board[0]) + """
        # """ + str(self.board[1]) + """
        # """ + str(self.board[2]) + """
        # """ + str(self.board[3]) + """
        # """ + str(self.board[4]) + self.operator

    def isSafe(self, queens):
        if (queens[0] == 2):
            return True

    # def buildBoard(self):
    #     self.board[self.queens] = "Q"

    #     return self.road
    
    def is_goal(self):
        goal = [0,4]
        return (self.queens == goal)
    
    def description(self):
        return "Problema das rainhas"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        return 1


def main():
    
    size = 4
    queens = [0,0]

    print('Busca A*')
    state = Queens(size, queens, False, '')
    algorithm = AEstrela()
    #algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path()+" ; Drop Passanger")
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
	
