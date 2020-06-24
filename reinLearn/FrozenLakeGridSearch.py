import gym
from QLearning import QLearning
from numpy import loadtxt
import numpy as np
from IPython.display import clear_output
from time import sleep

#
# @author: Cesar 
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

    def __init__(self, grid):
        self.grid = grid
    
    def execute(self):
        for i in self.grid:
            if len(i) == 0:
                return
        
        env = gym.make("FrozenLake-v0").env
        for a in self.grid["alpha"]:
            print("current alpha -> {}".format(a))

            for g in self.grid["gamma"]:
                print("current gamma -> {}".format(g))

                for ep in self.grid["i_epsilon"]: 
                    print("current epsilon -> {}".format(ep))

                    for e in self.grid["episodes"]:
                        print("current episodes -> {}".format(e))

                        qlearn = QLearning(env, alpha = a, gamma = g, epsilon = ep, epsilon_min = 0.001, epsilon_dec = 0.9999, episodes = e)
                        q_table = qlearn.train("grid_data/q_table_alpha_{}_gamma_{}.csv".format(a, g), "grid_results/actions_frozen_lake_alpha_{}_gamma_{}".format(a, g))
                
                        rewards = 0
                        for i in range(101):
                            state = env.reset()
                            train_done = False
                            count = 0
                            while (not train_done) and (count < 200):
                                action = np.argmax(q_table[state])
                                state, reward, train_done, _ = env.step(action)
                                count += 1
                            if reward == 1:
                                rewards += 1

                        self.results.append([a, g, ep, e, rewards]) 

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

grid = GridSearchQ(parameters)
grid.execute()
grid.printResults()


                


        
        