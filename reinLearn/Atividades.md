# Proposta de atividades

## Faça a instalação do pacote Gym na sua máquina

Eventualmente, a instalação via arquivo `requirements.txt` pode não ter funcionado na sua máquina. Se foi este o caso então execute os comandos abaixo: 

Para Mac ou Linux:
````bash
pip3 install cmake 'gym[atari]' scipy
````

Para Windows:
````bash
py.exe -m pip install cmake 'gym[atari]' scipy
````

Caso contrário, pode ignorar os comandos acima.


## Trabalhe com o arquivo [TaxiDriverGym_introduction.py](TaxiDriverGym_introduction.py)

* Leia a descrição do ambiente em [https://gym.openai.com/envs/Taxi-v3/](https://gym.openai.com/envs/Taxi-v3/).

* Execute cada um dos comandos que estão no arquivo [TaxiDriverGym_introduction.py](TaxiDriverGym_introduction.py) em um interpretador python para entender o que o que é environment, reward e action. Além de entender detalhes do ambiente. 

* Quantos espaços possíveis o ambiente Taxi-v3 possui? 

* Quantas ações o agente que atua no ambiente Taxi-v3 possui? 

* O que a variável reward retornada por env.step(<number>) significa? 

## Trabalhe com o arquivo [TaxiDriverGym.py](TaxiDriverGym.py)

* Abra em um editor de texto e descomente as linhas 11 e 12 e comente a linha 13. O código deve ficar como abaixo:
````python
# only execute the following lines if you want to create a new q-table
qlearn = QLearning(env, alpha=0.1, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
q_table = qlearn.train('data/q-table-taxi-driver.csv', 'results/actions_taxidriver')
#q_table = loadtxt('data/q-table-taxi-driver.csv', delimiter=',')
````

* Execute o arquivo [TaxiDriverGym.py](TaxiDriverGym.py) com o comando:

````bash
python TaxiDriverGym.py
````

Lembre-se que nesta execução o programa irá criar toda a Q-table e armazenar no arquivo data/q-table-taxi-driver.csv. Depois de calcular os valores para a Q-table o programa irá resolver um dos possíveis cenários considerando um estado inicial qualquer. Além disso, o programa irá gerar dois plots 
no diretório results que descrevem a quantidade de ações executadas em cada época. 

* Agora faça o algoritmo [TaxiDriverGym.py](TaxiDriverGym.py) ler a Q-table a partir do arquivo gerado anteriormente e veja qual é o comportamento. Execute diversas vezes.

* Qual é o comportamento do agente? Ele sempre consegue encontrar uma solução? As soluções parecem ser ótimas? 

* Descomente novamente as linhas 11 e 12, comente a linha 13 e faça alpha receber 0 como apresentado na linha abaixo:

````
qlearn = QLearning(env, alpha=0, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
````

* Execute novamente o código [TaxiDriverGym.py](TaxiDriverGym.py). O que aconteceu? Qual é a explicação para este comportamento? 

## Trabalhe com o arquivo [FrozenLake_introduction.py](FrozenLake_introduction.py)

* Leia a descrição do ambiente em [https://github.com/openai/gym/wiki/FrozenLake-v0](https://github.com/openai/gym/wiki/FrozenLake-v0).

* Veja o que está codificado no arquivo e execute o mesmo.

* Quantos estados e quantas ações o ambiente FrozenLake-v0 tem?

* O que aconteceu com a execução das ações? O resultado foi o esperado? Descreve o que aconteceu.

## Trabalhe com o arquivo [FrozenLake.py](FrozenLake.py)

* Abra em um editor de texto e descomente as linhas 12 e 13 e comente a linha 14. O código deve ficar como abaixo:

````python
# only execute the following lines if you want to create a new q-table
qlearn = QLearning(env, alpha=0.9, gamma=0.95, epsilon=0.7, epsilon_min=0.1, epsilon_dec=0.9999, episodes=100000)
q_table = qlearn.train('data/q-table-frozen-lake.csv','results/actions_frozen_lake')
#q_table = loadtxt('data/q-table-frozen-lake.csv', delimiter=',')
````

* Execute o arquivo [FrozenLake.py](FrozenLake.py) com o comando:

````bash
python FrozenLake.py
````

* Os dois arquivos, TaxiDriver.py e FrozenLake.py, geraram os arquivos results/actions_taxidriver.jpg e results/actions_frozen_lake.jpg, respectivamente. Existe uma diferença significativa entre os arquivos? Se existir, diga qual é e justifique a sua resposta. 

* Agora faça o algoritmo [FrozenLake.py](FrozenLake.py) ler a Q-table a partir do arquivo gerado anteriormente e veja qual é o comportamento. Execute diversas vezes. Ele consegue chegar ao objetivo sempre? Ele consegue chegar ao objetivo na maioria das vezes? 


## Próximo exercício: MountainCar.py

* Leia a descrição do ambiente em [https://gym.openai.com/envs/MountainCarContinuous-v0/](https://gym.openai.com/envs/MountainCarContinuous-v0/).

Execute o arquivo [MountainCar.py](MountainCar.py) com o comando:

````bash
python MountainCar.py
````

* Antes de mostrar o carro em movimento, a solução imprime um log. Cada linha termina com o texto "Actions in this episode NNN". Por que este texto começa com 200 e espera-se que ao longo da execução este número vá diminuindo?

* A movimentação do carro aconteceu? Foi possível ver o carro se movimentando uma interface gráfica? O resultado apresentado mostrou um carro capaz de chegar no objetivo? 

## Lunar Lander

* Leia a descrição do ambiente em [https://gym.openai.com/envs/LunarLander-v2/](https://gym.openai.com/envs/LunarLander-v2/).

* Execute o script de exemplo: 

```bash
python LunarLander_introduction.py
```

e depois:

```bash
python LunarLander.py
```

## Projetos implementados pelos alunos

Para ver os projetos implementados pelos alunos, acesse o link [Projetos](Projetos.md). Neste link você irá encontrar uma descrição e quais foram os resultados obtidos para cada projeto.

## Referências

- https://gym.openai.com/
- https://github.com/openai/gym/wiki/FrozenLake-v0
- https://github.com/openai/gym/wiki/MountainCar-v0
- https://gym.openai.com/envs/LunarLander-v2/


