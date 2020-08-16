# Projetos 2020

No primeiro semestre de 2020 os seguintes projetos envolvendo aprendizagem por reforço foram implementados: 

## Agente para o ambiente Frozen Lake (FrozenLake-v0)

O ambiente Frozen Lake é um ambiente não determinístico onde um agente deve encontrar um caminho do lugar onde ele está para outro lugar passando por buracos. Se ele chegar no objetivo sem cair no buraco então ele termina a simulação e tem 1 ponto de reward. Se ele cair em um dos buracos então ele termina a simulação com 0 pontos de reward. Como o chão é de gelo, não necessariamente a ação de ir para baixo vai levar o agente para baixo. Isto acontece com todas as quatro ações. Por isso que este ambiente é não determinístico. 

O objetivo deste projeto é identificar os melhores hiperparâmetros para o agente usando uma abordagem de GridSearch. O código está no arquivo [FrozenLakeGridSearch.py](FrozenLakeGridSearch.py). Os valores testados para os hiperparâmetros foram: 

`````
parameters = {
    "alpha": [1, 0.95, 0.9, 0.85, 0.8, 0.7, 0.5, 0.3, 0.2],
    "gamma": [0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.50, 0.3],
    "i_epsilon": [0.9, 0.8, 0.7, 0.5],
    "episodes": [10000, 50000, 100000]
}
`````
O relatório com a apresentação dos melhores resultados está em [grid_results/Report/Report.md](grid_results/Report/Report.md). A análise dos resultados mostra que a melhor configuração é

* alpha = 0.2
* gamma = 0.99
* epsilon = 0.8
* episodes = 100000

Com esta configuração o agente consegue chegar ao destino em 89 simulações das 100 testadas.  

## Jogador de Roleta (Roulette-v0): 

Neste ambiente o agente pode jogar escolher um número entre 0 e 36 em um ambiente modificado de casino.
Para cada rodada da roleta, o agente aposta em um número. O agente recebe uma recompensa de 35 pontos se ele apostar no 0 e o 0 for sorteado. O agente recebe uma recomensa de 1 ponto se ele apostar em um número e a paridade (par ou ímpar) do número sorteado for a mesma que o número escolhido pelo agenda. Em qualquer outra situação o agente recebe uma recompensa de -1. Além de escolher entre 0 e 36, o agente também pode escolher 37 que significa sair do jogo.

Um agente utilizando Reinforcement Learning está implementado em [Roulette.py](Roulette.py). Interessante notar que independente dos hiperparâmetros escolhidos, o resultado é sempre o mesmo: 

`````
python3 Roulette.py               

Action:  37
Reward:  0
Done?  True

Finished!
Total Rewards:  0
`````

Ou seja, *o agente sempre escolhe como primeira ação dele sair do jogo!*


## Jogador de Blackjack:  





## Agente para controlar um módulo lunar: 