from BarthPlayer import BarthPlayer
import warnings
import numpy as np

def test_barth_player_eval():
    warnings.filterwarnings('ignore', category=PendingDeprecationWarning)

    board = np.matrix([[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [2, 1, 1, 1, 0, 0, 0]])

    ev = BarthPlayer().eval(2,board)
    assert ev == -10000

def test_barth_player_move():
    warnings.filterwarnings('ignore', category=PendingDeprecationWarning)

    board = np.matrix([[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [2, 1, 1, 1, 0, 0, 0]])

    action = BarthPlayer().move(2, board)
    assert action == 4