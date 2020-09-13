import gym
from QLearning import QLearning
from numpy import loadtxt
import numpy as np
from numpy import savetxt
from multiprocessing import Process

#
# This script implements a GridSearch procedure in order to find the best
# hyperparameters for the Frozen Lake problem.
#

def inner_execution(envDesc, a, g, ep, e):
    env = gym.make(envDesc).env
    print("current alpha -> {}, gamma -> {}, epsilon -> {}, episodes -> {}".format(a,g,ep,e))
    qlearn = QLearning(env, alpha = a, gamma = g, epsilon = ep, epsilon_min = 0.001, epsilon_dec = 0.9999, episodes = e)
    q_table = qlearn.train(
        "grid_data/q_table_{}_alpha_{}_gamma_{}_ep{}_e{}.csv".format(envDesc, a, g, ep, e), 
        None
        )

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

    r = np.array([a, g, ep, e, rewards])
    print (r)
    savetxt(
        "grid_results/results_{}_alpha_{}_gamma_{}_ep{}_e{}".format(envDesc, a, g, ep, e),
        r, delimiter = ',', newline="  ", fmt = "%10.5f"
        )

if __name__ == '__main__':

    grid = {
        "alpha": [1, 0.95, 0.9, 0.85, 0.8, 0.7, 0.5, 0.3, 0.2],
        "gamma": [0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.50, 0.3],
        "i_epsilon": [0.9, 0.8, 0.7, 0.5],
        "episodes": [10000, 50000, 100000]
    }

    envDesc = 'FrozenLake-v0'

    for i in grid:
        if len(i) == 0:
            break

    processes = []
    for a in grid["alpha"]:
        for g in grid["gamma"]:
            for ep in grid["i_epsilon"]: 
                for e in grid["episodes"]:
                    p = Process(target=inner_execution, args=(envDesc, a, g, ep, e,))
                    processes.append(p)
                    p.start()

    # Espera pelo término de todos os processos.
    # Não eh necessário esperar visto que não existe mais
    # execução abaixo
    #for proc in processes:
    #    proc.join()
    



                


        
        