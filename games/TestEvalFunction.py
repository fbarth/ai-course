from BarthPlayer import BarthPlayer
import numpy as np

board = np.matrix([[0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0.],
 [0., 2., 0., 0., 0., 0., 0.],
 [0., 2., 0., 0., 0., 0., 0.],
 [2., 2., 1., 1., 1., 0., 0.]])

print(board)
#action = BarthPlayer().max_value(board, None, 2, 2)
#x = BarthPlayer().eval(2,board)
#print(x)

action = BarthPlayer().move(2, board)
print(action)

