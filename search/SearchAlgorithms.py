from collections import deque
from Graph import Node

class SearchAlgorithm:
    def search(self):
        pass

#
# This class implements Breadth-first search
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
# This class implements Depth-first search
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