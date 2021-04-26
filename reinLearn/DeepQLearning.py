import gym
import numpy as np
import random
from keras import Sequential
from keras.layers import Dense
from keras.activations import relu, linear
from keras.optimizers import adam

#
# This class implements the Deep Q-Learning algorithm.
# We can use this implementation to solve LunarLandar-v2 environment from Gym project.
#


class DeepQLearning:
    def __init__(self, env, gamma, epsilon, epsilon_min, epsilon_dec, episodes, batch_size, memory, model):
        self.env = env
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.episodes = episodes
        self.batch_size = batch_size
        self.memory = memory
        self.model = model

    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return random.randrange(self.env.action_space.n)
        action = self.model.predict(state)
        return np.argmax(action[0])

    def experience(self, state, action, reward, next_state, terminal):
        self.memory.append((state, action, reward, next_state, terminal))

    def experience_replay(self):
        if len(self.memory) > self.batch_size:
            batch = random.sample(self.memory, self.batch_size)
            states = np.array([i[0] for i in batch])
            actions = np.array([i[1] for i in batch])
            rewards = np.array([i[2] for i in batch])
            next_states = np.array([i[3] for i in batch])
            terminals = np.array([i[4] for i in batch])

            # np.squeeze(): Remove single-dimensional entries from the shape of an array.
            # Para se adequar ao input
            states = np.squeeze(states)
            next_states = np.squeeze(next_states)

            # \ indica que as operações continuam na próxima linha, adicionado pelo pylint seguindo pep-8
            targets = rewards + self.gamma * \
                (np.amax(self.model.predict_on_batch(
                    next_states), axis=1)) * (1 - terminals)
            targets_full = self.model.predict_on_batch(states)

            indexes = np.array([i for i in range(self.batch_size)])
            targets_full[[indexes], [actions]] = targets

            self.model.fit(states, targets_full, epochs=1, verbose=0)
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_dec

        return

    def train(self):
        loss = []
        for i in range(self.episodes+1):
            state = self.env.reset()
            state = np.reshape(state, (1, 8))
            score = 0
            max_steps = 3000
            for _ in range(max_steps):
                action = self.select_action(state)
                self.env.render()
                next_state, reward, terminal, _ = self.env.step(action)
                score += reward
                next_state = np.reshape(next_state, (1, 8))
                self.experience(state, action, reward, next_state, terminal)
                state = next_state
                self.experience_replay()
                if terminal:
                    print(f'Episódio: {i+1}/{self.episodes}. Score: {score}')
                    break
            loss.append(score)

            # encerrar se a média dos últimos 50 episódios for maior que 200 (solved) para não ficar rodando muito tempo
            # percebi que, normalmente, após resolver 10 a 20 seguidos, ele costuma acertar todos
            # coloquei 50 para ter certeza, talvez realizar mais testes
            mean_50 = np.mean(loss[-50:])
            print(f'Média dos últimos 50 episódios: {mean_50}')
            if mean_50 > 200:
                print('Aprendeu!')
                break

        return loss
