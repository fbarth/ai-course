from collections import deque
from Graph import Node

#
# Implements search algorithms:
# 1) Breadth-first search (BuscaLargura)
# 2) Depth-first search (BuscaProfundidade)
# 3) Iterative deepening search (BPI)
# 4) Uniform cost search (CustoUniforme)
# 5) others TODO
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
        result = None
        algorithm = BuscaProfundidade()
        while True:
            result = algorithm.search(initialState, n)
            if (result != None):
                return result
            n = n+1