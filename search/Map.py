from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State

class Map(State):

    area = dict(
        'a',[(3,'b'),(6,'c')],
        'b',[(3,'a'),(3,'h'),(3,'k')],
        'c',[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
        'd',[(3,'c'),(1,'f'),(1,'e')],
        'e',[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
        'f',[(1,'g'),(1,'e'),(1,'d')],
        'g',[(2,'c'),(1,'f'),(2,'h')],
        'h',[(,''),(,''),(,'')],
        'i',[(,''),(,''),(,'')],
        'l',[(,''),(,''),(,'')],
        'k',[(,''),(,''),(,'')],
        'm',[(,''),(,''),(,'')],
        'n',[(,''),(,''),(,'')],
        'o',[(,''),(,''),(,'')],
        'p',[(,''),(,''),(,'')],
        'x',[(,''),(,''),(,'')]
        )

    def __init__(self, city, cost, op, goal):
        self.city = city
        self.cost_value = cost
        self.operator = op
        self.goal = goal
    
    def sucessors(self):
        sucessors = []
        #TODO
        return sucessors
    
    def is_goal(self):
        return (self.city == self.goal)
    
    def description(self):
        return "The map of cities with road distances"
    
    def cost(self):
        #return the cost to get at city "city"
        return self.cost_value

    def print(self):
        return str(self.operator)


def main():
    print('Busca em profundidade iterativa')
    state = Map('h', 0, '', 'o')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()