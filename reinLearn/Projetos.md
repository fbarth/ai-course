# Projetos 2020

No primeiro semestre de 2020 os seguintes projetos envolvendo aprendizagem por reforço foram implementados: 

## Agente para o ambiente Frozen Lake

O ambiente Frozen Lake é um ambiente não determinístico onde um agente deve encontrar um caminho do lugar onde ele está para outro lugar passando por buracos. Se ele chegar no objetivo sem cair no buraco então ele termina a simulação tem 1 ponto de reward. Se ele cair em um dos buracos então ele termina a simulação com 0 pontos de reward. Como o chão é de gelo, não necessariamente a ação de ir para baixo vai levar o agente para baixo. Isto acontece com todas as quatro ações. Por isso que este ambiente é não determinístico. 

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

## Jogador de Blackjack:  

## Jogador de Roleta: 

## Agente para controlar um módulo lunar: 