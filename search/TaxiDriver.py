from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):

    def __init__(self, taxiPosition, matrix, positionDestiny, passenger, op):
        self.taxiPosition = taxiPosition
        self.matrix = matrix
        self.positionDestiny = positionDestiny
        self.operator = op
        self.passenger = passenger
    
    def sucessors(self):
        sucessors = []
        #para cima
        if (self.taxiPosition[0]-1 >= 0):
            sucessors.append(TaxiDriver([self.taxiPosition[0]-1,self.taxiPosition[1]], self.matrix, self.positionDestiny, 'cima'))
        #para baixo
        if (self.taxiPosition[0]+1 < len(self.matrix) and self.taxiPosition[0]+1 > 0):
            sucessors.append(TaxiDriver([self.taxiPosition[0]+1, self.taxiPosition[1]], self.matrix, self.positionDestiny, 'baixo'))
        #para esquerda
        if (self.taxiPosition[1]-1 >= 0):
            sucessors.append(TaxiDriver([self.taxiPosition[0], self.taxiPosition[1]-1], self.matrix, self.positionDestiny, 'esquerda'))
        #para direita
        if (self.taxiPosition[1]+1 < len(self.matrix[0]) and self.taxiPosition[1]+1 > 0 ):
            sucessors.append(TaxiDriver([self.taxiPosition[0],self.taxiPosition[1]+1], self.matrix, self.positionDestiny, 'direita'))
        return sucessors
    
    def is_goal(self):
        return(self.taxiPosition == self.positionDestiny)
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        return 1


def main():
    print('Busca A *')
    matrix = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    state = TaxiDriver([0,0], matrix, [3,2],'')
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()