from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from Graph import State

# 
# Implements a simplified version of vacuum world problem
# with 4 room
#

class VacuumWorld(State):

    def __init__(self, left, right, vacuum, op):
        pass

    
    def sucessors(self):
        pass
    
    def is_goal(self):
        pass
    
    def description(self):
        return "Implementa o problema do aspirador de pó com 4 quartos"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorldWith4room('sujo', 'sujo', 'left', '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    #
    # Executando busca em profundidade
    #
    state = VacuumWorldWith4room('sujo', 'sujo', 'left', '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
    