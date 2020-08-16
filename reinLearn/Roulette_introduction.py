import gym
import sys

env = gym.make('Roulette-v0').env
action = int(sys.argv[1])
print(action)
state, reward, done, info = env.step(action)
print(state)
print(reward)
print(done)
print(info)