# Reinforcement Learning

Nesta pasta você irá encontrar alguns exemplos de implementações utilizadno Aprendizagem por Reforço (*reinforcement learning*).

Os exemplos utilizam um projeto chamado **OpenAI Gym**. Para executar os exemplos você terá que primeiro instalar o pacote: 

````
pip install cmake 'gym[atari]' scipy
````

## Exemplos

O primeiro grupo de exemplos está relacionado com os ambientes *Taxi-v3* e *FrozenLake*:

- TaxiDriverGym_introduction.py: Exemplo simples para entender os conceitos de environment *Taxi-v3*, space e action no ambiente Gym (ideia: poderíamos conectar a nossa implementação usando A* com este framework). 
- TaxiDriverGym.py: Implementação que mostra o treinamento de um agente usando o algoritmo *Q-Learning*. 
- QLearning.py: Implementação do algoritmo QLearning que pode ser utilizado por environments modo texto do projeto **Gym**.  
- FrozenLake_introduction.py: Exemplo simples para entender os conceitos do environment *FrozenLake-v0*. 
- FrozenLake.py: Implementação que mostra o treinamento de um agente usando o algoritmo *Q-Learning*.

O segundo grupo de exemplos está relacionado com ambientes que o espaço não é texto, mas são espaços gráficos 2D: 

- MountainCar.py: Exemplo de um carro que precisa aprender como subir uma montanha. 

## Referências

- https://gym.openai.com/
- https://github.com/openai/gym/wiki/FrozenLake-v0
- https://github.com/openai/gym/wiki/MountainCar-v0