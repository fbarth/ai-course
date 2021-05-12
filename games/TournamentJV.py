from JogoVelha import JogoVelha
from ManualPlayerJV import ManualPlayerJV
from RandomPlayerJV import RandomPlayerJV
from BarthJV import BarthJV
from LucasPlayer import BiggerBrainBot
from ChadPlayer import ChadPlayer
from AstolfoPlayer import AstolfoPlayer
from MariBia import MariBia
from CaioSamuel import CaioSamuel
from TigasTortoJV import TigasTorto

#
# Campeonato de Jogo da Velha, 
# versao 1o semestre de 2021
#
# 8 jogadores, incluindo 1 jogador do professor e 
# 1 jogador aleatorio.
#

players = [
    BarthJV(),
    RandomPlayerJV(),
    BiggerBrainBot(),
    ChadPlayer(),
    AstolfoPlayer(),
    MariBia(),
    CaioSamuel(),
    TigasTorto()]
    
points = {}
for p in players:
    points[p.name()] = 0

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[i].name() + " vs "+players[j].name())
        winner = JogoVelha(players[i], players[j]).game()
        if (winner=='draw'):
            points[players[i].name()] += 0.5
            points[players[j].name()] += 0.5
        else:
            points[winner] += 1 

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[j].name() + " vs "+players[i].name())
        winner = JogoVelha(players[j], players[i]).game()
        if (winner=='draw'):
            points[players[i].name()] += 0.5
            points[players[j].name()] += 0.5
        else:
            points[winner] += 1 

print('Results:')
print('\n')
print(points)
