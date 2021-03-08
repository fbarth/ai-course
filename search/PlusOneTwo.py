from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from Graph import State

#
# Implements a very simple problem to ilustrate search algorithms
#
# Initial state: 1
# Operations: +1 and +2
# Final state: any number bigger than 0
#

class PlusOneTwo(State):

    def __init__(self, number, op, Goal):
        self.number = number
        self.operator = op
        self.Goal = Goal

    def env(self):
        return str(self.number)
    
    def sucessors(self):
        sucessors = []
        sucessors.append(PlusOneTwo(self.number+2, '2', self.Goal))
        sucessors.append(PlusOneTwo(self.number+1, '1', self.Goal))
        return sucessors
    
    def is_goal(self):
        return self.number == self.Goal
    
    def description(self):
        return "Problema simples com operadores de soma 1 e soma 2. Estados representados apenas por um numero"
    
    def cost(self):
        return 1

    def h(self):
        #Metodo de calculo do custo heuristico
        #Valor absoluto da distancia entre objetivo e proximo nó, garantindo que distancias negativas não existam
        return (abs(self.Goal - self.number))
        #return 0
    
    def print(self):
        return str(self.operator)

from datetime import datetime

def main():
    
    #
    # Executando busca em largura
    #
    print('Busca em largura')
    state = PlusOneTwo(1, '', 10)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()
