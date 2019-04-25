from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):

    def __init__(self, op, maze, taxiPosition, passengerPosition, goalPosition, hasPassenger):
        self.operator = op
        self.maze = maze
        self.taxiPosition = taxiPosition
        self.passengerPosition = passengerPosition
        self.goalPosition = goalPosition
        self.hasPassenger = hasPassenger
    
    def sucessors(self):
        sucessors = []
        #TODO: Implementar barreira
        print(str(self.taxiPosition[0]) + ',' + str(self.taxiPosition[1]) + ' ' + str(self.hasPassenger))
        if((not self.hasPassenger) and (self.taxiPosition == self.passengerPosition)):
            print("vai pegar o passageiro")
            sucessors.append(TaxiDriver('Pegar Passageiro', self.maze, self.taxiPosition, None, self.goalPosition, True))
        if((self.taxiPosition[0] - 1 >= 0) and (self.maze[self.taxiPosition[0]][self.taxiPosition[1]] != 'B')):
            sucessors.append(TaxiDriver('Subir', self.maze, [self.taxiPosition[0] - 1, self.taxiPosition[1]], self.passengerPosition, self.goalPosition, self.hasPassenger))
        if((self.taxiPosition[1] - 1 >= 0) and (self.maze[self.taxiPosition[0]][self.taxiPosition[1]] != 'B')):
            sucessors.append(TaxiDriver('Esquerda', self.maze, [self.taxiPosition[0], self.taxiPosition[1] - 1], self.passengerPosition, self.goalPosition, self.hasPassenger))
        if((self.taxiPosition[0] + 1 < len(self.maze)) and (self.maze[self.taxiPosition[0]][self.taxiPosition[1]] != 'B')):
            sucessors.append(TaxiDriver('Descer', self.maze, [self.taxiPosition[0] + 1, self.taxiPosition[1]], self.passengerPosition, self.goalPosition, self.hasPassenger))
        if((self.taxiPosition[1] + 1 < len(self.maze[0])) and (self.maze[self.taxiPosition[0]][self.taxiPosition[1]] != 'B')):
            sucessors.append(TaxiDriver('Direita', self.maze, [self.taxiPosition[0], self.taxiPosition[1] + 1], self.passengerPosition, self.goalPosition, self.hasPassenger))

        return sucessors
    
    def is_goal(self):
        return ((self.taxiPosition == self.goalPosition) and (self.hasPassenger))
    
    def description(self):
        return "Taxi Driver"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if(not self.hasPassenger):
            return abs((self.taxiPosition[0] - self.passengerPosition[0]) + (self.taxiPosition[1] - self.passengerPosition[1])) + 10
        else:
            return abs((self.taxiPosition[0] - self.goalPosition[0]) + (self.taxiPosition[1] - self.goalPosition[1]))



def main():
    print('Busca A *')

    maze = [[" "," "," "," "," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "],
            [" "," "," ","B"," "," "," "," "," "," "]]

    taxi = [0,0]
    passenger = [7,8]
    goal = [4,2]
    state = TaxiDriver('', maze, taxi, passenger, goal, False)
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path() + ', deixar o passageiro')
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()