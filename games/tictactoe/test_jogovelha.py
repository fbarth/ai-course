from JogoVelha import JogoVelha
import pytest

def test_run_game():
    f = JogoVelha(1,2)
    f.printBoard()

def test_final():
    f = JogoVelha(1,2)
    assert f.hasWinner() == False

def test_final2():
    f = JogoVelha(1,2)
    f.board = [2,2,2,0,1,0,1,1,0]
    assert f.hasWinner() == True

def test_final3():
    f = JogoVelha(1,2)
    f.board = [2,2,1,0,1,0,1,0,0]
    assert f.hasWinner() == True

def test_final4():
    f = JogoVelha(1,2)
    f.board = [1,2,2,1,2,0,1,1,0]
    assert f.hasWinner() == True

def test_empate():
    f = JogoVelha(1,2)
    f.board = [2,2,1,1,1,2,2,1,2]
    assert f.hasWinner() == False

def test_movement():
    f = JogoVelha(1,2)
    f.board = [0,0,0,0,0,0,0,0,0]
    f.movement(1,4)
    assert f.board == [0,0,0,0,1,0,0,0,0]
    f.movement(2,0)
    assert f.board == [2,0,0,0,1,0,0,0,0]
    f.printBoard()

def test_movimento_invalido():
    with pytest.raises(Exception):
        f = JogoVelha(1,2)
        f.board = [0,0,0,0,1,0,0,0,0]
        f.movement(1,4)

def test_movimento_invalido2():
    with pytest.raises(Exception):
        f = JogoVelha(1,2)
        f.board = [0,0,0,0,1,0,0,0,0]
        f.movement(1,10)

def test_jogador_invalido():
    with pytest.raises(Exception):
        f = JogoVelha(1,2)
        f.board = [0,0,0,0,1,0,0,0,0]
        f.movement(3,0)

def test_print():
    print(JogoVelha.printSymbol(1))
    print(JogoVelha.printSymbol(2))

def test_empate():
    f = JogoVelha(1,2)
    f.board = [0,0,0,0,1,0,0,0,0]
    assert f.isDraw() == False
    f.board = [2,2,1,1,1,2,2,1,2]
    assert f.isDraw() == True
    f.board = [1,2,1,2,2,1,2,1,1]
    assert f.isDraw() == False
    assert f.hasWinner() == True