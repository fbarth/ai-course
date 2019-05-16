from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):

    passanger = [2,7] #[4,5]
    destiny = [5,2]
    blocks = [[0,4],[1,4],[2,4],[3,4],[4,4],[5,4]]
    size = 10

    # passanger = [4,5]
    # destiny = [0,0]
    # blocks = [[0,4],[1,4],[2,4],[3,4],[4,4],[5,4]]
    # size = 7

    # passanger = [8,5]
    # destiny = [9,0]
    # blocks = [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5]]
    # size = 10

    # passanger = [8,5]
    # destiny = [9,0]
    # blocks = [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[6,4],[7,4],[8,4],[9,4]]
    # size = 10

    def isPossible(self, taxi):
        for block in self.blocks:
            if (block == taxi):
                return False
        return True

    def __init__(self, taxi, passangerOnBoard, op):
        self.operator = op
        self.taxi = taxi 
        self.passangerOnBoard = passangerOnBoard

    def env(self):
        return str(self.operator)+str(self.taxi)+str(self.passangerOnBoard)
    
    def sucessors(self):
        sucessors = []
        #move up
        if(self.taxi[0]-1 >=0 and self.isPossible([self.taxi[0]-1, self.taxi[1]])):
            t = TaxiDriver([self.taxi[0]-1, self.taxi[1]], self.passangerOnBoard, "move up")
            sucessors.append(t)
        #move down
        if(self.taxi[0]+1 < self.size and self.isPossible([self.taxi[0]+1, self.taxi[1]])):
            t = TaxiDriver([self.taxi[0]+1, self.taxi[1]], self.passangerOnBoard, "move down")
            sucessors.append(t)
        #move left
        if(self.taxi[1]-1 >=0 and self.isPossible([self.taxi[0], self.taxi[1]-1])):
            t = TaxiDriver([self.taxi[0], self.taxi[1]-1], self.passangerOnBoard, "move left")
            sucessors.append(t)
        #move right
        if(self.taxi[1]+1 < self.size and self.isPossible([self.taxi[0], self.taxi[1]+1])):
            t = TaxiDriver([self.taxi[0], self.taxi[1]+1], self.passangerOnBoard, "move right")
            sucessors.append(t)
        #pick passanger
        if((not self.passangerOnBoard) and (self.taxi == self.passanger)):
            t = TaxiDriver(self.taxi, True, "pick passanger")
            sucessors.append(t)

        return sucessors
    
    def is_goal(self):
        return self.passangerOnBoard and (self.destiny == self.taxi)
    
    def description(self):
        return "Taxi que precisa pegar um passageiro e levar ateh o destino, respeitando os obstáculos"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if(self.passangerOnBoard):
            return abs(self.taxi[0] - self.destiny[0]) + abs(self.taxi[1] - self.destiny[1])
        else:
            # uma vez que vc pega o passageiro vc deve despriorizar os caminhos que levam ao passageiro
            return abs(self.taxi[0] - self.passanger[0]) + abs(self.taxi[1] - self.passanger[1]) + self.size*10


def main():
    print('Busca A *')
    state = TaxiDriver([0,0], False, '')
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path()+ " ; drop passanger")
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()