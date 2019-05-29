from abc import ABC, abstractmethod

#
# Implements basic data structures necessary to implement 
# search algorithms
#

class Node:
    def __init__(self,state,father_node):
        self.state = state
        self.father_node = father_node
        if self.father_node == None:
            self.depth = 0
            self.g = 0
        else:
            self.depth = father_node.depth + 1
            self.g = state.cost() + self.father_node.g

    def show_path(self):
        if self.father_node != None:
            return self.father_node.show_path()  + " ; " + self.state.operator 
        else:
            return self.state.operator
    
    def h(self):
        return self.state.h()

    def f(self):
        #f(n) = g(n) + h(n)
        return self.g + self.h()

    def nearStates(self, state): # peguei do github
        near_states = []
        # Para cada state[coluna] verfica se as colunas vizinhas estao vazias
        for row in range(self.N):
            for col in range(self.N):
                # Se for diferente:
                #   entao a col atual da iteracao esta disponivel para movimentar-se
                #   visto que o state[] guarda o valor das colunas em que estao as rainhas
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col  # Troca a coluna para a vazia
                    near_states.append(list(aux))  # E inclui na lista de nearStates
        return near_states
    
    def best_nextState(self, neighbours):
        best = neighbours[0]

        for i in neighbours:
            if i < best:
                best = i

        return best       
    
class State(ABC):

    @abstractmethod
    def sucessors(self):
        pass
    
    @abstractmethod
    def is_goal(self):
        pass
    
    @abstractmethod
    def description(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def printEnv(self):
        pass