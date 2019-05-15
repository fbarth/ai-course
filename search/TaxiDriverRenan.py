from SearchAlgorithms import AEstrela
from Graph import State


class TaxiDriver(State):

    # Renan Miguel 11710867

    # where = [2,5]
    # customer = [5,4]
    # blocks = [[0,1], [1,4], [2,4],[3,4],[4,4]]
    # size = 100

    where = [3,0]
    customer = [1,0]
    blocks = [[2,0], [1,1], [1,2], [1,3], [3,1]]
    size = 10

    def __init__(self, taxi, onBoard, op):
        self.taxi = taxi
        self.onBoard = onBoard
        self.operator = op

    def env(self):
        return "onBoard: " + str(self.onBoard) + " ->  Position taxi: " + str(self.taxi) + " -> target: " + str(self.taxi == self.where)  # self.customer

    def sucessors(self):
        sucessors = []

        if (self.taxi[0] - 1 >= 0 and self.taxiCanGo(self.taxi[0] - 1, self.taxi[1])):
            sucessors.append(TaxiDriver([self.taxi[0] - 1, self.taxi[1]], self.onBoard, 'up'))

        if (self.taxi[0] + 1 >= 0 and self.taxiCanGo(self.taxi[0] + 1, self.taxi[1])):
            sucessors.append(TaxiDriver([self.taxi[0] + 1, self.taxi[1]], self.onBoard, 'down'))

        if (self.taxi[1] - 1 >= 0 and self.taxiCanGo(self.taxi[0], self.taxi[1]-1)):
            sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1] - 1], self.onBoard, 'left'))

        if (self.taxi[1] + 1 >= 0 and self.taxiCanGo(self.taxi[0], self.taxi[1] + 1)):
            sucessors.append(TaxiDriver([self.taxi[0], self.taxi[1] + 1], self.onBoard, 'right'))

        if(self.taxi == self.customer and (not self.onBoard)):
            sucessors.append(TaxiDriver(self.taxi, True, 'take customer'))

        return sucessors

    def is_goal(self):
        return self.onBoard and (self.taxi == self.where)

    def description(self):
        return "Describe the problem"

    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if (self.onBoard):
            return abs(self.taxi[0] - self.where[0]) + abs(self.taxi[1] - self.where[1])
        else:
            return (abs(self.taxi[0] - self.customer[0]) + abs(self.taxi[1] - self.customer[1])) + self.size * 10

    def taxiCanGo(self, x, y):
        for block in self.blocks:
            if (x == block[0] and y == block[1]):
                return False
        return True


def main():
    print('Busca A*')

    taxi = [0, 0]
    state = TaxiDriver(taxi, False, '')

    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()
