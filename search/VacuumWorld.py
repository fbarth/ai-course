from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from Graph import State

# TODO
# Implements a simplified version of vacuum world problem
#

class VacuumWorld(State):

    def __init__(self):
        pass
    
    def sucessors(self):
        pass
    
    def is_goal(self):
        pass
    
    def description(self):
        return "bla"
    
    def cost(self):
        return 1

    def print(self):
        pass

def main():
    
    #
    # Executando busca em largura
    #
    state = None #TODO
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
    state = None #TODO
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
    