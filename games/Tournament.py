from FourInRow import FourInRow
from RandomPlayer import RandomPlayer
from ManualPlayer import ManualPlayer
from BarthPlayer import BarthPlayer

print('Ramdom vs Barth \n')
FourInRow(RandomPlayer(), BarthPlayer()).game()

print('Barth vs Manual \n')
FourInRow(BarthPlayer(), RandomPlayer()).game()