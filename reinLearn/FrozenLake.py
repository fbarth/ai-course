import random
from IPython.display import clear_output
import gym
import numpy as np
from QLearning import QLearning
from numpy import loadtxt

# exemplo de ambiente nao determinístico
env = gym.make('FrozenLake-v0').env

# only execute the following lines if you want to create a new q-table
# qlearn = QLearning(env, alpha=0.9, gamma=0.95, epsilon=0.9, epsilon_min=0.001, epsilon_dec=0.9999, episodes=500000)
# q_table = qlearn.train('data/q-table-frozen-lake.csv','results/actions_frozen_lake')
q_table = loadtxt('data/q-table-frozen-lake.csv', delimiter=',')

state = env.reset()
epochs = 0
done = False
frames = [] # for animation
    
while not done:
    action = np.argmax(q_table[state])
    state, reward, done, info = env.step(action)

    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
        }
    )
    epochs += 1

from IPython.display import clear_output
from time import sleep

clear_output(wait=True)

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        #print(frame['frame'].getvalue())
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)
        
print_frames(frames)

print("\n")
print("Timesteps taken: {}".format(epochs))