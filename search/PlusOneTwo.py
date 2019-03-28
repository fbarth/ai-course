from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import BuscaAstar
from Graph import State

#
# Implements a very simple problem to ilustrate search algorithms
#
# Initial state: 1
# Operations: +1 and +2
# Final state: any number bigger than 0
#

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

    def h_cost(self):
        #Metodo de calculo do custo heuristico
        #Valor absoluto da distancia entre objetivo e proximo nó, garantindo que distancias negativas não existam
        return (abs(10 - self.number))
    
    def print(self):
        return str(self.operator)


def main():
    
    #
    # Executando busca em largura
    #
    print('Busca em largura')
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
    print('Busca em profundidade')
    state = PlusOneTwo(1, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    #
    # Executando busca em profundidade iterativa
    #
    print('Busca em profundidade iterativa')
    state = PlusOneTwo(1, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    #
    # Executando busca de custo uniforme
    #
    print('Busca de custo uniforme')
    state = PlusOneTwo(1, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    #
    # Executando busca gananciosa
    #
    print('Busca Gananciosa')
    state = PlusOneTwo(1, '')
    algorithm = BuscaGananciosa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    #
    # Executando busca A*
    #
    print('Busca A*')
    state = PlusOneTwo(1, '')
    algorithm = BuscaAStar()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
        

if __name__ == '__main__':
    main()
    
