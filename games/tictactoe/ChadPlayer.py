from Player import Player
import copy

#
# Authors: Lucas Rodrigues & Lucas Facci
#

class ChadPlayer(Player):

    def name(self):
        return "Chad, from based department"

    def move(self, player_code, board, finalAction = None):
        if player_code not in board: 
            if opponent(player_code) not in board or board[4] == opponent(player_code):
                return 0
            else:
                return 4

        winningMove = self.doWinningMovesExists(player_code, board)
        if winningMove != None:
            return winningMove

        losingMove = self.doWinningMovesExists(opponent(player_code), board)
        if losingMove != None:
            return losingMove

        if not self.haveIStarted(player_code, board):
            if board[4] == player_code and len(find(opponent(player_code), board, 1)) == 1 and len(find(opponent(player_code), board, 0)) == 1:
                if find(opponent(player_code), board, 1)[0] == 2 or find(opponent(player_code), board, 1)[0] == 6:
                    if find(opponent(player_code), board, 0)[0] == 3 or find(opponent(player_code), board, 0)[0] == 1:
                        return 0
                    else:
                        return 8
                if find(opponent(player_code), board, 1)[0] == 0 or find(opponent(player_code), board, 1)[0] == 8:
                    if find(opponent(player_code), board, 0)[0] == 7 or find(opponent(player_code), board, 0)[0] == 3:
                        return 6
                    else:
                        return 2
            elif board[4] == player_code and len(find(opponent(player_code), board, 0)) == 2 and find(opponent(player_code), board, 1) == []:
                if 1 in find(opponent(player_code), board, 0):
                    if 3 in find(opponent(player_code), board, 0):
                        return 0
                    else:
                        return 2
                if 7 in find(opponent(player_code), board, 0):
                    if 3 in find(opponent(player_code), board, 0):
                        return 6
                    else:
                        return 8
            elif board[4] == player_code and find(opponent(player_code), board, 1) != []:
                return find(0, board, 0)[0]
            elif find(0, board, 1) != []:
                return find(0, board, 1)[0]

        primesucessors = self.sucessores(player_code, board)
        bestTime = 10
        for ps in primesucessors:
            if self.closestVictory(player_code, ps['board'], ps['action']) != None:
                time, action = self.closestVictory(player_code, ps['board'], ps['action'])
                if time < bestTime:
                    bestTime = time
                    finalAction = action
                elif time == bestTime and (action == 0 or action == 2 or action == 6 or action == 8):
                    bestTime = time
                    finalAction = action

        if finalAction != None:
            return finalAction
        else:
            return self.fuckIt(board)

    def haveIStarted(self, player_code, board):
        me = 0
        op= 0
        for slot in board:
            if slot == player_code:
                me += 1
            elif slot == opponent(player_code):
                op += 1
        if op > me:
            return False
        else:
            return True

    def sucessores(self, player_code, board):
        suc = []
        for i in range(0,9):
            if board[i] == 0:
                possibleBoard = copy.deepcopy(board)
                possibleBoard[i] = player_code
                suc.append({'board':possibleBoard, 'action':i})
        return suc

    def doWinningMovesExists(self, player, board):
        sucessors = self.sucessores(player, board)
        for s in sucessors:
            if hasWinner(s['board'], player):
                return s['action']
        return None

    def closestVictory(self, player, board, action, p = 1):
        sucessors = self.sucessores(opponent(player), board)
        for s in sucessors:
            supercessors = self.sucessores(player, s['board'])
            for sc in supercessors:
                if hasWinner(sc['board'], player):
                    return p + 1, action
            for sc in supercessors:
                if self.closestVictory(player, sc['board'], action, p + 1) != None:
                    return self.closestVictory(player, sc['board'], action, p + 1)

    def fuckIt(self, board):
        for x in range(0,9):
            if board[x] == 0:
                return x

def opponent(player):
    if player==1:
        return 2
    return 1

def find(id, board, mod):
    found = []
    if mod == 1: 
        search = [0, 2, 6, 8]
    else:
        search = [1, 3, 5, 7]
    for slot in search:
        if board[slot] == id:
            found.append(slot)
    return found

def hasWinner(board, player_code):
    if((board[0] == board[1] == board[2]) & (board[0] == player_code)):
        return True
    elif((board[3] == board[4] == board[5]) & (board[3] == player_code)):
        return True
    elif((board[6] == board[7] == board[8]) & (board[6] == player_code)):
        return True
    elif((board[0] == board[3] == board[6]) & (board[0] == player_code)):
        return True
    elif((board[1] == board[4] == board[7]) & (board[1] == player_code)):
        return True
    elif((board[2] == board[5] == board[8]) & (board[2] == player_code)):
        return True
    elif((board[0] == board[4] == board[8]) & (board[0] == player_code)):
        return True
    elif((board[2] == board[4] == board[6]) & (board[2] == player_code)):
        return True
    else:
        return False