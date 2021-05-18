from abc import ABC, abstractmethod

class Player(ABC): 

    @abstractmethod
    def move(self, player_code, board):
        pass

    @abstractmethod
    def name(self):
        pass