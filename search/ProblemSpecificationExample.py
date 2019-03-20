from Graph import State

class PlusOneTwo(State):

    def __init__(self, op):
        self.operator = op
        #TODO
    
    def sucessors(self):
        sucessors = []
        #TODO
        return sucessors
    
    def is_goal(self):
        pass
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)


def main():
    pass

if __name__ == '__main__':
    main()