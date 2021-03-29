from collections import deque
from Graph import Node
import logging
logging.basicConfig(filename='search_algorithms.log', level=logging.DEBUG)

# function used to sort a list
def sortFunction(val):
    return val[1]

#
# Implements search algorithms:
# 1) Breadth-first search (BuscaLargura)
# 2) Depth-first search (BuscaProfundidade)
# 3) Iterative deepening search (BPI)
# 4) Uniform cost search (CustoUniforme)
# 5) Greddy search algorithm (BuscaGananciosa)
# 6) A* search algorithm (AEstrela)
# 7) hill-climing search algorithms
#

class SearchAlgorithm:
    def search(self):
        pass

#
# This class implements the Breadth-first search
#
class BuscaLargura (SearchAlgorithm):

    def search (self, initialState): 
        #Creating a Queue
        open = deque()
        open.append(Node(initialState, None))
        while (len(open) > 0):
            n = open.popleft()
            if (n.state.is_goal()):
                return n
            for i in n.state.sucessors():
                open.append(Node(i,n))
        return None

#
# This class implements the Depth-first search (limited)
#
class BuscaProfundidade (SearchAlgorithm):

    def search (self, initialState, m): 
        #Using list as stack
        open = []
        open.append(Node(initialState, None))
        while (len(open) > 0):
            n = open.pop()
            if (n.state.is_goal()):
                return n
            if (n.depth < m):
                for i in n.state.sucessors():
                    open.append(Node(i,n))
        return None

#
# This class implements Iterative Deepening Depth-first search
#
class BuscaProfundidadeIterativa (SearchAlgorithm):

    def search (self, initialState): 
        n = 1
        algorithm = BuscaProfundidade()
        while True:
            result = algorithm.search(initialState, n)
            if (result != None):
                return result
            n = n+1

#
# This class implements a Uniform cost search algorithm
#
class BuscaCustoUniforme (SearchAlgorithm):

    def search (self, initialState):
        open = []
        new_n = Node(initialState, None)
        open.append((new_n, new_n.g))
        while (len(open) > 0):
            #list sorted by g()
            open.sort(key = sortFunction, reverse = True)
            n = open.pop()[0]
            if (n.state.is_goal()):
                return n
            for i in n.state.sucessors():
                new_n = Node(i,n)
                open.append((new_n,new_n.g))
        return None
    
#
# This class implements a Greddy search algorithm
#
class BuscaGananciosa (SearchAlgorithm):

    def search (self, initialState):
        open = []
        new_n = Node(initialState, None)
        open.append((new_n, new_n.h()))
        while (len(open) > 0):
            #list sorted by h()
            open.sort(key = sortFunction, reverse = True)
            n = open.pop()[0]
            if (n.state.is_goal()):
                return n
            for i in n.state.sucessors():
                new_n = Node(i,n)
                open.append((new_n, new_n.h()))
        return None

#
# This class implements a A* search algorithm
#
class AEstrela (SearchAlgorithm):

    def search (self, initialState):
        states = []
        open = []
        new_n = Node(initialState, None)
        open.append((new_n, new_n.f()))
        while (len(open) > 0):
            #list sorted by f()
            open.sort(key = sortFunction, reverse = True)
            n = open.pop()[0]
            logging.debug(n.state.env()+" -- "+str(n.f())+" -- "+str(n.h()))

            if (n.state.is_goal()):
                return n
            for i in n.state.sucessors():
                new_n = Node(i,n)
                # eh necessario descrever o conteudo do estado
                # para verificar se ele já foi instanciado ou nao
                if (new_n.state.env() not in states):
                    open.append((new_n,new_n.f()))
                    # nao eh adiciona o estado ao vetor.
                    # eh adicionado o conteudo
                    states.append(new_n.state.env())
                    logging.debug(len(states))
                else: 
                    logging.debug('nao entrou')
        return None

class SubidaMontanha (SearchAlgorithm):

    def best(self, successors):
        best_state = successors[0]
        for i in successors:
            if i.h() < best_state.h():
                best_state = i
        return best_state

    def search (self, initialState):
        atual = initialState
        while True:
            prox = self.best(atual.sucessors())
            if prox.h() >= atual.h():
                return atual
            atual = prox

class SubidaMontanha2 (SearchAlgorithm):

    def best(self, successors):
        best_state = successors[0]
        for i in successors:
            if i.h() < best_state.h():
                best_state = i
        return best_state

    def search (self, initialState):
        atual = initialState
        while True:
            prox = self.best(atual.sucessors())
            if prox.h() >= atual.h():
                if atual.is_goal():
                    return atual
                else: 
                    atual.randomBoard()
            else:
                atual = prox

