import numpy as np
import gym
import random
from numpy import savetxt
from IPython.display import clear_output

class QLearning:

    def __init__(self, env, alpha = 0.1, gamma = 0.6, epsilon = 0.1):
        self.env = env
        self.q_table = np.zeros([env.observation_space.n, env.action_space.n])
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def train(self, filename, episodes = 100000):
        for i in range(1, episodes+1):
            state = self.env.reset()
            reward = 0
            done = False
    
            while not done:
                if random.uniform(0, 1) < self.epsilon:
                    action = self.env.action_space.sample() # Explore action space
                else:
                    action = np.argmax(self.q_table[state]) # Exploit learned values

                next_state, reward, done, _ = self.env.step(action) 
        
                old_value = self.q_table[state, action]
                next_max = np.max(self.q_table[next_state])
        
                new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
                self.q_table[state, action] = new_value
                state = next_state

            if i % 100 == 0:
                clear_output(wait=True)
                print(f"Episode: {i}")

        savetxt(filename, self.q_table, delimiter=',')
