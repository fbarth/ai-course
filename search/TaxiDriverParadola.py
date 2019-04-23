from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State

class TaxiDriver(State):

    def __init__(self, taxiPosition, passengerPosition, destination, onboard, rowLen, colLen, op):
        self.operator = op
        self.taxiPosition = taxiPosition
        self.passengerPosition = passengerPosition
        self.destination = destination
        self.onboard = onboard
        self.rowLen = rowLen
        self.colLen = colLen
    
    def sucessors(self):
        sucessors = []
        #print(self.taxiPosition)
        if(self.taxiPosition == self.destination and self.onboard == True):
            sucessors.append(TaxiDriver(self.taxiPosition, self.passengerPosition, self.destination, self.onboard, self.rowLen, self.colLen, 'Chegou ao seu destino'))
        else:
            if(self.taxiPosition[1]-1 >= 0):
                sucessors.append(TaxiDriver([self.taxiPosition[0], self.taxiPosition[1]-1], self.passengerPosition, self.destination, self.onboard, self.rowLen, self.colLen, 'Move Left'))
            if(self.taxiPosition[1]+1 < self.colLen):
                sucessors.append(TaxiDriver([self.taxiPosition[0], self.taxiPosition[1]+1], self.passengerPosition, self.destination, self.onboard, self.rowLen, self.colLen, 'Move Right'))
            if(self.taxiPosition[0]-1 >= 0):
                sucessors.append(TaxiDriver([self.taxiPosition[0]-1, self.taxiPosition[1]], self.passengerPosition, self.destination, self.onboard, self.rowLen, self.colLen, 'Move Up'))
            if(self.taxiPosition[0]+1 < self.rowLen):
                sucessors.append(TaxiDriver([self.taxiPosition[0]+1, self.taxiPosition[1]], self.passengerPosition, self.destination, self.onboard, self.rowLen, self.colLen, 'Move Down'))
            if(self.taxiPosition == self.passengerPosition):
                sucessors.append(TaxiDriver(self.taxiPosition, self.passengerPosition, self.destination, True, self.rowLen, self.colLen, 'Embarcou'))
    
        return sucessors
    
    def is_goal(self):
        return (self.taxiPosition == self.destination and self.onboard == True)
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        pass


def main():
    print('Busca em profundidade iterativa')
    state = TaxiDriver([0,0], [2,3], [1,1], False, 3, 4, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()