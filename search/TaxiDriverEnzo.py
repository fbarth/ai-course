from SearchAlgorithms import AEstrela
from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State

# Projeto realizado por Enzo Scapinelli

class TaxiDriver(State):

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
    
    def sucessors(self):
        sucessors = []

        if (self.isPassangerOnBoard == False):
            if(int(self.taxiPositionVertical) >= 0 and int(self.taxiPositionVertical) <= self.size and self.is_not_barrier()):
                sucessors.append(TaxiDriver(self.taxiPositionVertical + 1, self.taxiPositionHorizontal, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Down'))
                sucessors.append(TaxiDriver(self.taxiPositionVertical - 1, self.taxiPositionHorizontal, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Up'))

            if(int(self.taxiPositionHorizontal) >= 0 and int(self.taxiPositionHorizontal) <= self.size and self.is_not_barrier()):
                sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal + 1, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Right'))
                sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal - 1, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Left'))
        else:
            if(int(self.taxiPositionVertical) >= 0 and int(self.taxiPositionVertical) <= self.size and self.is_not_barrier()):
                sucessors.append(TaxiDriver(self.taxiPositionVertical + 1, self.taxiPositionHorizontal, self.passangerPositionVertical + 1, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Down'))
                sucessors.append(TaxiDriver(self.taxiPositionVertical - 1, self.taxiPositionHorizontal, self.passangerPositionVertical - 1, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Up'))

            if(int(self.taxiPositionHorizontal) >= 0 and int(self.taxiPositionHorizontal) <= self.size and self.is_not_barrier()):
                sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal + 1, self.passangerPositionVertical, self.passangerPositionHorizontal + 1, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Right'))
                sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal - 1, self.passangerPositionVertical, self.passangerPositionHorizontal - 1, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Move Left'))

        # Se o Passageiro chegou ao destino
        if(self.destinyPositionHorizontal == self.passangerPositionHorizontal and self.destinyPositionVertical == self.passangerPositionVertical and self.isPassangerOnBoard):
            sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal, self.passangerPositionVertical, self.passangerPositionHorizontal, self.isPassangerOnBoard, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, True, self.size, 'Drop Passanger'))
            

        # Se o Passageiro está dentro do taxi
        if (self.taxiPositionHorizontal == self.passangerPositionHorizontal and self.taxiPositionVertical == self.passangerPositionVertical):
            sucessors.append(TaxiDriver(self.taxiPositionVertical, self.taxiPositionHorizontal, self.passangerPositionVertical, self.passangerPositionHorizontal, True, self.destinyPositionVertical, self.destinyPositionHorizontal, self.barrierPosition, self.isPassangerOnDestiny, self.size, 'Take Passanger'))        

        return sucessors
    
    def is_goal(self):
        return (self.isPassangerOnBoard and self.isPassangerOnDestiny)

    def is_not_barrier(self):

        for i in self.barrierPosition:
            if(self.taxiPositionHorizontal == i[0] and self.taxiPositionVertical == i[1]):
                return False
        return True

    
    def description(self):
        return "Problema de taxi e passageiro"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def h(self):
        if(self.isPassangerOnBoard == False):
            return abs(self.taxiPositionHorizontal - self.passangerPositionHorizontal) + abs(self.taxiPositionVertical - self.passangerPositionVertical)
        else:
            return abs(self.taxiPositionHorizontal - self.destinyPositionHorizontal) + abs(self.taxiPositionVertical - self.destinyPositionVertical)


def main():
    
    taxi = [0,0]
    passager = [3,3] 
    destiny = [0,5]
    barrier = [[1,0],[1,1]]
    size = 6

    print('Busca A*')
    state = TaxiDriver(taxi[0], taxi[1], passager[0], passager[1], False, destiny[0], destiny[1], barrier, False, size, '')
    algorithm = AEstrela()
    #algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()