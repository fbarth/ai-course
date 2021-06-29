# Projetos 2020

No primeiro semestre de 2020 os seguintes projetos envolvendo aprendizagem por reforço foram implementados: 

## Agente para o ambiente Frozen Lake (FrozenLake-v0)

O ambiente Frozen Lake é um ambiente não determinístico onde um agente deve encontrar um caminho do lugar onde ele está para outro lugar passando por buracos. Se ele chegar no objetivo sem cair no buraco então ele termina a tarefa e tem 1 ponto de reward. Se ele cair em um dos buracos então ele termina a tarefa com 0 pontos de reward. 

Neste ambiente o agente consegue executar 4 ações: ir para cima, ir para baixo, ir para esquerda e ir para direita. Como o chão é de gelo, não necessariamente a ação de ir para baixo vai levar o agente para baixo, por exemplo. Isto acontece com todas as quatro ações. Por isso que este ambiente é não determinístico. 

O objetivo deste projeto é identificar os melhores hiperparâmetros para o agente usando uma abordagem de GridSearch. As implementações executam as seguintes etapas:

* Para cada combinação de valores dos hiperparâmetros, a implementação gera uma q-table;
* Esta q-table é avaliada com 100 execuções no ambiente;
* Ao final das execuções são contabilizadas quantas vezes o agente termina a tarefa com sucesso.
* Seleciona-se os hiperparâmetros e a q-table com o maior número de execuções com sucesso. 
* *Opcional*: executa-se N vezes o problema considerando a q-table gerada para validar se o resultado obtido é replicado.

Para este problema existem duas implementações: 

* [GridSearchQ.py](GridSearchQ.py): uma implementação sequencial para definir os melhores hiperparâmetros. O problema desta implementação é o tempo necessário para terminar a execução, visto que a combinação dos possíveis valores dos hiperparâmetros pode ser de fato grande. 

* [GridSearchQConc.py](GridSearchQConc.py): trata-se de uma versão concorrente da implementação acima, ou seja, consegue executar todas as simulações em um tempo bem menor que a versão sequencial. Recomendamos a execução desta versão. Para a execução desta versão é necessário executar a seguinte ordem de comandos:

````bash
./execute_frozen_lake_grid_search.sh
# após terminada a execução
./generate_results_frozen_lake.sh
# isto irah gerar um arquivo grid_results/finalResults_FrozenLake_final.csv com os resultados
````

Os valores testados para os hiperparâmetros foram: 

````json
parameters = {
    "alpha": [1, 0.95, 0.9, 0.85, 0.8, 0.7, 0.5, 0.3, 0.2],
    "gamma": [0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.50, 0.3],
    "i_epsilon": [0.9, 0.8, 0.7, 0.5],
    "episodes": [10000, 50000, 100000]
}
````

O relatório com a apresentação dos melhores resultados está em [grid_results/Report/Report.md](grid_results/Report/Report.md). A análise dos resultados mostra que a melhor configuração é

* alpha = 0.2
* gamma = 0.99
* epsilon = 0.8
* episodes = 100000

Com esta configuração o agente consegue chegar ao destino em 89 simulações das 100 testadas.

### Código GridSearchQ.py

O código do arquivo [GridSearchQ.py](GridSearchQ.py) foi testado e validado para os ambientes `FrokenLake-v0` e `Blackjack-v0`. O método init da classe GridSearchQ recebe o nome do environment para que o mesmo possa ser utilizado pela rotina de grid search.

## Jogador de Roleta (Roulette-v0)

Neste ambiente o agente pode jogar um número entre 0 e 36 em um ambiente modificado de casino.
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


## Jogador de Blackjack (Blackjack-v0)

Este agente sabe jogar Blackjack. Ou melhor, sabe interagir com o ambiente `Blackjack-v0` do projeto OpenAI. 

Esta implementação faz uso de um GridSearch para determinar quais os melhores parâmetros. Os melhores parâmetros encontrados foram: 

`````
Alpha: 0.01
Gamma: 0.0001
Episodes: 700000
`````

Para executar as simulações é necessário executar o arquivo [GridSearchQ.py](GridSearchQ.py) passando como parâmetro no método init o nome do environment "Blackjack-v0". 


## Agente para controlar um módulo lunar

Os códigos estão em [LunarLander_introduction.py](LunarLander_introduction.py) e [LunarLander.py](LunarLander.py) e a documentação está em [../docs/DeepQ-Learning.docx](../docs/DeepQ-Learning.docx).


## Robô de trading implementado por alunos (turma 2021)

