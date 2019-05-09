from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):

    taxi_origin = [0,0]
    passenger_origin = [4,5]
    goal = [5,2]
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def isValidPosition(self, taxiPosition):
        return (self.maze[taxiPosition[0]][taxiPosition[1]] == 0)

    def __init__(self, op, taxiPosition, hasPassenger):
        self.operator = op
        self.taxiPosition = taxiPosition
        self.hasPassenger = hasPassenger
        self.taxi_origin = taxiPosition

    def sucessors(self):
        sucessors = []
        #print(str(self.taxiPosition[0]) + ',' + str(self.taxiPosition[1]) + ' ' + str(self.hasPassenger) + ' ' + str(self.h()))

        #Subir no mapa
        if((self.taxiPosition[0] - 1 >= 0) and (self.isValidPosition([self.taxiPosition[0] - 1, self.taxiPosition[1]]))):
            sucessors.append(TaxiDriver('Subir', [self.taxiPosition[0] - 1, self.taxiPosition[1]], self.hasPassenger))
        
        #Descer no Mapa
        if((self.taxiPosition[0] + 1 < len(self.maze)) and (self.isValidPosition([self.taxiPosition[0] + 1, self.taxiPosition[1]]))):
            sucessors.append(TaxiDriver('Descer', [self.taxiPosition[0] + 1, self.taxiPosition[1]], self.hasPassenger))
        
        #Ir para a Esquerda no mapa
        if((self.taxiPosition[1] - 1 >= 0) and (self.isValidPosition([self.taxiPosition[0], self.taxiPosition[1] - 1 ]))):
            sucessors.append(TaxiDriver('Esquerda', [self.taxiPosition[0], self.taxiPosition[1] - 1], self.hasPassenger))
         
        #Ir para a Direita no Mapa
        if((self.taxiPosition[1] + 1 < len(self.maze[0])) and (self.isValidPosition([self.taxiPosition[0], self.taxiPosition[1] + 1 ]))):
            sucessors.append(TaxiDriver('Direita', [self.taxiPosition[0], self.taxiPosition[1] + 1], self.hasPassenger))


        #Pegar Passageiro
        if((not self.hasPassenger) and (self.taxiPosition == self.passenger_origin)):
            sucessors.append(TaxiDriver('Pegar Passageiro', self.taxiPosition, True))
        
        return sucessors
    
    def is_goal(self):
        return ((self.taxiPosition == self.goal) and (self.hasPassenger))
    
    def description(self):
        return "Taxi Driver"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if(not self.hasPassenger):
            return abs(self.taxiPosition[0] - self.passenger_origin[0]) + abs(self.taxiPosition[1] - self.passenger_origin[1]) + len(self.maze)*10 - (abs(self.taxiPosition[0] - self.taxi_origin[0]) + abs(self.taxiPosition[1] - self.taxi_origin[1]))
        else:
            return abs(self.taxiPosition[0] - self.goal[0]) + abs(self.taxiPosition[1] - self.goal[1]) - (abs(self.taxiPosition[0] - self.passenger_origin[0]) + abs(self.taxiPosition[1] - self.passenger_origin[1]))



def main():
    print('Busca A *')

    taxi = [0,0]
    
    state = TaxiDriver('', taxi, False)
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path() + ', deixar o passageiro')
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()