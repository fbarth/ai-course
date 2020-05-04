import gym

env = gym.make("Taxi-v3").env

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))
print('\n\n')

env.render()
# escolhe uma acao aleatoria
action = env.action_space.sample()
# executa a acao
state, reward, done, info = env.step(action)
env.render()
# executa a acao ir para north
state, reward, done, info = env.step(1)
env.render()


# The filled square represents the taxi, which is yellow without a passenger and green with a passenger.
# The pipe ("|") represents a wall which the taxi cannot cross.
# R, G, Y, B are the possible pickup and destination locations. The blue letter represents the current 
# passenger pick-up location, and the purple letter is the current destination.

# actions:
# 0 = south
# 1 = north
# 2 = east
# 3 = west
# 4 = pickup
# 5 = dropoff

import gym

env = gym.make("Taxi-v3").env

state = env.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()