#
# O objetivo deste arquivo eh mostrar como funciona o
# environment do black jack.
#
# Neste ambiente o jogador joga contra o dealer e soh
# pode realizar duas acoes:
# - pedir por mais cartas (1)
# - parar (0)
#
# O ambiente eh representado por uma 3-tuple:
# (
#   soma das cartas do jogador, 
#   qual a carta o dealer estah mostrando, 
#   se o jogador estah segurando um Ás ou nao)
#

import gym
env = gym.make("Blackjack-v0")
print('Actions: '+ str(env.action_space))
print('Spaces: '+ str(env.observation_space))

print('Inicializando o jogo...')
state = env.reset()
print(state)
done = False

while not done:
    action = env.action_space.sample()
    print('Action = '+ str(action))
    state, reward, done, info = env.step(action)
    print(state)

print('resultado =  ' + str(reward))

print('Mão do dealer' + str(env.dealer))
