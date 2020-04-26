#
# Training the agent
#

import random
from IPython.display import clear_output
import gym
import numpy as np

env = gym.make("Taxi-v3").env
env.s = 328
q_table = np.zeros([env.observation_space.n, env.action_space.n])

# Hyperparameters

# (alpha) is the learning rate (0<α≤1) - Just like in supervised learning settings, 
# α is the extent to which our Q-values are being updated in every iteration. 
alpha = 0.1


# (gamma) is the discount factor (0≤γ≤1) - determines how much importance we want 
# to give to future rewards. A high value for the discount factor (close to 1) 
# captures the long-term effective award, whereas, a discount factor of 0 makes 
# our agent consider only immediate reward, hence making it greedy.
gamma = 0.6

# There's a tradeoff between exploration (choosing a random action) and 
# exploitation (choosing actions based on already learned Q-values). 
# We want to prevent the action from always taking the same route, and possibly overfitting, 
# so we'll be introducing another parameter called ϵ "epsilon" to cater to this 
# during training.
epsilon = 0.1


for i in range(1, 100001):
    state = env.reset()

    epochs, penalties, reward, = 0, 0, 0
    done = False
    
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[state]) # Exploit learned values

        # define o proximo estado (next_state) e a 
        # recompensa (reward) por aplicar a action no atual estado
        next_state, reward, done, info = env.step(action) 
        
        # valor atual para o par state,action
        old_value = q_table[state, action]
        # valor da melhor acao a ser executada no novo estado
        next_max = np.max(q_table[next_state])
        
        # atualiza o par state, action levando-se em consideracao a equacao
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1
        
    if i % 100 == 0:
        clear_output(wait=True)
        print(f"Episode: {i}")

print("Training finished.\n")

print(q_table)
print('\n')

#
# Executing agent after Q-learning trainning
#

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





