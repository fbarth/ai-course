import gym
from QLearning_BlackJack import QLearning
from numpy import loadtxt
import numpy as np
from IPython.display import clear_output
from time import sleep
import sys

#
# @author: Cesar + others
# 
# This script implements a GridSearch procedure in order to find the best
# hyperparameters for the Frozen Lake problem.
#

class GridSearchQBlack:
    
    grid = {
        "alpha": [], # Learning rate. The higher it is, more value it will give to new experiences
        "gamma": [], # Determines the importance of future rewards, rather than the current one
    }
    results = []

    def __init__(self, envDesc, grid):
        self.envDesc = envDesc
        self.grid = grid
    
    def stateNumber(self, state):
        (x,y,z) = state
        y = y * 32
        z = z * 352
        return x+y+z

    def inner_execution(self, env, a, g, ep, e):
        print("current alpha -> {}, gamma -> {}, epsilon -> {}, episodes -> {}".format(a,g,ep,e))
        qlearn = QLearning(env, alpha = a, gamma = g, epsilon = ep, epsilon_min = 0.001, epsilon_dec = 0.9999, episodes = e)
        q_table = qlearn.train(
            "grid_data/q_table_{}_alpha_{}_gamma_{}_ep{}_e{}.csv".format(self.envDesc, a, g, ep, e), 
            "grid_results/actions_{}_alpha_{}_gamma_{}_ep{}_e{}".format(self.envDesc, a, g, ep, e)
            )
        
        rewards = 0
        state= env.reset()
        done = False
        state = self.stateNumber(state)

        for i in range(101):
            while not done:
                action = np.argmax(q_table[state])
                state, reward, done, info = env.step(action)
                if reward == 1:
                    rewards += 1
                state = self.stateNumber(state)

        self.results.append([a, g, ep, e, rewards])
    
    def execute(self):
        for i in self.grid:
            if len(i) == 0:
                return

        env = gym.make(self.envDesc)
        for a in self.grid["alpha"]:
            for g in self.grid["gamma"]:
                for ep in self.grid["i_epsilon"]: 
                    for e in self.grid["episodes"]:
                        #
                        # TODO: we must turn this execution into concurrent 
                        #
                        self.inner_execution(env, a, g, ep, e) 


    def printResults(self):
        print('\n\n\n\n\n')
        for r in self.results: 
            print(r)
                

#
# This implementation is taking too much time to execute with
# parameters bellow because the implementation is sequencial. 
#
parameters = {
    "alpha": [1, 0.95, 0.9, 0.85, 0.8, 0.7, 0.5, 0.3, 0.2],
    "gamma": [0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.50, 0.3],
    "i_epsilon": [0.9, 0.8, 0.7, 0.5],
    "episodes": [10000, 50000, 100000]
}

#
# Execute grid search for Blackjack environment
#
grid = GridSearchQBlack('Blackjack-v0', parameters)
grid.execute()
grid.printResults()


                


        
        