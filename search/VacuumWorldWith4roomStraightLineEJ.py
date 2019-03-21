from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from Graph import State

class VacuumWorldWith4roomStraightLine(State):
	
	def __init__(self, left, right, left1, right1, vacuum, operator):
		self.left = left
		self.right = right
		self.left1 = left1
		self.right1 = right1
		self.vacuum = vacuum
		self.operator = operator
		
	def sucessors(self):
		sucessors = []
		sucessors.append(VacuumWorldWith4roomStraightLine(self.left, self.right, self.left, self.left1, 'right', 'Move Right'))
		sucessors.append(VacuumWorldWith4roomStraightLine(self.left, self.right, self.left, self.left1, 'left', 'Move Left'))
		
		if (self.vacuum == 'left'):
			sucessors.append(VacuumWorldWith4roomStraightLine(self.left, True, self.left1, True, self.vacuum, 'clean'))
		else:
			sucessors.append(VacuumWorldWith4roomStraightLine(True, self.right1, True, self.right1,self.vacuum, 'clean'))
		
		return sucessors
		
	def is_goal(self):
		return self.left and self.right and self.right1 and self.left1
		
	

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorldWith4roomStraightLine(False, False, False, False,'left', '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:def description(self):
		return "Resolvendo 4 quartos"
		
	def cost(self):
		return 1
	
	def print(self):
		return str(self.operator)
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    #
    # Executando busca em profundidade
    #
    state = VacuumWorldWith4roomStraightLine(False, False, False, False,'left', '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
    