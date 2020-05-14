# Reinforcement Learning

Nesta pasta você irá encontrar alguns exemplos de implementações utilizadno Aprendizagem por Reforço (*reinforcement learning*).

Os exemplos utilizam um projeto chamado **OpenAI Gym**. Para executar os exemplos você terá que primeiro instalar o pacote: 

````
pip3 install cmake 'gym[atari]' scipy
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

## Instalação de todos os environments

Para utilizar todos os environments é necessário fazer a instalação completa do pacote Gym:

````
pip3 install 'gym[all]'
````

No comando acima deixa-se claro que a instalação é no pip3, ou seja, no python3. No entanto, na sua máquina talvez seja necessário apenas informar pip. 


## Exemplos não terminados

- LunarLander.py: 
- MsPacman.py: 

## Atividades

Não deixe de ler o arquivo (Atividades.md)[Atividades.md]. Este arquivo tem uma lista com propostas de exercícios para compreender melhor o projeto Gym e os conceitos relacionados com Aprendizagem por Reforço. 

## Referências

- https://gym.openai.com/
- https://github.com/openai/gym/wiki/FrozenLake-v0
- https://github.com/openai/gym/wiki/MountainCar-v0
- https://gym.openai.com/envs/LunarLander-v2/
