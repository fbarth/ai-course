import gym
import numpy as np

env = gym.make("LunarLander-v2")
env.reset()

#0- Do nothing
#1- Fire left engine
#2- Fire down engine
#3- Fire right engine

done = False
while done != True:
    env.render()
    action = np.random.randint(1, env.action_space.n)
    state2, reward, done, _ = env.step(action) 
    print(str(state2)+"  "+str(reward))
