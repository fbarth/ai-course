from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from Graph import State

# 
# Implements a simplified version of vacuum world problem
# with 4 rooms
#
#   -----------
#   | TL | TR |   
#   -----------
#   | BL | BR |
#   -----------
#
# Initial state:
#	VacuumPos: TopLeft
#	TopLeftRoom: Dirty
#	TopRightRoom: Dirty
#   BottomLeft: Dirty
#   BottomRight: Dirty
# Operations: 
#	Move Vacuum Left
#	Move Vacuum Right
#   Move Vacuum Up
#   Move Vacuum Down
#	Clean
# Final state: 
#	All Rooms are clean
#

class VacuumWorld(State):

    def __init__(self, vacuumPositionVertical, vacuumPositionHorizontal, isTopLeftRoomClean, isTopRightRoomClean, isBottomLeftRoomClean, isBottomRightRoomClean, op):
        self.vacuumPositionVertical = vacuumPositionVertical # [Top, Bottom]
        self.vacuumPositionHorizontal = vacuumPositionHorizontal # [Left, Right]
        self.isTopLeftRoomClean = isTopLeftRoomClean #[True, False]
        self.isTopRightRoomClean = isTopRightRoomClean #[True, False]
        self.isBottomLeftRoomClean = isBottomLeftRoomClean #[True, False]
        self.isBottomRightRoomClean = isBottomRightRoomClean #[True, False]
        self.operator = op # string that describes the operation
    
    def sucessors(self):
        sucessors = []

        if(self.vacuumPositionVertical == 'top'):
            sucessors.append(VacuumWorld('bottom', self.vacuumPositionHorizontal, self.isTopLeftRoomClean, self.isTopRightRoomClean, self.isBottomLeftRoomClean, self.isBottomRightRoomClean, 'Move Down'))
        else:
            sucessors.append(VacuumWorld('top', self.vacuumPositionHorizontal, self.isTopLeftRoomClean, self.isTopRightRoomClean, self.isBottomLeftRoomClean, self.isBottomRightRoomClean, 'Move Up'))

        if(self.vacuumPositionHorizontal == 'right'):
            sucessors.append(VacuumWorld(self.vacuumPositionVertical, 'left', self.isTopLeftRoomClean, self.isTopRightRoomClean, self.isBottomLeftRoomClean, self.isBottomRightRoomClean, 'Move Left'))
        else:
            sucessors.append(VacuumWorld(self.vacuumPositionVertical, 'right', self.isTopLeftRoomClean, self.isTopRightRoomClean, self.isBottomLeftRoomClean, self.isBottomRightRoomClean, 'Move Right'))

		
		#Implementar ações de limpeza

        if (self.vacuumPositionVertical == 'top' and self.vacuumPositionHorizontal == 'left'):
            sucessors.append(VacuumWorld(self.vacuumPositionVertical, self.vacuumPositionHorizontal, True, self.isTopRightRoomClean, self.isBottomLeftRoomClean, self.isBottomRightRoomClean, 'clean'))
        elif(self.vacuumPositionVertical == 'top' and self.vacuumPositionHorizontal == 'right'):
            sucessors.append(VacuumWorld(self.vacuumPositionVertical, self.vacuumPositionHorizontal, self.isTopLeftRoomClean, True, self.isBottomLeftRoomClean, self.isBottomRightRoomClean, 'clean'))
        elif(self.vacuumPositionVertical == 'bottom' and self.vacuumPositionHorizontal == 'left'):
            sucessors.append(VacuumWorld(self.vacuumPositionVertical, self.vacuumPositionHorizontal, self.isTopLeftRoomClean, self.isTopRightRoomClean, True, self.isBottomRightRoomClean, 'clean'))
        else:
            sucessors.append(VacuumWorld(self.vacuumPositionVertical, self.vacuumPositionHorizontal, self.isTopLeftRoomClean, self.isTopRightRoomClean, self.isBottomLeftRoomClean, True, 'clean'))

        return sucessors
    
    def is_goal(self):
        return (self.isTopLeftRoomClean and self.isTopRightRoomClean and self.isBottomLeftRoomClean and self.isBottomRightRoomClean)
    
    def description(self):
        return "Problema do aspirador de pó, contendo quatro salas"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

    def equals(self, VacuumWorld):
        return (self.vacuumPositionHorizontal == VacuumWorld.vacuumPositionHorizontal 
                and self.vacuumPositionVertical == VacuumWorld.vacuumPositionVertical
                and self.isTopLeftRoomClean == VacuumWorld.isTopLeftRoomClean
                and self.isTopRightRoomClean == VacuumWorld.isTopRightRoomClean
                and self.isBottomLeftRoomClean == VacuumWorld.isBottomLeftRoomClean
                and self.isBottomRightRoomClean == VacuumWorld.isBottomRightRoomClean)

def main():
    
    #
    # Executando busca em largura
    #
    print('Busca em largura')
    state = VacuumWorld('bottom', 'left', False, False, False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    # #
    # # Executando busca em profundidade
    # #
    # print('Busca em profundidade')
    # state = VacuumWorld('top', 'left', False, False, False, False, '')
    # algorithm = BuscaProfundidade()
    # result = algorithm.search(state, 10)
    # if result != None:
    #     print('Achou!')
    #     print(result.show_path())
    # else:
    #     print('Nao achou solucao')

    # #
    # # Executando busca em profundidade iterativa
    # #
    print('Busca em profundidade iterativa')
    state = VacuumWorld('top', 'left', False, False, False, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

    # #
    # # Executando busca de custo uniforme
    # #
    # print('Busca de custo uniforme')
    # state = VacuumWorld('top', 'left', False, False, False, False, '')
    # algorithm = BuscaCustoUniforme()
    # result = algorithm.search(state)
    # if result != None:
    #     print('Achou!')
    #     print(result.show_path())
    # else:
    #     print('Nao achou solucao')

if __name__ == '__main__':
    main()