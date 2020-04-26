# Reinforcement Learning

Nesta pasta você irá encontrar alguns exemplos de implementações utilizadno Aprendizagem por Reforço (*reinforcement learning*).

Os exemplos utilizam um projeto chamado **OpenAI Gym**. 

````
pip install cmake 'gym[atari]' scipy
````

O primeiro grupo de exemplos está relacionado com o ambiente *Taxi-v3*:

- TaxiDriverGym_1.py: Exemplo simples para entender os conceitos de environment, space e action no ambiente Gym.
- TaxiDriverGym_2.py: Outro exemplo bem simples só para entender como configurar um state no environment *Taxi-v3*.
- TaxiDriverGym_3.py: Mostra uma implementação aleatória procurando pela solução no *Taxi-v3* (ideia: poderíamos conectar a nossa implementação usando A* com este framework). 
- TaxiDriverGym_4.py: Implmentação mais complexa que mostra o treinamento de um agente usando o algoritmo *Q-Learning*. 

O segundo grupo de implmentações componentiza o algoritmo Q-Learning para reutilizar este algoritmo em diversos environments:

- QLearning.py: Implementação do algoritmo QLearning. Esta classe gera uma q-table para cada environment e grava em arquivo.
- TaxiDriverGym_5.py: faz uso do QLearning.py para gerar uma única vez a q-table e executar diversas vezes o problema do taxi driver.

