from BarthPlayer import BarthPlayer
from SushiPlayer import SushiPlayer
import numpy as np

board = np.matrix([[0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 2., 0., 0., 0.],
 [0., 0., 1., 1., 0., 0., 0.]])

print(board)
action = SushiPlayer().max_value(board, None, -999999, 999999, 2, 3)
print(action)
#print(SushiPlayer().eval(2,board))
#action = BarthPlayer().move(2, board)
#print(action)

