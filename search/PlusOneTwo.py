from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from Graph import State

class PlusOneTwo(State):

    def __init__(self, number, op):
        self.number = number
        self.operator = op
    
    def sucessors(self):
        sucessors = []
        sucessors.append(PlusOneTwo(self.number+2, '2'))
        sucessors.append(PlusOneTwo(self.number+1, '1'))
        return sucessors
    
    def is_goal(self):
        if self.number == 10:
            return True
        return False
    
    def description(self):
        return "Problema simples com operadores de soma 1 e soma 2. Estados representados apenas por um numero"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)


def main():
    
    #
    # Executando busca em largura
    #
    state = PlusOneTwo(1, '')
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
    state = PlusOneTwo(1, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')




if __name__ == '__main__':
    main()
    