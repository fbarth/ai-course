from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):
    # Igor Ehlert - 11710374
    # Vinícius Gomes - 11710390

    # passenger = [15,2]
    # destination = [19,19]
    # size = 20
    # blocks = [[1,1],[2,0]]

    passenger = [3,2]
    destination = [0,0]
    size = 4
    blocks = [[1,1],[2,1],[3,1],[1,2],[1,2],[2,2]]

    def __init__(self, taxi, onboard, op):
        self.operator = op
        self.taxi = taxi
        self.onboard = onboard

    def printEnv(self):
        return 'Comando' #self.customer
    
    def sucessors(self):
        sucessors = []
        #print(self.taxi)
        if(self.taxi[1]-1 >= 0 and self.isblocked(self.taxi[0], self.taxi[1]-1)):
            sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1]-1], self.onboard,  'Move Left'))
            
        if(self.taxi[1]+1 < self.size and self.isblocked(self.taxi[0], self.taxi[1]+1)):
            sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1]+1], self.onboard,  'Move Right'))

        if(self.taxi[0]-1 >= 0 and self.isblocked(self.taxi[0]-1, self.taxi[1])):
            sucessors.append(TaxiDriver([self.taxi[0]-1, self.taxi[1]], self.onboard,  'Move Up'))

        if(self.taxi[0]+1 < self.size and self.isblocked(self.taxi[0]+1, self.taxi[1])):
            sucessors.append(TaxiDriver([self.taxi[0]+1, self.taxi[1]], self.onboard,  'Move Down'))
            
        if(self.onboard == False and self.taxi == self.passenger):
            sucessors.append(TaxiDriver(self.taxi,  True,  'Embarcou'))
    
        return sucessors
    
    def is_goal(self):
        return (self.taxi == self.destination) and self.onboard == True
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if (self.onboard):
            return abs(self.taxi[0] - self.destination[0]) + abs(self.taxi[1] - self.destination[1])
        else:
            return (abs(self.taxi[0] - self.passenger[0]) + abs(self.taxi[1] - self.passenger[1])) + self.size * 10

    def isblocked(self, row, col):
        for block in self.blocks:
            if (row == block[0] and col == block[1]):
                return False
        
        return True



def main():
    print('Busca A*')
    state = TaxiDriver([3,0], False, '')
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
        print('Desembarcou')
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()