#
# TODO implement a solution for N-queens problem, where N could
# be any number between 4 and 10.
#

from SearchAlgorithms import SubidaMontanhaEJ_FELIPE
from Graph import State
from random import randrange


class N_QueensProblemEJ(State):

    # Elmeri 11710854 e Felipe 11710467

    def __init__(self, v):
        self.value = v

    def env(self):
        return "n: " + str(self.value)

    def sucessors(self):
        sucessors = []

        for i in range(1,5):
            x = self.value - randrange(0, 3)
            sucessors.append(N_QueensProblemEJ(x))

        return sucessors

    def is_goal(self):
        return 1

    def description(self):
        return "Describe the problem"

    def cost(self):
        return 1

    def print(self):
        pass

    def h(self):
        return self.value

    def printEnv(self):
        return self.value


def main():
    print('Subida na montanha')

    state = N_QueensProblemEJ(100)
    algorithm = SubidaMontanhaEJ_FELIPE()
    result = algorithm.search(state)
    
    if result != None:
        print('Achou!')
        print(result.printEnv())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()
