from FourInRow import FourInRow
from ManualPlayer import ManualPlayer
from RandomPlayer import RandomPlayer
from LucasDaniel import LucasDaniel
import time
import numpy as np

def test_game():
    f = FourInRow(LucasDaniel(), LucasDaniel()).game()