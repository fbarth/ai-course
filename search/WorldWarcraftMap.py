from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from Graph import State
import time
import networkx as nx
import math
import csv

#
# @author Lucas Cilento
# May, 2021
#

class WorldWarcraftMap(State):

    def __init__(self, city, cost, op, goal):
        self.city = city
        self.cost_value = cost
        self.operator = op
        self.goal = goal
    
    def sucessors(self):
        sucessors = []
        neighbors = WorldWarcraftMap.area[self.city]
        for next_city in neighbors:
            sucessors.append(WorldWarcraftMap(next_city[1], next_city[0], next_city[1], self.goal))
        return sucessors
    
    def is_goal(self):
        return (self.city == self.goal)
    
    def description(self):
        return "The map of cities with road distances"
    
    def cost(self):
        return self.cost_value
    
    def print(self):
        return str(self.operator)
    
    def env(self):
        return self.city+"#"+str(self.cost())

    def h(self):
        return int(WorldWarcraftMap.g.edges[self.city,self.goal]['distance'])

    @staticmethod
    def createArea():
        WorldWarcraftMap.info = []
        #
        # Formato do texto de entrada: 
        # 'Cidade',CoordenadaX,CoordenadaY,'Cidade Adjacente 1','Cidade Adjacente 2', etc...
        #
        f = csv.reader(open("WorldWarcraftMapAreaInput.txt", "r"))
        for row in f:
            destinations = []
            for x in range(3, len(row)):
                destinations.append(row[x])
            WorldWarcraftMap.info.append([row[0],row[1],row[2],destinations])
        WorldWarcraftMap.area = {}
        for city in WorldWarcraftMap.info:
            aux = []
            for possibleDestination in city[3]:
                aux.append((calculatePointDistance([int(city[1]), int(city[2])], getCityCoords(possibleDestination, WorldWarcraftMap.info)),possibleDestination))
            WorldWarcraftMap.area[city[0]] = (aux)

    @staticmethod
    def createHeuristics():
        WorldWarcraftMap.heuristics = []
        for xCity in WorldWarcraftMap.info:
            aux = [xCity[0]]
            for yCity in WorldWarcraftMap.info:
                aux.append([yCity[0],calculatePointDistance([int(xCity[1]), int(xCity[2])], [int(yCity[1]), int(yCity[2])])])
            WorldWarcraftMap.heuristics.append(aux)

        WorldWarcraftMap.g = nx.Graph()
        for city in WorldWarcraftMap.heuristics:
            for destination in city:
                if len(destination[0]) > 1:
                    WorldWarcraftMap.g.add_edge(city[0],destination[0], distance = destination[1])

def calculatePointDistance(a, b):
    return math.sqrt(math.pow((b[0] - a[0]), 2) + math.pow((b[1] - a[1]), 2))

def getCityCoords(cityName, mapInfo):
    for row in mapInfo:
        if row[0] == cityName:
            return [int(row[1]), int(row[2])]
    return "Cidade não encontrada."

def main():
    WorldWarcraftMap.createArea()
    WorldWarcraftMap.createHeuristics()

    start = 'Ahn Qiraj'
    end = 'Silvermoon'
    print('\nBusca por algoritmo A* (de {} a {}):\n'.format(start, end))
    state = WorldWarcraftMap(start, 0, start, end)
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print('\nCusto total da solução: '+str(result.g))
    else:
        print('Não achou solução')
    print('Tempo de processamento em segundos: {}\n'.format(str(tf-ts)))
    

if __name__ == '__main__':
    main()
