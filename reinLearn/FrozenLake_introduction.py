import gym
env = gym.make("FrozenLake-v0").env
print(env.observation_space.n)
print(env.action_space.n)
print(env.render(mode='ansi'))

#indo para baixo
state, reward, done, _ = env.step(1)
print(env.render(mode='ansi'))
print(reward)

#indo para baixo
state, reward, done, _ = env.step(2)
print(env.render(mode='ansi'))
print(reward)

#objetivo
env.s = 15
print(env.render(mode='ansi'))