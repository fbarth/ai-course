from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from Graph import State
import time;

class Map(State):

    area = {
        'a':[(3,'b'),(6,'c')],
        'b':[(3,'a'),(3,'h'),(3,'k')],
        'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
        'd':[(3,'c'),(1,'f'),(1,'e')],
        'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
        'f':[(1,'g'),(1,'e'),(1,'d')],
        'g':[(2,'c'),(1,'f'),(2,'h')],
        'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
        'i':[(2,'e'),(2,'h')],
        'l':[(1,'k')],
        'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
        'm':[(2,'n'),(1,'x'),(14,'e')],
        'n':[(2,'m'),(3,'k')],
        'o':[(2,'c')],
        'p':[(2,'c')],
        'x':[(1,'m')]
        }

    def __init__(self, city, cost, op, goal):
        self.city = city
        self.cost_value = cost
        self.operator = op
        self.goal = goal
    
    def sucessors(self):
        sucessors = []
        neighbors = Map.area[self.city]
        for next_city in neighbors:
            sucessors.append(Map(next_city[1], next_city[0], next_city[1], self.goal))
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
    print('Busca em profundidade iterativa: sair de h e chegar em o')
    state = Map('h', 0, 'h', 'o')
    algorithm = BuscaProfundidadeIterativa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))

    print('Busca em profundidade iterativa: sair de i e chegar em x')
    state = Map('i', 0, 'i', 'x')
    algorithm = BuscaProfundidadeIterativa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))

    print('Busca em de custo uniforme: sair de h e chegar em o')
    state = Map('h', 0, 'h', 'o')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))

    print('Busca de custo uniforme: sair de i e chegar em x')
    state = Map('i', 0, 'i', 'x')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))

    print('Busca de custo uniforme: sair de p e chegar em n')
    state = Map('p', 0, 'p', 'n')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))

if __name__ == '__main__':
    main()