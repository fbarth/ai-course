from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from Graph import State

class VacuumWorld4RoomSquare(State):

    def __init__(self, topLeft, topRight, bottomLeft, bottomRight, position, operator):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        self.position = position
        self.operator = operator

    def sucessors(self):
        sucessors = []

        sucessors.append(VacuumWorld4RoomSquare(self.topLeft, self.topRight, self.bottomLeft, self.bottomRight, 'right', 'Move right'))        
        sucessors.append(VacuumWorld4RoomSquare(self.topLeft, self.topRight, self.bottomLeft, self.bottomRight, 'left', 'Move Left'))
        sucessors.append(VacuumWorld4RoomSquare(self.topLeft, self.topRight, self.bottomLeft, self.bottomRight, 'bottom', 'Move bottom'))
        sucessors.append(VacuumWorld4RoomSquare(self.topLeft, self.topRight, self.bottomLeft, self.bottomRight, 'top', 'Move top'))

        if (self.position == 'left'):
            sucessors.append(VacuumWorld4RoomSquare(True, self.topRight, self.bottomLeft, self.bottomRight, self.position, 'clean'))
        elif (self.position == 'bottom'):
            sucessors.append(VacuumWorld4RoomSquare(self.topLeft, self.topRight, True, self.bottomRight, self.position, 'clean'))
        elif (self.position == 'right'):
            sucessors.append(VacuumWorld4RoomSquare(self.topLeft, self.topRight, self.bottomLeft, True, self.position, 'clean'))
        elif (self.position == 'top'):
            sucessors.append(VacuumWorld4RoomSquare(self.topLeft, True, self.bottomLeft, self.bottomRight, self.position, 'clean'))
        
        return sucessors
        
    def is_goal(self):
        return self.topLeft and self.topRight and self.bottomLeft and self.bottomRight
        
    def description(self):
        return "Resolvendo 4 quartos"
    
    def cost(self):
        return 1
        
    def print(self):
        return str(self.operator)

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorld4RoomSquare(False, False, False, False,'bottom', '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    #
    # Executando busca em profundidade
    #
    state = VacuumWorld4RoomSquare(False, False, False, False,'bottom', '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
    