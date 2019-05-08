from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):

    def __init__(self, taxi, matrix, where, customer,took, blocks, drop, op):
        self.matrix = matrix
        self.operator = op
        self.taxi = taxi
        self.where = where
        self.customer = customer
        self.took = took
        self.blocks = blocks
        self.drop = drop

    def printEnv(self):
        return str(self.took)+"   "+str(self.taxi) #self.customer

    def sucessors(self):
        sucessors = []

        if (self.took == False and self.taxi_can_go(self.taxi[0], self.taxi[1], self.blocks)): 
            if (self.taxi[0] - 1 >= 0):
                sucessors.append(TaxiDriver([self.taxi[0]-1, self.taxi[1]], self.matrix, self.where, self.customer,False, self.blocks, False, 'up'))
            
            if (self.taxi[0]+1 < len(self.matrix) and self.taxi[0]+1 > 0):
                sucessors.append(TaxiDriver([self.taxi[0]+1, self.taxi[1]], self.matrix, self.where, self.customer, False, self.blocks, False,'down'))

            if (self.taxi[1]-1 >= 0):
                sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1] - 1], self.matrix, self.where,self.customer, False, self.blocks,False, 'left'))
            
            if (self.taxi[1]+1 < len(self.matrix[0]) and self.taxi[1] + 1 > 0):
                sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1]+1], self.matrix, self.where, self.customer,False, self.blocks, False,'right'))

            if(self.taxi == self.customer):
                sucessors.append(TaxiDriver(self.taxi, self.matrix, self.where, self.customer, True, self.blocks, False, 'take customer'))

        if (self.took == True and self.taxi_can_go(self.taxi[0], self.taxi[1], self.blocks)):
            if (self.taxi[0] - 1 >= 0):
                sucessors.append(TaxiDriver([self.taxi[0]-1, self.taxi[1]], self.matrix, self.where, [self.customer[0]-1, self.customer[1]], True, self.blocks,False, 'up'))
            
            if (self.taxi[0] + 1 < len(self.matrix) and self.taxi[0] + 1 > 0):
                sucessors.append(TaxiDriver([self.taxi[0]+1, self.taxi[1]], self.matrix, self.where, [self.customer[0]+1, self.customer[1]], True, self.blocks, False,'down'))

            if (self.taxi[1] - 1 >= 0):
                sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1] - 1], self.matrix, self.where, [self.customer[0], self.customer[1] - 1] , True, self.blocks, False,'left'))
            
            if (self.taxi[1] + 1 < len(self.matrix[0]) and self.taxi[1] + 1 > 0):
                sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1] + 1], self.matrix, self.where, [self.customer[0], self.customer[1] + 1], True, self.blocks, False,'right'))
        
        if(self.took == True and self.taxi == self.where):
            sucessors.append(TaxiDriver(self.taxi, self.matrix, self.where, self.customer, True, self.blocks, True, 'drop customer'))
        
        return sucessors
    
    def is_goal(self):
        return self.drop == True and self.customer == self.where
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return abs(self.taxi[0]- self.where[0]) + abs(self.taxi[1] - self.where[1])
        
    def print(self):
        return str(self.operator)

    def h(self):
        if (self.took):
            return abs(self.taxi[0] - self.customer[0]) + abs(self.taxi[1] - self.customer[1]) 
        else:
            return abs(self.taxi[0] - self.where[0]) + abs(self.taxi[1] - self.where[1]) + 100
    
    def taxi_can_go(self, x, y, obs):
        for i in obs:
            if (x == i[0] and y == i[1]):
                return False
        
        return True

def main():
    print('Busca A*')
    #matrix = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    matrix = [[0 for col in range(6)] for row in range(6)]
    #state = TaxiDriver([0,0], matrix, [1,2], [1,1], False, [[0,1], [1,1], [2,1]], False, '')
    state = TaxiDriver([5,0], matrix, [5,5], [2,3], False, [[1,2],[2,2],[3,2],[4,2],[5,2],[1,3]], False, '')
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()