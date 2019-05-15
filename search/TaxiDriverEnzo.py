from SearchAlgorithms import AEstrela
from Graph import State

# Projeto realizado por Enzo Scapinelli

class TaxiDriver(State):

    road = []
    s = 10

    for x in range(0, s):
        road.append([' '] * s)

    def __init__(self, taxiPositionVertical, taxiPositionHorizontal, passangerPositionVertical, passangerPositionHorizontal, isPassangerOnBoard, destinyPositionVertical, destinyPositionHorizontal, barrierPosition, isPassangerOnDestiny, size, op):
        self.taxiPositionVertical = taxiPositionVertical # Y
        self.taxiPositionHorizontal = taxiPositionHorizontal # X
        self.passangerPositionVertical = passangerPositionVertical # Y
        self.passangerPositionHorizontal = passangerPositionHorizontal # X
        self.isPassangerOnBoard = isPassangerOnBoard
        self.destinyPositionVertical = destinyPositionVertical # Y
        self.destinyPositionHorizontal = destinyPositionHorizontal # X
        self.barrierPosition = barrierPosition
        self.isPassangerOnDestiny = isPassangerOnDestiny
        self.size = size
        self.operator = op # string that describes the operation

    def printEnv(self):
        self.buildRoad()
        return """
        """ + str(self.road[0]) + """
        """ + str(self.road[1]) + """
        """ + str(self.road[2]) + """
        """ + str(self.road[3]) + """
        """ + str(self.road[4]) + self.operator

    def buildRoad(self):
        for x in range(0, self.s):
            for y in range(0, self.s):
                self.road[x][y] = " "

        if (not self.isPassangerOnBoard):
            self.road[self.passangerPositionVertical][self.passangerPositionHorizontal] = "P"
            self.road[self.taxiPositionVertical][self.taxiPositionHorizontal] = "T"
        
        for i in self.barrierPosition:
            self.road[i[0]][i[1]] = "B"

        if(self.isPassangerOnBoard):
            self.road[self.taxiPositionVertical][self.taxiPositionHorizontal] = "X"

        return self.road

    def sucessors(self):
        sucessors = []

        # Move Down
        if(int(self.taxiPositionVertical) <= self.size and self.is_not_barrier()):
            sucessors.append(TaxiDriver(self.taxiPositionVertical + 1, self.taxiPositionHorizontal, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Down'))
        # Move Up
        if(int(self.taxiPositionVertical) > 0 and self.is_not_barrier()):
                sucessors.append(TaxiDriver(self.taxiPositionVertical - 1, self.taxiPositionHorizontal, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Up'))
        # Move Right
        if(int(self.taxiPositionHorizontal) <= self.size and self.is_not_barrier()):
            sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal + 1, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Right'))
        # Move Left
        if(int(self.taxiPositionHorizontal) > 0 and self.is_not_barrier()):
            sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal - 1, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Left'))
        
        # Se o Passageiro está dentro do taxi
        if (self.taxiPositionHorizontal == self.passangerPositionHorizontal and self.taxiPositionVertical == self.passangerPositionVertical):
            sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal, self.passangerPositionVertical, self.passangerPositionHorizontal, True, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Take Passanger'))        
      
        return sucessors
    
    def is_goal(self):
        return (self.isPassangerOnBoard and (self.taxiPositionHorizontal == self.destinyPositionHorizontal and self.taxiPositionVertical == self.destinyPositionVertical))

    def is_not_barrier(self):

        for i in self.barrierPosition:
            if(self.taxiPositionVertical == i[0] and self.taxiPositionHorizontal == i[1]):
                    return False
        return True

    
    def description(self):
        return "Problema de taxi e passageiro"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        tax = 0

        for i in self.barrierPosition:
            if(self.taxiPositionHorizontal + 1 == i[0] or self.taxiPositionHorizontal - 1 == i[0]):
                tax = tax + 1
            elif(self.taxiPositionVertical + 1 == i[1] or self.taxiPositionVertical - 1 == i[0]):
                tax = tax + 1

        if(self.isPassangerOnBoard == False):
            return self.size*(abs(self.taxiPositionHorizontal - self.passangerPositionHorizontal) + abs(self.taxiPositionVertical - self.passangerPositionVertical) + tax) - self.size
        else:    
            return abs(self.taxiPositionHorizontal - self.destinyPositionHorizontal) + abs(self.taxiPositionVertical - self.destinyPositionVertical) + tax


def main():
    
    taxi = [0,4]
    passager = [0,0] 
    destiny = [4,0]
    barrier = [[0,1],[0,2]]
    size = 30

    print('Busca A*')
    state = TaxiDriver(taxi[0], taxi[1], passager[0], passager[1], False, destiny[0], destiny[1], barrier, False, size, '')
    algorithm = AEstrela()
    #algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path()+" ; Drop Passanger")
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
	
