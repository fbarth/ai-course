import gym
import numpy as np
import matplotlib.pyplot as plt

#
# This code was adapted from 
# https://towardsdatascience.com/getting-started-with-reinforcement-learning-and-open-ai-gym-c289aca874f
# 
# I changed:
#  * the initialize of Q table
#  * the way that the solution decay epsilon
#

env = gym.make('MountainCar-v0')
env.reset()

print('State space: ', env.observation_space)
print('Action space: ', env.action_space)

print(env.observation_space.low)
print(env.observation_space.high)

# Define Q-learning function
def QLearning(env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):
    # Determine size of discretized state space
    num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])
    num_states = np.round(num_states, 0).astype(int) + 1
    
    # Initialize Q table
    #Q = np.random.uniform(low = -1, high = 1, 
    #                      size = (num_states[0], num_states[1], 
    #                              env.action_space.n))

    Q = np.zeros([num_states[0], num_states[1], env.action_space.n])
    
    # Initialize variables to track rewards
    reward_list = []
    ave_reward_list = []
    actions_per_episode = []
    
    # Run Q learning algorithm
    for i in range(episodes):
        # Initialize parameters
        done = False
        tot_reward, reward = 0,0
        state = env.reset()
        
        # Discretize state
        state_adj = (state - env.observation_space.low)*np.array([10, 100])
        state_adj = np.round(state_adj, 0).astype(int)
    
        qtd_actions = 0
        while done != True:   
            # Render environment for last five episodes
            if i >= (episodes - 6):
                env.render()
                
            # Determine next action - epsilon greedy strategy
            if np.random.random() < 1 - epsilon:
                action = np.argmax(Q[state_adj[0], state_adj[1]]) 
            else:
                action = np.random.randint(0, env.action_space.n)
                
            # Get next state and reward
            state2, reward, done, _ = env.step(action) 
            #print(reward)
            
            # Discretize state2
            state2_adj = (state2 - env.observation_space.low)*np.array([10, 100])
            state2_adj = np.round(state2_adj, 0).astype(int)
            
            #Allow for terminal states
            if done and state2[0] >= 0.5:
                Q[state_adj[0], state_adj[1], action] = reward
                
            # Adjust Q value for current state
            else:
                delta = alpha*(reward + gamma * np.max(Q[state2_adj[0], state2_adj[1]]) - Q[state_adj[0], state_adj[1],action])
                Q[state_adj[0], state_adj[1],action] += delta
                                     
            # Update variables
            tot_reward += reward
            state_adj = state2_adj
            qtd_actions = qtd_actions + 1
        
        # Decay epsilon
        if epsilon > epsilon_min:
            epsilon = epsilon * epsilon_dec
        
        # Track rewards
        reward_list.append(tot_reward)
        
        if (i+1) % 100 == 0:
            ave_reward = np.mean(reward_list)
            ave_reward_list.append(ave_reward)
            actions_per_episode.append(qtd_actions)
            reward_list = []
            
        if (i+1) % 100 == 0:    
            print('Episode {} Average Reward: {}  Actions in this episode {} '.format(i+1, ave_reward, actions_per_episode[len(actions_per_episode)-1]))

    input("Enter a key...")
    env.close()
    
    return ave_reward_list, actions_per_episode

# Run Q-learning algorithm
rewards, qtd_actions = QLearning(env, 0.1, 0.9, 0.8, 0, 0.999, 5000)

# Plot Rewards
plt.plot(100*(np.arange(len(rewards)) + 1), rewards)
plt.xlabel('Episodes')
plt.ylabel('Average Reward')
plt.title('Average Reward vs Episodes')
plt.savefig('results/rewards_MountainCar-v0.jpg')     
plt.close()  

plt.plot(100*(np.arange(len(qtd_actions)) + 1), qtd_actions)
plt.xlabel('Episodes')
plt.ylabel('# Actions')
plt.title('# Actions vs Episodes')
plt.savefig('results/actions_MountainCar-v0.jpg')     
plt.close()  