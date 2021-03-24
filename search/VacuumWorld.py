from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State

# 
# Implements a simplified version of vacuum world problem
#
# Initial state:
#	VacuumPos: Left
#	LeftRoom: Dirty
#	RightRoom: Dirty
# Operations: 
#	Move Vacuum Left
#	Move Vacuum Right
#	Clean
# Final state: 
#	Both Rooms are clean
#

class VacuumWorld(State):

    def __init__(self, vacuumPosition, isLeftRoomClean, isRightRoomClean, op):
        self.vacuumPosition = vacuumPosition # [right, left]
        self.isLeftRoomClean = isLeftRoomClean #[True, False]
        self.isRightRoomClean = isRightRoomClean #[True, False]
        self.operator = op # string that describes the operation

    def env(self):
        return str(self.vacuumPosition)+";"+str(self.isLeftRoomClean)+";"+str(self.isRightRoomClean)
    
    def sucessors(self):
        sucessors = []
        # É necessario verificar a VacuumPos antes de mover a Vacuum?
        # Nao eh necessario
        sucessors.append(VacuumWorld('right', self.isLeftRoomClean, self.isRightRoomClean, 'Move Right'))
        sucessors.append(VacuumWorld('left', self.isLeftRoomClean, self.isRightRoomClean, 'Move Left'))
		
		#Implementar ações de limpeza. Importante: Verificar qual a VacuumPos e se a posição está suja
		#Como designar sucessors condicionais?
        if (self.vacuumPosition == 'right'):
            sucessors.append(VacuumWorld(self.vacuumPosition, self.isLeftRoomClean, True, 'clean'))
        else:
            sucessors.append(VacuumWorld(self.vacuumPosition, True, self.isRightRoomClean, 'clean'))
        
        return sucessors
    
    def is_goal(self):
        return (self.isLeftRoomClean and self.isRightRoomClean and (self.vacuumPosition == 'left'))
    
    def description(self):
        return "Problema do aspirador de pó, contendo duas salas"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorld('left', False, False, '')
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
    state = VacuumWorld('left', False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
