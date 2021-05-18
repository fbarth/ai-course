from BarthJV import BarthJV
import numpy as np

def test_barth_player_eval():
    board = [1,1,1,0,2,0,2,2,0]
    ev = BarthJV().eval(2,board)
    assert ev == -10

def test_barth_player_eval2():
    board = [1,1,0,0,2,0,2,2,0]
    ev = BarthJV().eval(2,board)
    assert ev == 0

def test_barth_player_eval3():
    board = [1,2,1,0,2,0,2,2,0]
    ev = BarthJV().eval(2,board)
    assert ev == 10

def test_barth_player_eval4():
    board = [1,2,1,0,1,0,1,2,2]
    ev = BarthJV().eval(1,board)
    assert ev == 10

def test_sucessores():
    board = [1,2,1,0,1,0,1,2,2]
    boards = BarthJV().sucessores(1,board)
    print(boards)
    assert len(boards) == 2
    assert boards == [[3, [1, 2, 1, 1, 1, 0, 1, 2, 2]], [5, [1, 2, 1, 0, 1, 1, 1, 2, 2]]]

def test_sucessores2():
    board = [0,0,0,0,0,0,0,0,0]
    boards = BarthJV().sucessores(1,board)
    print(boards)
    assert len(boards) == 9

def test_sucessores3():
    board = [0,0,0,0,1,0,0,0,0]
    boards = BarthJV().sucessores(2,board)
    print(boards)
    assert len(boards) == 8

def test_sucessores4():
    board = [1,2,1,2,1,2,1,2,1]
    boards = BarthJV().sucessores(1,board)
    print(boards)
    assert len(boards) == 0

def test_move1():
    board = [1,2,1,0,1,0,0,2,2]
    move= BarthJV().move(1,board)
    assert move == 6

def test_move2():
    board = [1,2,1,0,1,0,0,0,2]
    move= BarthJV().move(2,board)
    assert move == 6

def test_move3():
    board = [0,0,0,0,0,0,0,0,0]
    move= BarthJV().move(1,board)
    print(move)

def test_move4():
    board = [0,0,0,0,0,0,0,0,1]
    move= BarthJV().move(2,board)
    print(move)

def test_move5():
    board = [2,1,1,1,1,2,2,0,0]
    move= BarthJV().move(2,board)
    assert move == 7

def test_move6():
    board = [2,0,0,0,1,0,0,0,0]
    move= BarthJV().move(1,board)
    print(move)

def test_move7():
    board = [2,0,0,0,1,0,0,0,1]
    move= BarthJV().move(2,board)
    print(move)

def test_move8():
    board = [2,0,2,0,1,0,0,0,1]
    move= BarthJV().move(1,board)
    assert move == 1

def test_move9():
    board = [2,0,2,0,1,1,0,0,1]
    move= BarthJV().move(2,board)
    assert move == 1

def test_move10():
    board = [2,0,1,0,1,0,0,0,0]
    move= BarthJV().move(2,board)
    assert move == 6