# Proposta de atividades

* Faça a instalação do pacote Gym na sua máquina: 

````
pip3 install cmake 'gym[atari]' scipy
````

* Trabalhe com o arquivo [TaxiDriverGym_introduction.py](TaxiDriverGym_introduction.py): 

    * Execute cada um dos comandos que estão no arquivo [TaxiDriverGym_introduction.py](TaxiDriverGym_introduction.py) em um interpretador python para entender o que o que é environment, reward e action. Além de entender detalhes do ambiente. 

    * Quantos espaços possíveis o ambiente Taxi-v3 possui? 

    * Quantas ações o agente que atua no ambiente Taxi-v3 possui? 

    * O que a variável reward retornada por env.step(<number>) significa? 

* Trabalhe com o arquivo [TaxiDriverGym.py](TaxiDriverGym.py):

    * Abra em um editor de texto e descomente as linhas 12 e 13 e comente a linha 14. O código deve ficar como abaixo:
    ````
    # only execute the following lines if you want to create a new q-table
    qlearn = QLearning(env, alpha=0.1, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
    q_table = qlearn.train('data/q-table-taxi-driver.csv')
    #q_table = loadtxt('data/q-table-taxi-driver.csv', delimiter=',')
    ````

    * Execute o arquivo [TaxiDriverGym.py](TaxiDriverGym.py) com o comando:
    ````
    python3 TaxiDriverGym.py
    ````

    Lembre-se que nesta execução o programa irá criar toda a Q-table e armazenar no arquivo data/q-table-taxi-driver.csv. Depois de calcular os valores para a Q-table o programa irá resolver um dos possíveis cenários considerando um estado inicial qualquer. 

    * Agora faça o algoritmo [TaxiDriverGym.py](TaxiDriverGym.py) ler a Q-table a partir do arquivo gerado anteriormente e veja qual é o comportamento. Execute diversas vezes.

    * Qual é o comportamento do agente? Ele sempre consegue encontrar uma solução? As soluções parecem ser ótimas? 

    * Descomente novamente as linhas 12 e 13, comente a linha 14 e faça alpha receber 0 como apresentado na linha abaixo:

    ````
    qlearn = QLearning(env, alpha=0, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
    ````

    * Execute novamente o código [TaxiDriverGym.py](TaxiDriverGym.py). O que aconteceu? Qual é a explicação para este comportamento? 




