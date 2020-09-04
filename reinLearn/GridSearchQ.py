import gym
from QLearning import QLearning
from numpy import loadtxt
import numpy as np
from IPython.display import clear_output
from time import sleep

#
# @author: Cesar + others
# 
# This script implements a GridSearch procedure in order to find the best
# hyperparameters for the Frozen Lake problem.
#

class GridSearchQ:
    
    grid = {
        "alpha": [], # Learning rate. The higher it is, more value it will give to new experiences
        "gamma": [], # Determines the importance of future rewards, rather than the current one
    }
    results = []

    def __init__(self, envDesc, grid):
        self.envDesc = envDesc
        self.grid = grid

    def inner_execution(self, env, a, g, ep, e):
        print("current alpha -> {}, gamma -> {}, epsilon -> {}, episodes -> {}".format(a,g,ep,e))
        qlearn = QLearning(env, alpha = a, gamma = g, epsilon = ep, epsilon_min = 0.001, epsilon_dec = 0.9999, episodes = e)
        q_table = qlearn.train(
            "grid_data/q_table_{}_alpha_{}_gamma_{}_ep{}_e{}.csv".format(self.envDesc, a, g, ep, e), 
            "grid_results/actions_{}_alpha_{}_gamma_{}_ep{}_e{}".format(self.envDesc, a, g, ep, e)
            )
                
        rewards = 0
        for i in range(101):
            state = env.reset()
            train_done = False
            count = 0
            while (not train_done) and (count < 200):
                action = np.argmax(q_table[state])
                tate, reward, train_done, _ = env.step(action)
                count += 1
                if reward == 1:
                    rewards += 1

        self.results.append([a, g, ep, e, rewards])
    
    def execute(self):
        for i in self.grid:
            if len(i) == 0:
                return
        
        env = gym.make(self.envDesc).env
        for a in self.grid["alpha"]:
            for g in self.grid["gamma"]:
                for ep in self.grid["i_epsilon"]: 
                    for e in self.grid["episodes"]:
                        self.inner_execution(env, a, g, ep, e) 

    def printResults(self):
        print('\n\n\n\n\n')
        for r in self.results: 
            print(r)
                

parameters = {
    "alpha": [1, 0.95, 0.9, 0.85, 0.8, 0.7, 0.5, 0.3, 0.2],
    "gamma": [0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.50, 0.3],
    "i_epsilon": [0.9, 0.8, 0.7, 0.5],
    "episodes": [10000, 50000, 100000]
}

#
# Execute grid search for FrozenLake environment
#
grid = GridSearchQ("FrozenLake-v0", parameters)
grid.execute()
grid.printResults()


                


        
        