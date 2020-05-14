# Proposta de atividades

* Faça a instalação do pacote Gym na sua máquina: 

````
pip3 install cmake 'gym[atari]' scipy
````

* Execute cada um dos comandos que estão no arquivo [TaxiDriverGym_introduction.py](TaxiDriverGym_introduction.py) em um interpretador python para entender o que o que é environment, reward e action. Além de entender detalhes do ambiente.  

* Trabalhe com o arquivo [TaxiDriverGym.py](TaxiDriverGym.py):

    * Abra em um editor de texto e descomente as linhas 12 e 13 e comente a linha 14: 


    ````
    # only execute the following lines if you want to create a new q-table
    qlearn = QLearning(env, alpha=0.1, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
    q_table = qlearn.train('data/q-table-taxi-driver.csv')
    #q_table = loadtxt('data/q-table-taxi-driver.csv', delimiter=',')
    ````

    * Execute o arquivo 

