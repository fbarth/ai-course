import gym
import numpy as np

env = gym.make("MsPacman-v0")
env.reset()

done = False
while done != True:
    env.render()
    action = np.random.randint(1, env.action_space.n)
    state2, reward, done, _ = env.step(action) 
    print(str(state2)+"  "+str(reward))

#
# Comments from: https://www.oreilly.com/radar/introduction-to-reinforcement-learning-and-openai-gym/
#
# You will notice that env.reset() returns a large array of numbers. 
# To be specific, you can enter state.shape to show that our current
# state is represented by a 210x160x3 Tensor. This represents the height, 
# length, and the three RGB color channels of the Atari game or, simply 
# put, the pixels.
#