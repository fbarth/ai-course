from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):

    #Pedro GMR Basso 11529904

    originPosition = [0,0]
    passengerPosition = [2,4]
    destinationPosition = [0,0]
    maze = [[ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [ 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [ 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [ 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [ 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, op, taxiPosition, hasPassenger):
        self.operator = op
        self.taxiPosition = taxiPosition
        self.hasPassenger = hasPassenger
        self.origin_position = taxiPosition
    
    #Check if the next desirable position isn't a barrier
    def isPositionPossible (self, taxiPosition):
        return (self.maze[taxiPosition[0]][taxiPosition[1]] == 0)

    def sucessors(self):
        sucessors = []

        #Go UP
        if((self.taxiPosition[0] - 1 >= 0) and (self.isPositionPossible([self.taxiPosition[0] - 1, self.taxiPosition[1]]))):
            sucessors.append(TaxiDriver('Go Up', [self.taxiPosition[0] - 1, self.taxiPosition[1]], self.hasPassenger))

        #Go DOWN
        if((self.taxiPosition[0] + 1 < len(self.maze)) and (self.isPositionPossible([self.taxiPosition[0] + 1, self.taxiPosition[1]]))):
            sucessors.append(TaxiDriver('Go Down', [self.taxiPosition[0] + 1, self.taxiPosition[1]], self.hasPassenger))

        #Go LEFT
        if((self.taxiPosition[1] - 1 >= 0) and (self.isPositionPossible([self.taxiPosition[0], self.taxiPosition[1] - 1]))):
            sucessors.append(TaxiDriver('Go Left', [self.taxiPosition[0], self.taxiPosition[1] - 1], self.hasPassenger))
        
        #Go RIGHT
        if((self.taxiPosition[1] + 1 < len(self.maze[0])) and (self.isPositionPossible([self.taxiPosition[0], self.taxiPosition[1] + 1]))):
            sucessors.append(TaxiDriver('Go Right', [self.taxiPosition[0], self.taxiPosition[1] + 1], self.hasPassenger))

        #Pick up passenger
        if((not self.hasPassenger) and (self.taxiPosition == self.passengerPosition)):
            sucessors.append(TaxiDriver('Pick Up', self.taxiPosition, True))

        return sucessors
    
    def env(self):
        return str(self.operator)+str(self.taxiPosition)+str(self.hasPassenger)
    
    def is_goal(self):
        return ((self.taxiPosition == self.destinationPosition) and (self.hasPassenger))
    
    def description(self):
        return "Taxi Driver"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if(not self.hasPassenger):
            return abs(self.taxiPosition[0] - self.passengerPosition[0]) + abs(self.taxiPosition[1] - self.passengerPosition[1]) + 10*len(self.maze)
        else:
            return abs(self.taxiPosition[0] - self.destinationPosition[0]) + abs(self.taxiPosition[1] - self.destinationPosition[1])



def main():
    print('A* Algorithm')
    taxi = [1,0]

    state = TaxiDriver('Start', taxi, False)
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Solution Found!')
        print(result.show_path() + ' ; Drop Passenger')
    else:
        print('No Solution =(')

if __name__ == '__main__':
    main()
