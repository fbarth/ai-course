import random
from IPython.display import clear_output
import gym
import numpy as np
import sys
from QLearning import QLearning
from numpy import loadtxt

from IPython.display import clear_output
from time import sleep

# def print_frames(frames):
#     for i, frame in enumerate(frames):
#         clear_output(wait=True)
#         #print(frame['frame'])
#         #print(frame['frame'].getvalue())
#         print(f"Timestep: {i + 1}")
#         print(f"State: {frame['state']}")
#         print(f"Action: {frame['action']}")
#         print(f"Reward: {frame['reward']}")
#         sleep(.1)

env = gym.make('Roulette-v0').env
#q_table = loadtxt('data/q-table-roulette.csv', delimiter=',')

#2600loss - stable
qlearn = QLearning(env, alpha=0.001, gamma=0.001, epsilon=0.9, epsilon_min=0.001, epsilon_dec=0.9999, episodes=1000000)

# 500-1000loss - real player like
#qlearn = QLearning(env, alpha=0.001, gamma=0.001, epsilon=0.9, epsilon_min=0.1, epsilon_dec=0.7, episodes=1000000)
q_table = qlearn.train('data/q-table-roulette.csv', None)

#q_table = loadtxt('data/q-table-roulette.csv', delimiter=',')

state = env.reset()
done = False
rewards = 0
actions = 0

while not done:
    action = np.argmax(q_table)
    state, reward, done, info = env.step(action)
    actions += 1   

    rewards += reward

    print("\n")    
    print("Action: ", action)
    print("Reward: ", reward)
    print("Done? ", done)

clear_output(wait=True)
print("\n")
print("Finished!")
print("Total Rewards: ", rewards)