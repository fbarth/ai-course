import random
from IPython.display import clear_output
import gym
import numpy as np
from QLearning import QLearning
from numpy import loadtxt

env = gym.make("Taxi-v3").env

# only execute the following lines if you want to create a new q-table
qlearn = QLearning(env, alpha=0.1, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
q_table = qlearn.train('data/q-table-taxi-driver.csv', 'results/actions_taxidriver')
#q_table = loadtxt('data/q-table-taxi-driver.csv', delimiter=',')

state = env.reset()
epochs, penalties, reward = 0, 0, 0
done = False
frames = [] # for animation
    
while not done:
    action = np.argmax(q_table[state])
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1

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
print("Penalties incurred: {}".format(penalties))