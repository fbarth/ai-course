from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from Graph import State

# 
# Implements a simplified version of vacuum world problem
#

class VacuumWorld(State):

    def __init__(self, left, right, vacuum, op):
        self.left = left
        self.right = right
        self.vacuum = vacuum
        self.operator = op
    
    def sucessors(self):
        sucessors = []
        # ir para esquerda
        sucessors.append(VacuumWorld(self.left, self.right, 'left', 'ir p/ esquerda'))
        #ir para direita
        sucessors.append(VacuumWorld(self.left, self.right, 'right', 'ir p/ esquerda'))
        #limpar
        if self.vacuum == 'left':
            sucessors.append(VacuumWorld('limpo', self.right, self.vacuum, 'limpar'))
        else:
            sucessors.append(VacuumWorld(self.left, 'limpo', self.vacuum, 'limpar'))
        return sucessors
    
    def is_goal(self):
        if (self.left == 'limpo') and (self.right == 'limpo'):
            return True
        return False
    
    def description(self):
        return "Implementa o problema do aspirador de pó"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorld('sujo', 'sujo', 'left', '')
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
    state = VacuumWorld('sujo', 'sujo', 'left', '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
    