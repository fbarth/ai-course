from JogoVelha import JogoVelha
from ManualPlayerJV import ManualPlayerJV
from RandomPlayerJV import RandomPlayerJV

players = [
    ManualPlayerJV(),
    RandomPlayerJV()]
    
points = {}
for p in players:
    points[p.name()] = 0

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[i].name() + " vs "+players[j].name())
        winner = JogoVelha(players[i], players[j]).game()
        if (winner=='draw'):
            points[players[0].name()] += 0.5
            points[players[1].name()] += 0.5
        else:
            points[winner] += 1 

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[j].name() + " vs "+players[i].name())
        winner = JogoVelha(players[j], players[i]).game()
        if (winner=='draw'):
            points[players[0].name()] += 0.5
            points[players[1].name()] += 0.5
        else:
            points[winner] += 1 

print('Results:')
print('\n')
print(points)
