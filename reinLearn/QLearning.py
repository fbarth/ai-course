import numpy as np
import gym
import random
from numpy import savetxt
import sys
import matplotlib.pyplot as plt

#
# This class implements the Q Learning algorithm.
# We can use this implementation to solve Toy text environments from Gym project. 
#

class QLearning:

    def __init__(self, env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):
        self.env = env
        self.q_table = np.zeros([env.observation_space.n, env.action_space.n])
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.episodes = episodes

    def select_action(self, state):
        rv = random.uniform(0, 1)
        if rv < self.epsilon:
            return self.env.action_space.sample() # Explore action space
        return np.argmax(self.q_table[state]) # Exploit learned values

    def train(self, filename, plotFile):
        actions_per_episode = []
        for i in range(1, self.episodes+1):
            state = self.env.reset()
            reward = 0
            done = False
            actions = 0

            while not done:
                action = self.select_action(state)
                next_state, reward, done, _ = self.env.step(action) 
        
                # Adjust Q value for current state
                old_value = self.q_table[state, action]
                next_max = np.max(self.q_table[next_state])
                new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
                self.q_table[state, action] = new_value
                
                state = next_state
                actions += 1

            if i % 100 == 0:
                actions_per_episode.append(actions)
                sys.stdout.write("Episodes: " + str(i) +'\r')
                sys.stdout.flush()
            
            if self.epsilon > self.epsilon_min:
                self.epsilon = self.epsilon * self.epsilon_dec

        savetxt(filename, self.q_table, delimiter=',')
        if (plotFile is not None): self.plotactions(plotFile, actions_per_episode)
        return self.q_table

    def plotactions(self, plotFile, actions_per_episode):
        plt.plot(actions_per_episode)
        plt.xlabel('Episodes')
        plt.ylabel('# Actions')
        plt.title('# Actions vs Episodes')
        plt.savefig(plotFile+".jpg")     
        plt.close()

        size = len(actions_per_episode)
        start = (int)(size - (size * 0.1))
        plt.plot(actions_per_episode[start:])
        plt.xlabel('Episodes')
        plt.ylabel('# Actions')
        plt.title('# Actions vs Episodes (Last episodes)')
        plt.savefig(plotFile+"_last.jpg")     
        plt.close()
